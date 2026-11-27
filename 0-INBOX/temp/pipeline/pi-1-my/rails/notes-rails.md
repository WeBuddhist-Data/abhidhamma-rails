# pi-1 Burmese rails translation (သဘောတရားများကို စုစည်းရေတွက်ခြင်း): notes

Method (as the Marathi pi-1 rails, adapted): rails = the harmonised zero-shot (AI_translation/burmese/pi-1-burmese-plain-zeroshot_split_chapters, read only) brought into agreement with the locked termbase (AI_translation/burmese/pi-1-pali-burmese-termbase-plain.md, sha256 09668de0fa34…, read only; termbase/APPROVED.md). The zero-shot is built by formula generators (pi-1-my/make_*.py + my_formulas.py), so the systematic differences are fixed in a RAILS LAYER that runs those generators' own logic with in-memory source patches (identical Pāli keeps identical Burmese everywhere); the residual single cases are explicit rules on the built text. Output: AI_translation/burmese/pi-1-burmese-plain-rails_split_chapters/ (14 chapters, same filenames). Rebuild and check everything with `zsh 0-INBOX/temp/pipeline/pi-1-my/rails/regen_rails.sh`. Sources: the Pāli, the termbase and the zero-shot only (no Burmese translation, nissaya or web source; no Marathi wording).

## Files
- protected-md5-before.txt: md5 of the termbase, the zero-shot chapters and merged file, the generators, my_formulas.py, regen_zeroshot.sh, my-zeroshot-terms.md and the generators' notes files, recorded before any work; regen_rails.sh step 0 checks them (unchanged).
- adherence_my.py: Burmese adherence (adherence_loose.py adapted): a keyword passes if any termbase sense's term occurs in the segment; a term occurs if each content chunk occurs after stripping ၏ ကို ၌ တွင် နှင့် မှ ဖြင့် အား သို့ သည် က များ တို့ and the endings သော / သည် / ၍ / ခြင်း / မှု (at least 2 code points kept). Reports are tab-separated.
- adherence-zeroshot.txt: input (32243 checked, 487 misses); regen_rails.sh reproduces it from the zero-shot and checks it is unchanged.
- my_formulas_rails.py: the layer: FORMULA_PATCHES (my_formulas.py) and GEN_PATCHES (per generator), each (old, new, count, reason «Lnn headword = term»).
- build_rails.py: runs make_sample, make_ch2-01, make_ch2-02-03, make_ch2-04-05, make_ch3, make_ch4, make_ch5 in one process, each with a fresh patched my_formulas module (as each zero-shot generator runs in its own process), OUT set to the rails folder; only the chapter writers are called (never write_terms / write_notes, so my-zeroshot-terms.md and notes-ch*.md are not touched). A patch that does not occur exactly its stated number of times stops the run before anything is written. `--plain DIR` builds without patches: it reproduces the zero-shot byte for byte (checked: 14 of 14 identical). Log: layer-log.tsv (63 source patches).
- apply_termbase.py → apply-log.tsv: residual rules (segment ids, Pāli keyword check, exact replacement count; nothing written on a mismatch).
- classify_misses.py → adherence-classified.tsv: all 487 zero-shot misses plus the 20 misses the rails introduce, one row each (id, keyword, termbase term, text form, class, reason, ch, src). GENUINE rows name their layer patch / rule, which must have been applied in the build, their old form must be in the zero-shot segment and the keyword must pass in the rails segment; INFLECTION / ARTEFACT rows carry a text-form regex that must match the segment and, where given, a Pāli check (privative, compound, negation present). The run fails on any unverified row.
- rails_misses_check.py: every miss left in the rails must be a known INFLECTION / ARTEFACT row.
- line_scan.py → line-scan-zeroshot.txt / line-scan-rails.txt: per-line check of the GENUINE families (required termbase form present, old form gone). Zero-shot: 699 flags; rails: 0.
- rejected_scan.py: blind-spot scan (decided senses whose rejected candidate is still in a segment that holds the headword); it found the nominaliser and domanassa families (L26, L27).
- align-rails.txt / align-hidden-rails.txt, adherence-rails.txt: check outputs. diff_count.py: lines changed per chapter.
- seg.py, ctx.py, kwic.py, scan.py: inspection helpers used for the classification.

## Misses by class (487 zero-shot + 20 rails-introduced)
| class | rows | what |
|---|---|---|
| GENUINE | 405 | all fixed: Yo / Yaṃ / yo / yaṃ / yañca 208 (L02 205, R01–R02 3), uppanna family 99 (L01: uppannaṃ 49, cittaṃ uppannaṃ 12, dhātu uppannā 10, uppannā 10, uppanno 8, uppanne 10), kusalato / vipākato / kiriyato ca 38 (L23), ākāsa 12 (L03), Catukkanayo / Pañcakanayo / nayo 8 (L07), kāyiko / vācasiko 8 (L13), rūpañca nibbānañca 6 (L24), paṭicca / paṭiccasamuppādakusalatā 3 (L04), indriyānaṃ 3 (L09), vibhava 3 (L11), samuppannā 2 (L22), kammassa katattā 2 (L10), dhammānaṃ vipākato 2 (L12), (an)uppādāya 2 (L20), 1 each: samāpatti (L06), Suddhikaappaṇihitaṃ (L08), kodha (L14), kaṇṇasukhā (L15), hadaya (L16), bhiyyokamyatā (L17), bojjhaṅgā (L18), Saṃvego (L19), anussati (L21) |
| INFLECTION | 2 | Saṃviggassa / saṃviggassa «သံဝေဂ ရသူ၏» (person genitive of the termbase «သံဝေဂ ရသော», approved Mātikā wording; doubt 7) |
| ARTEFACT | 80 + 20 | privative / negation 62: anikkhitta- 17 «လက်မလွှတ်ခြင်း», adussanā 7, amanasikārā 4 «နှလုံး မသွင်းခြင်း», anavasesa- 3 «အကြွင်းအကျန် မရှိ», the not-arisen / future lists ajātā … asamuṭṭhitā 18 («မ…သေးသော»), na / neva … pahātabbā 8 (style rule «ပယ်ရမည် မဟုတ်»), asekkhā 2, aññāṇaṃ 2, adhāraṇatā 1; compound with its own entry 13: dvedhāpatho 5, anekaṃsaggāho 4, ketukamyatā 2, dovacassatā 2; -vidhena numerals 4 (Dasa / Ekādasa «ဆယ်မျိုး / ဆယ့်တစ်မျိုး», vidhena = မျိုး); proper name 1 (Paranimmitavasavattī, rule 1 of APPROVED.md); rails-introduced 20: kusalato ca vipākato, termbase conflict (doubt 1) |

Two ARTEFACT rows (samuppannā in the not-arisen lists 1-1042 / 1-1045) pass in the rails as a side effect of L22 («မဖြစ်ပေါ်လာသေးသော»).

## Layer overrides (63 source patches) and rules (2 entries, 3 replacements)
- L01 uppanna = «ဖြစ်ပေါ်ပြီးသော»: my_formulas UPPANNA (the citta-opening formula of all 2-0x chapters, «… စိတ်သည် ဖြစ်ပေါ်ပြီးသော အချိန်၌»), make_ch5 ETTH «ထိုတို့၌ ဖြစ်ပေါ်ပြီးသော» and UPP (uppanno lobho …, uppanno ca vicāro). samuppannā stays «ဖြစ်ပေါ်လာသော» (closing formula). 3 patches.
- L02 Yo / Yaṃ / yañca = «… ရှိသမျှ» (decision Yo|0: the text's «… ရှိသမျှ» form): the definition list «Yo / Yā / Yaṃ [tasmiṃ samaye] [GEN] A B C – ayaṃ …» becomes «ထိုအချိန်၌ A၊ B၊ C ရှိသမျှ – ဤသည်မှာ …» (was «ထိုအချိန်၌ ရှိသော A …»; the closers «ဤသည်မှာ ထိုအချိန်၌ ရှိသော X ဖြစ်သည်» are «hoti» and stay). Patched in my_formulas r_rel (+ YO_REL), the hiri / ottappa BODY, make_ch2-02-03 r_rel_comma, make_ch2-04-05 (ahirika / anottappa), make_ch3 («Yo āyatanānaṃ ācayo, so …», «Yo rūpassa upacayo, sā …», r_elem «Yaṃ kakkhaḷaṃ … ရှိသမျှ၊ မိမိ၌ ရှိသည်ဖြစ်စေ …», r_vaca), make_ch4 (r_rel, «Yo kāyiko …, kāyikavācasiko … ရှိသမျှ –», the four hiri / ottappa pieces (its assert still holds), «Yo eva so dhammo appaccayo» «အကြောင်း မရှိသော သဘောတရား ရှိသမျှ» (was «အကြင်»), «yañca rūpaṃ kammassa katattā uppajjissati» «… ရုပ် ရှိသမျှလည်း»). The frame regex covers Yā as well (no entry; doubt 3). 21 patches. Residual rules R01 (1-1287) / R02 (1-1289, 1-1291): «yaṃ etasmiṃ antare …» «… ရှိသမျှ».
- L03 ākāsa = «ဟင်းလင်းပြင်»: ākāsānañcāyatana in my_formulas and make_ch2-04-05 (AKASA) «အဆုံး မရှိသော ဟင်းလင်းပြင် နယ်ပယ်» (was ကောင်းကင်). 2.
- L04 paṭiccasamuppādakusalatā «အကြောင်းတို့ကို မှီ၍ ဖြစ်ပေါ်ပုံ၌ ကျွမ်းကျင်ခြင်း» (Mātikā and 4-03; APPROVED.md). 1.
- L05 Suññatavāro «ဆိတ်သုဉ်းခြင်း ဖော်ပြချက်» (APPROVED.md; heading + colophon; no keyword miss, found by the line scan). 1.
- L06 samāpattivuṭṭhānakusalatā «ဈာန် ဝင်စားရာမှ ထမြောက်ရာ၌ ကျွမ်းကျင်ခြင်း» (samāpatti compound member, vuṭṭhāna = ထမြောက်ရာ; Mātikā and 4-03). 1.
- L07 Catukkanayo / Pañcakanayo «ဈာန် လေးပါး / ငါးပါး ခွဲနည်း» (headings and colophons, 2-02). 1.
- L08 Suddhikaappaṇihitaṃ «တောင့်တမှု မရှိသော ဈာန် သက်သက်» (heading, 2-05). 1.
- L09 indriyānaṃ paripāko «အာရုံခံ အင်္ဂါတို့ ရင့်ရော်ခြင်း» (ageing of matter, 3-02 / 3-03). 1.
- L10 kammassa katattā «ပြုခဲ့သော ကံကြောင့်» (make_ch4 KAMMA_KATATTA, make_ch5 «yañca rūpaṃ (na) kammassa katattā»; was «ကံကို ပြုခဲ့ခြင်းကြောင့်»). 3.
- L11 vibhavataṇhā «ဘဝ ပျောက်ကွယ်ခြင်းကို တပ်မက်မှု» (APPROVED.md). 1.
- L12 «Kusalānaṃ (vā) dhammānaṃ vipākato» «ကုသိုလ် သဘောတရားတို့၏ အကျိုး ဖြစ်သော စိတ်၌(ဖြစ်စေ)» (vipākato = အကျိုး ဖြစ်သော စိတ်). 2.
- L13 kāyiko / vācasiko «ကိုယ်ပိုင်းဆိုင်ရာ / နှုတ်ပိုင်းဆိုင်ရာ (မ)ကျူးလွန်ခြင်း», kāyikavācasiko «ကိုယ်ပိုင်းဆိုင်ရာနှင့် နှုတ်ပိုင်းဆိုင်ရာ». 1.
- L14 kodhasāmantā «အမျက်ဒေါသနှင့် နီးစပ်သော»; L15 kaṇṇasukhā «နား သာယာသော»; L16 hadayaṅgamā «နှလုံးသားသို့ ရောက်သော»; L17 bhiyyokamyatā «ပိုမို လိုချင်ခြင်း»; L18 bojjhaṅgā / sambojjhaṅgo «ဗောဇ္ဈင်» (2); L19 Saṃvegoti «သံဝေဂ ရခြင်း ဟူသည်»; L20 (an)uppādāya «(မ)ဖြစ်ပေါ်ရန်» (2); L21 pubbenivāsānussati «ရှေးဘဝများကို အဖန်ဖန် အောက်မေ့နိုင်သော ဉာဏ်» (4-03, all make_ch4).
- L22 samuppannā «ဖြစ်ပေါ်လာသော» in the arisen-states list (was «ကောင်းစွာ ဖြစ်ပေါ်ပြီးသော»), and asamuppannā «မဖြစ်ပေါ်လာသေးသော» built from it as the list builds every «မ…သေးသော» (no entry). 2.
- L23 «kusalato ca vipākato ca kiriyato ca» (and the two-member forms) «ကုသိုလ်စိတ်အနက်လည်းကောင်း၊ အကျိုး ဖြစ်သော စိတ်အနက်လည်းကောင်း၊ ပြုရုံမျှသာ ဖြစ်သော စိတ်အနက်လည်းကောင်း» (decided kusalato / vipākato / kiriyato and «vipākato ca kiriyato»; was «… အဖြစ်လည်းကောင်း»). 3.
- L24 rūpañca nibbānañca «ရုပ်လည်း နိဗ္ဗာန်လည်း» (also as subject: «ရုပ်လည်း နိဗ္ဗာန်လည်း အာရုံ မရှိသော …»). 1.
- L25 kusalahetu / kusalahetū / akusalahetū «ကုသိုလ် / အကုသိုလ် အမြစ်», abyākatahetū «… မဟုတ်သော အမြစ်» in chapter 5 (as 4-01; re-alignment kusalahetu|0). 3.
- L26 sineho «ချစ်ခင်မှု», mucchā «မိန်းမောမှု», santuṭṭhitā «ရောင့်ရဲမှု» (decided nominalisers; lobha lists 1-1065 / 1-1141 / 1-1236, 1-1355). 3.
- L27 domanassa «စိတ်ဆင်းရဲမှု» in sokaparidevadukkhadomanassupāyāsā (1-1343) and abhijjhādomanassā (1-1352, 1-1354). 2.
- Kept: identical Pāli = identical Burmese (align 0 / 0), synonym lists distinct (list_items raises on a shared word; the build passes), the two binding rules (Paranimmitavasavattī unchanged; nāma-rūpa untouched), the dash rule (check_marks OK), structure (ids / lines OK).

Lines changed per chapter (569 of 2,436 non-empty lines): 2-04 124, 2-01 117, 4-03 62, 2-03 61, 5-atthakatha 52, 4-01 40, 4-02 32, 3-02 28, 2-05 21, 3-03 20, 2-02 10, 1-matika 2, 3-01 0, preamble 0.

## Checks (regen_rails.sh)
- Protected files: 33 md5s unchanged (termbase, zero-shot chapters and merged file, generators, my_formulas.py, regen_zeroshot.sh, my-zeroshot-terms.md, notes-ch*.md).
- check_chapter_ids, check_text_pe (pi-6-mr/chk-pe copies removed again), check_marks: all 14 chapters OK; harmonise_typo: no «?», no Zawgyi range, NFC.
- Adherence: zero-shot 32243 checked, 487 misses; rails 32243 checked, 100 misses = 98 ARTEFACT + 2 INFLECTION, all known rows; GENUINE left 0 (405 fixed).
- align_check_my: 418 repeated Pāli sentences, 0 differing; align_hidden_my: 18 uneven lines, 0 unmatched.
- line_scan: 0 lines left (zero-shot 699 flags).
- A second regen_rails.sh run changes no byte (14 chapters + all rails/ tsv / txt outputs).

## Termbase doubts (termbase not changed)
1. **kusalato ca vipākato = «ကုသိုလ်အဖြစ်လည်းကောင်း ကံ၏ အကျိုးအဖြစ်လည်းကောင်း»** (single candidate, not decided) contradicts the decided kusalato «ကုသိုလ်စိတ်», vipākato «အကျိုး ဖြစ်သော စိတ်» and «vipākato ca kiriyato = အကျိုး ဖြစ်သော စိတ်အနက်လည်းကောင်း …», whose decision names «jhānā kusalato ca vipākato ca kiriyato ca» itself. Both cannot hold in the same phrase; the rails follow the decided entries (L23), which leaves 20 rows ARTEFACT. A value «ကုသိုလ်စိတ်အနက်လည်းကောင်း အကျိုး ဖြစ်သော စိတ်အနက်လည်းကောင်း» would settle it.
2. **Yeva = «အကြင်»** while Yo / Yaṃ / ye = «ရှိသမျှ» and decision Yo|0 rules «အကြင်» out as nissaya style. Kept (1-1091 «အကြင် သဘောတရားများသည် …»), so 1-1091 «Yeva te dhammā …» and 1-1092 «Yo eva so dhammo …» (now «… ရှိသမျှ») differ. Ye ye = «အကြင် အကြင်» likewise.
3. **Yā has no entry.** The rails give the definition-list Yā the same «… ရှိသမျှ» as Yo / Yaṃ (one frame for Yo / Yā / Yaṃ in the generators).
4. **Scope of the relative = «ရှိသမျှ».** Applied to the definition lists and every keyword-tagged relative. The correlative organ / object heads («Yaṃ cakkhu … pasādo …, yena cakkhunā …», «Yaṃ rūpaṃ … vaṇṇanibhā …», «Yo saddo …»), «Yaṃ taṃ rūpaṃ X, taṃ Y», «Yā sā vācā …» and the sense-door relatives (yena / yamhi / yaṃ … nissāya) keep the zero-shot's Burmese relative clause; the keyword map does not tag them. If the entry is meant for every relative pronoun, about 60 more lines need it.
5. **kammassa katattā** is glossed «said of kamma-born matter»; the vipāka opening «kusalassa kammassa katattā upacitattā» keeps «ကုသိုလ်ကံကို ပြုခဲ့၍ ဆည်းပူးခဲ့သောကြောင့်» (katattā / upacitattā entries).
6. **sineho** has only the affection sense; the water element «sineho sinehagataṃ» (cohesion, «စေးကပ်မှု») needs its own sense.
7. **Saṃviggassa = «သံဝေဂ ရသော»** is attributive; the approved Mātikā and 4-03 have the person genitive «သံဝေဂ ရသူ၏» (kept, INFLECTION). «သံဝေဂ ရသူ» would fit the genitive of a person.
8. **Dasa / Ekādasa (and dasa / ekādasa) = «ဆယ်ပါး / ဆယ့်တစ်ပါး»**: the keyword map tags them inside dasavidhena / ekādasavidhena, where vidhena = «မျိုး» gives «ဆယ်မျိုး / ဆယ့်တစ်မျိုး» (kept).
9. **samāpatti** has only the compound member «ဈာန် ဝင်စားရာ» (applied in samāpattivuṭṭhānakusalatā, L06); the plural noun (atthi … samāpatti, tāsaṃ samāpattīnaṃ, tāhi samāpattīhi) keeps «ဈာန် ဝင်စားမှု».
10. **Suddhikasuññataṃ** (no entry) keeps «ဆိတ်သုဉ်းခြင်း သက်သက်» while Suddhikaappaṇihitaṃ is now «တောင့်တမှု မရှိသော ဈာန် သက်သက်»; «ဆိတ်သုဉ်းသော ဈာန် သက်သက်» would mirror it (as the headings Suññataṃ / Appaṇihitaṃ).
11. **anindriyabaddharūpañca nibbānañca** (no entry, chapter 5) keeps «…နှင့် နိဗ္ဗာန်», while rūpañca nibbānañca is «ရုပ်လည်း နိဗ္ဗာန်လည်း».
12. **pubbenivāsānussati**: the anussati entry «အဖန်ဖန် အောက်မေ့ခြင်း» is applied («ရှေးဘဝများကို အဖန်ဖန် အောက်မေ့နိုင်သော ဉာဏ်»), but the same decision's reason quotes pubbenivāsānussati as «ရှေးဘဝများကို အောက်မေ့ခြင်း» without «အဖန်ဖန်».

## Bilingual-review fixes (2026-11-17, review/fix-notes.md)
- Rails layer L28–L35 (my_formulas_rails.py): L28 bahiddhā = «မိမိ၏ ပြင်ပ၌» (the user-approved termbase change, new sha256 eafe0f8d0f22…), L29–L32 A1–A5, L33 B4, L34 B9, L35 B11. New `apply_fixes.py` (run after apply_termbase.py; log fixes-log.tsv): F1 B8, F2 B1, F3 B2. Doubt 10 above is settled by L31 (A4).
- Not applied (locked termbase, user decision needed): B6, B7, B10.
- 159 lines changed against the pre-fix rails; all checks pass; a second run is byte-identical.

## Review fixes B6 / B7 / B10 (2026-11-17)
User-approved termbase change (termbase/APPROVED.md, sha256 3c8cc8d0…): L36 cittahetuka «စိတ်ကို အကြောင်းပြုသော» (6), L37 byāpajjanā / byāpajjitattaṃ on the byāpatti stem (7 lists), L38 ucchedadiṭṭhi without «သေပြီးနောက်» (3). Classifier and line scan extended (L36–L38, one ARTEFACT row for hetukaṃ in cittahetukaṃ). All checks pass; 706 lines differ from the zero-shot.
