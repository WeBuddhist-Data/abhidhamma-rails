# pi-4 Burmese rails translation (Puggalapaññatti «ပုဂ္ဂိုလ်များကို သတ်မှတ်ဖော်ပြခြင်း»): notes

Method (as the approved pi-3 / pi-2 Burmese rails runs, pi-3-my/rails/ and pi-2-my/rails/, read only; brief `pi-4-my/burmese-rails-brief.md`): rails = the harmonised zero-shot (AI_translation/burmese/pi-4-burmese-plain-zeroshot_split_chapters, read only) brought into agreement with the locked termbase (AI_translation/burmese/pi-4-pali-burmese-termbase-plain.md, sha256 c6a4e611…, read only; termbase/APPROVED.md; decisions termbase/decisions-A.tsv), keeping pi-1 / pi-2 / pi-3 identity, the approved person-type names, proper names, nāma-rūpa / bahiddhā rules, identical Pāli = identical Burmese, the dash rule and the structure, and with the 15 text inconsistencies of mapper-my/map-harmonise-notes.md («Text inconsistencies for the rails step», H1 … H15) settled where the locked termbase decides them. The zero-shot is built by formula generators (pi-4-my/make_sample.py, make_ch3-4.py, make_ch5.py, make_ch6-11.py + my4_formulas.py), so every systematic difference is fixed in a RAILS LAYER that runs those generators' own logic with in-memory source patches (none of them is edited). Residual single cases would be explicit rules on the built text (apply_termbase.py); none was needed. **Result: 36 source patches (families L01 … L25), 0 residual rules; 49 of 561 non-empty lines changed.** Output: AI_translation/burmese/pi-4-burmese-plain-rails_split_chapters/ (12 files: preamble + 11 chapters, same filenames). Rebuild and check everything with `zsh 0-INBOX/temp/pipeline/pi-4-my/rails/regen_rails.sh`. Sources: the Pāli, the termbase / decisions / APPROVED.md, the zero-shot and its generators, its keyword map and the final pi-1 / pi-2 / pi-3 rails only. No Burmese translation, nissaya or web source was used; language-priority/ was not opened; nothing committed.

## Files
- protected-md5-before.txt: md5s of 84 files, recorded before any work: the pi-4 termbase, the zero-shot chapters (12), merged file and keyword map, the four generators, my4_formulas.py, terms_my4.py, regen_zeroshot.sh, my4-zeroshot-terms.md, notes-*.md, harmonise_pi123.py, termbase/APPROVED.md, decisions-A.tsv, termbase-decisions.md, mapper-my/map-harmonise-notes.md, the pi-1 / pi-2 / pi-3 termbases and the pi-1 (14), pi-2 (19) and pi-3 (16) final rails chapters (my4_formulas reads these at import). regen_rails.sh step 0 checks all of them.
- build_rails.py: runs make_sample, make_ch3-4, make_ch5 and make_ch6-11 in one process, each with a fresh my4_formulas module and (for the three that «import make_sample as M») a fresh make_sample module, exactly as regen_zeroshot.sh runs them in separate processes. The make_sample patches apply where it runs and where it is imported. OUT is changed at source level to the rails folder; the «partial-» dump on a stop goes to rails/scratch. Only the chapter writers run (make_ch5: generate() + its SENT5 coverage check); terms_my4.write_terms is never called. A patch that does not occur exactly its stated number of times stops the run. `--plain DIR` builds without patches: 12 of 12 files byte-identical to the zero-shot (checked in every run).
- my_formulas_rails.py: the layer (FORMULA_PATCHES empty; GEN_PATCHES: make_sample 2, make_ch3-4 13, make_ch5 20, make_ch6-11 1). Each reason names the family, the termbase headword = term, the decision and the H item. Where a witnessed pi-2 value holds the old word (the requisite formula ^2-929 / ^2-849), the witness is kept and the pi-4 value derived from it by one explicit replacement. layer-log.tsv: the 36 applied patches.
- apply_termbase.py → apply-log.tsv: residual rules, none (0 entries, 0 replacements).
- adherence_my.py: pi-2's / pi-3's, logic unchanged. adherence-zeroshot.txt is the input (5790 checked, 122 misses); every run reproduces it.
- classify_misses.py → adherence-classified.tsv: all 122 zero-shot misses; the rails introduce none. A GENUINE row needs an applied Lnn family, the keyword map's zero-shot form in the zero-shot segment and the term in the rails segment. An INFLECTION / ARTEFACT row needs its text-form regex on the segment, the keyword map's form among the stated forms, and its Pāli check. The run fails on any unverified row. rails_misses_check.py (pi-2's): every miss left is a known INFLECTION / ARTEFACT row.
- map_vs_termbase.py → map-vs-termbase.txt: sense-level cross-check, stricter than the loose test. Every one of the 5828 keyword-map values must be a term of its entry, or FIXED (the rails segment has the term and no longer the old form), STALE (the term is already in the zero-shot segment; the map took a neighbouring word or an older form), KEPT (name, fragment, grammar, approved note or doubt; the form must still be in the rails), or «(no direct equivalent)» without an entry.
- line_scan.py → line-scan-zeroshot.txt / line-scan-rails.txt: per-line check of 55 families (req / forbid): every layer family and the kept items (the two rails-step notes, gilāna «သူနာ» / «လူနာ», the ^4-M-10 (22) / (23) names, araññagataṃ «ရောက်», bahiddhā). `--stats`: all 55 have Pāli hits. A test on a copy with deliberate errors («ကျင့်သော», «ထောပတ်နှင့်», «စင်စစ်», «ဘဝင်မြင့်သူ») flagged each one.
- pi123_identity.py runs pi-4-my/harmonise_pi123.py (read only) with its zero-shot folder line replaced in memory → pi123-identity-rails.txt. align_kept.py: the rails' set of differing repeated sentences must equal the zero-shot's (0). check_text_pe_rails.py: pi-2's wrapper (copies in rails/chk-pe, deleted). diff_count.py → lines-changed.txt. output-md5.txt: md5s of the rails chapters and rails/ outputs (step 8). Inspection helpers, not part of the checks: seg.py, kw.py, ctx.py, misses_view.py, mapdiff.py.

## Misses by class (122 zero-shot + 0 rails-introduced)
| class | rows | what |
|---|---|---|
| GENUINE | 43 | all fixed (zero-shot 43 → rails 0): ṭhito ×4 (L01), pakāsenti / brahmacariyaṃ pakāsenti ×6 (L05), dīgharattaṃ ×2 (L06), dubbaṇṇo / dubbaṇṇatāya ×2 (L07), abhisamayo / puggalassa abhisamayo ×7 (L12), atthe / atthaṃ / attha ×3 (L13), byañjanaṃ (L14), the paṭipanna family ×9 (L15), abhirūpo (L16), kasira / kasirena ×2 (L17), ābādho (L18), ajinaṃ (L19), sappi (L20), rūpa (L21), raja (L22), ekanta (L23) |
| INFLECTION | 10 | finite «…ရမည်» of the gerundive «…ရမည့်» (cintetabbā ^4-62, upaṭṭhātabbā and desetabbo ^4-94 — desetabbo's verb itself was fixed by L04 —, daṭṭhabbo ^4-202); finite «… ရ၏» of «… ရသည်» (byāpajjati ^4-193 / ^4-197, saṅkhaṃ gacchati ^4-156); agent «နောင်တ ရသူ» (vippaṭisārī ^4-191, ^4-M-11); predicate «ချမ်းသာ ဖြစ်လိမ့်မည်» (phāsu ^4-122) |
| ARTEFACT | 69 | privative fragments: appahīn- «မပယ်ရသေး» ×12, anāvattidhammo ×18, dubbaco, adhāraṇatā, amaccharī, appameyyo, «နှလုံး မသွင်း»; own entries / own words: the book title ^4-0 ×2, paccekasambuddho, pāpadhammo / pāpiccho «ယုတ်မာသော» ×7 (^4-116 now passes only because L07's «ဆိုး» occurs in the segment), sampajānakārī, vaṇṇārahassa vaṇṇaṃ, gilāno / gilānūpamā «လူနာ» ×2, pāṇabhūta … (not bhūtagāma) ×3, Paranimmita, the bracket notes «ဤနည်းတူ» ×3, rajaggasmiṃ; the approved rails-step notes phalaṃ ^4-116 / ^4-117 «အကျိုး» ×2 and indriyānaṃ ^4-M-6 «စွမ်းရည်»; senses the term does not cover (kept, doubts 1 – 4, 7): attanā ×4, vācāya ×3, gahapati, eva, aggaṃ |

Sense-level cross-check: 5828 values; 5619 are a termbase term; 209 explained: FIXED 73 (every Lnn family), STALE 21 (sambuddho «… ဘုရား» ×9, upakkilese ×4, samannāgatā ×3, kantā ×2, vūpasanta ×2, ārāmo: the text already has the term), KEPT 77, no entry 38; 0 unexplained.

## Layer (36 source patches) and rules (0 entries)
| family | termbase / H item | patches | change |
|---|---|---|---|
| L01 | ṭhito «တည်နေ» (H10) | 1 (×2) | «ဖိုလ်၌ တည်သောအခါ» → «ဖိုလ်၌ တည်နေသောအခါ» ^4-29, ^4-30, reused ^4-206, ^4-208 |
| L02 | ^4-M-14 group NAME (H12) | 1 | «မဂ်နှင့် ပြည့်စုံသူ လေးယောက်» → «မဂ်နှင့် ပြည့်စုံသော ပုဂ္ဂိုလ် လေးယောက်»; the same Pāli line reused in the ^4-207 question and answer (ch9 / ch10) follows |
| L03 | suṇāti / sutvā / suṇato «ကြား» (H6) | 4 | «ကြားရ၏» ^4-91 … ^4-93, «ကြားနာ၏ / ကြားနာ၍» ^4-177, «ကြားနာသော်လည်း» ^4-151 |
| L04 | desenti / desetabbo «ဟော» (H1) | 3 | «ဟောကြားကြ၏» → «ဟောကြ၏» ^4-107 … ^4-109; ^4-94 «တရား ဟောကြားရမည်» → «တရား ဟောရမည်» and dhammadesanā (no entry, same sentence) «တရား ဟောခြင်း»; paveda- keeps «ဟောကြား» |
| L05 | pakāsenti «ထင်ရှားပြ» (H1) | 1 | «ထုတ်ဖော် ပြကြ၏» → «ထင်ရှားပြကြ၏» ^4-107 … ^4-109 |
| L06 | dīgharattaṃ (H4) | 1 | «ကြာမြင့်စွာ» → «ရှည်လျားသော ကာလပတ်လုံး» ^4-116 / ^4-117 (no ciraṃ); ciraṃ dīgharattaṃ ^4-113 … unchanged |
| L07 | dubbaṇṇa «အဆင်း ဆိုး» (H9) | 1 | the cloths and the monk ^4-116 |
| L08 | senāsana «အိပ်ရာ နေရာ» (H2) | 2 | the requisite formula ^4-116, ^4-117, ^4-192 |
| L09 | purisapuggalo «ပုဂ္ဂိုလ်» | 2 | «“ဤလူ ပုဂ္ဂိုလ်သည်» → «“ဤပုဂ္ဂိုလ်သည်» ^4-124, ^4-126 |
| L10 | bhogaṃ «စည်းစိမ်» | 1 | «စည်းစိမ်ဥစ္စာကို» ×2 → «စည်းစိမ်ကို» ^4-104 … ^4-106 |
| L11 | unnaḷo / mukharo spacing (H14), vāco «စကားကို ပြော» | 2 | ^4-118 «ဘဝင် မြင့်သူ၊ … စကား များသူ၊ ရှုပ်ပွေစွာ စကားကို ပြောသူ»; ^4-119 «ရှုပ်ပွေစွာ စကားကို မပြောသူ» |
| L12 | abhisamayo «ထင်ထင်ရှားရှား သိမြင်ခြင်း» (H7) | 1 | ^4-148 … ^4-151 |
| L13 / L14 | attha- «အနက်အဓိပ္ပာယ်», byañjanaṃ «စကားလုံး» (H1) | 3 | ^4-149 atthe; ^4-177 sātthaṃ sabyañjanaṃ = ^4-107's «အနက်အဓိပ္ပာယ်နှင့် ပြည့်စုံသော၊ စကားလုံးနှင့် ပြည့်စုံသော»; ^4-189 atthamaññāya |
| L15 | paṭipanna family «ကျင့်ကြံ» (H5) | 4 | ^4-164 / ^4-165 (su-, du-, sammā-, micchā-), ^4-189 dhammānudhammappaṭipanno |
| L16 | abhirūpo / dassanīyo / pāsādiko | 1 | ^4-168 «ရုပ်ချောသူ၊ ရှုချင်ဖွယ် ဖြစ်သူ၊ ကြည်ညိုဖွယ် ဖြစ်သူ» → «အဆင်းလှသူ၊ ရှုချင်ဖွယ် ကောင်းသူ၊ ကြည်ညိုဖွယ် ကောင်းသူ» |
| L17 | kasira «ပင်ပန်း» | 1 | ^4-168 kasiravuttika / kasirena |
| L18 | ābādho «အနာရောဂါ» | 1 | ^4-168 bahvābādho |
| L19 / L20 | ajinaṃ «သမင်သားရေ», sappi «ထောပတ်ကြည်» (H3) | 1 | ^4-176 kharājina, sappitela |
| L21 | rūpa|1 «အဆင်းအရောင်» | 1 | ^4-176 sarūpavaccha «အဆင်းအရောင် တူသော» |
| L22 | raja «ဖုန်လုံး» | 1 | ^4-177 rajāpatho |
| L23 | ekanta «လုံးဝ» | 1 | ^4-177 |
| L24 | nikati «ကောက်ကျစ်ခြင်း» (H8) | 1 | ^4-179 |
| L25 | pamāda «မေ့လျော့မှု» | 1 | surāmerayamajjapamādaṭṭhāyī ^4-132 … ^4-135 |

The other logged items, checked and kept (line_scan K families): H10 / H11 gilāna «သူနာ» only in gilānapaccaya, the sick person «လူနာ» (own entry gilāno); H13 ^4-M-10 (22) / (23): the approved name table has one name per pair (rūpappamāṇo rūpappasanno …, each Pāli word an alias), so the two Burmese names per line stay; H14 dhāraṇatā: ^4-59 «စွဲမှတ် မထားခြင်း» is the negative of «စွဲမှတ်ထားခြင်း» (kept); H15 a Pāli misprint (nothing to do). ^4-198 gataṃ: the text has araññagataṃ … «တောသို့ ရောက်သည်ဖြစ်စေ» (right); the keyword map's «မှား» is a mapping error (map not edited). The rails-step notes: indriyānaṃ ^4-M-6 «စွမ်းရည်» and phalaṃ ^4-116 / ^4-117 «အကျိုး» were already in the text (0 changes, logged as ARTEFACT rows). Person-type names, proper names, bahiddhā and the dash rule unchanged (check_marks OK).

## Lines changed per chapter (non-empty lines)
preamble 0/3, 1 1/185, 2 2/47, 3 0/48, 4 18/57, 5 23/147, 6 1/34, 7 0/8, 8 1/12, 9 1/3, 10 2/11, 11 0/6 — total 49 of 561.

## Checks (regen_rails.sh, all pass)
- Protected files: 84 md5s unchanged; termbase sha256 = the lock (c6a4e611…).
- Reproduction: build without the layer = zero-shot, 12 of 12 files byte-identical.
- check_chapter_ids, check_text_pe (wrapper) and check_marks: all 12 files OK; typography OK.
- Adherence: zero-shot 5790 checked, 122 misses (input reproduced) → rails 78 misses = 68 ARTEFACT + 10 INFLECTION, all known rows; GENUINE fixed 43, left 0; 0 unverified. Sense-level: 0 unexplained of 5828.
- pi-1 / pi-2 / pi-3 identity: 45 / 45, 35 / 36 + 1 explained (harmonise B3 «ထိုသူသည်»), 2 / 2.
- align_check_my: 70 repeated Pāli sentences, 0 with differing Burmese (zero-shot 0; none new); align_hidden_my: 47 uneven lines, 0 unmatched.
- line_scan: 0 lines left (zero-shot 128 flags); 55 of 55 families have Pāli hits.
- Rerun: a second regen_rails.sh run changes no byte (12 chapters + rails/ tsv / txt outputs, 25 files).

## Termbase doubts (termbase not changed)
1. **gahapati** «သူကြွယ်မျိုး» (gloss: the member of gahapatimahāsāla) does not fit the householder himself at ^4-177 «gahapati vā gahapatiputto vā» «သူကြွယ်ဖြစ်စေ»; kept (the decision names it for the speaker / rails step).
2. **attanā** «မိမိကိုယ်တိုင်» (personally) does not fit «X-bhūtena attanā viharati» (^4-177, ^4-178, ^4-185, ^4-M-10) «… မိမိကိုယ်ဖြင့် နေ၏»; kept.
3. **vācāya** «နှုတ်» is the door of speech; pisuṇāya / pharusāya vācāya (^4-137 … ^4-139) is the speech itself «… စကား» (vācā / vācaṃ); kept, as the decision says.
4. **aggaṃ** «ဖျား»: its gloss names the dust cloud, but rajaggaṃ has its own entry «ဖုန်လုံး» and the text (^4-194 «Kimassa rajaggasmiṃ?» «ဖုန်လုံး ဟူသည်») has no «ဖျား» there; the two entries disagree.
5. **nikati / sāci**: with nikati «ကောက်ကျစ်ခြင်း» applied (H8), the ^4-179 list «… vañcana-nikati-sāciyoga» has «ကောက်ကျစ်ခြင်း၊ ကောက်ကျစ်သော နည်းလမ်း»: two synonyms share «ကောက်ကျစ်» (synonym-list rule); a term for one of them would need to change. **Resolved 2026-11-20** (termbase sāci «ကွေ့ဝိုက်သော», review fix F05, review/fix-notes.md).
6. **Cross-book phrases**: pamāda «မေ့လျော့မှု၏ အကြောင်း» (surāmeraya…) and senāsana «အိပ်ရာ နေရာ» in the requisite formula now differ from the pi-2 final rails (^2-703 «မေ့လျော့ခြင်း၏ အကြောင်း», ^2-929 / ^2-849 «ကျောင်းအိပ်ရာနေရာ»), although the pi-2 termbase has the same terms. No shared sentence, so identity is unaffected; deliberate (the locked pi-4 decisions).
7. **eva** «သာ» (only) would change the meaning of the yodhājīva simile ^4-193 … ^4-198 (rajaggaññeva / dhajaggaññeva «… ကိုပင်», tameva saṅgāmasīsaṃ «ထိုစစ်ပွဲ၏ ရှေ့တန်းကိုပင်»); the identifying «ပင်» is kept for the whole simile (one form).
8. **dhammadesanā** has no entry; changed with the desa- family to «တရား ဟောခြင်း» (^4-94, next to desetabbo «ဟောရမည်»), on the decisions' family rule «desa- «ဟော» vs paveda- «ဟောကြား»»; to confirm.
9. **Wording to check by a Burmese speaker**: vikiṇṇavāco «ရှုပ်ပွေစွာ စကားကို ပြောသူ» (vikiṇṇa «ရှုပ်ပွေစွာ» + vāco «စကားကို ပြောသော»), maggasamaṅgino at ^4-M-14 repeats «ပုဂ္ဂိုလ်» where the Pāli has puggalā once.
10. **The keyword map** is stale in places (21 STALE values, and ^4-198 gataṃ «မှား»); it was not rebuilt (read only).
