# pi-5 Burmese rails translation (Kathāvatthu «အငြင်းပွားရာ အကြောင်းအရာများကို ဆွေးနွေးခြင်း»): notes

Method (as the approved pi-4 Burmese rails run, pi-4-my/rails/, read only; brief `pi-5-my/burmese-rails-brief.md`):
rails = the harmonised zero-shot (AI_translation/burmese/pi-5-burmese-plain-zeroshot_split_chapters, read only) brought
into agreement with the locked termbase (AI_translation/burmese/pi-5-pali-burmese-termbase-plain.md, sha256 6f2558f8…,
read only; termbase/APPROVED.md; decisions termbase/decisions-A.tsv) and with the §A text inconsistencies of
mapper-my/map-harmonise-notes.md, keeping pi-1 … pi-4 identity, identical Pāli = identical Burmese, the dash and quote
rules and the structure. The zero-shot is built by eight formula generators (make_sample, make_ch2-5, make_ch6-10,
make_ch11-12, make_ch13-16, make_ch17-20, make_ch21-25, make_ch26-31 + my5_formulas.py), so systematic differences are
source patches of a RAILS LAYER run in memory (none of the generators is edited); the remaining single-segment
differences are explicit rules on the built text. **Result (termbase sha256 ee9018fb…, after the termbase change 2026-11-22 «rails-step proposals»): 152 source patches
(families L01 … L39; L38 withdrawn), 198 residual rules (363 replacements); 597 of 3460 non-empty lines changed; GENUINE
left 0; ALL CHECKS PASSED.** Rebuild and check everything with
`zsh 0-INBOX/temp/pipeline/pi-5-my/rails/regen_rails.sh`. Sources: the Pāli, the termbase / decisions / APPROVED.md,
the zero-shot and its generators, its keyword map and the final pi-1 … pi-4 rails only. No Burmese translation,
nissaya or web source was used; language-priority/ was not opened; nothing committed; the system temp folder not used.

## Files
- protected-md5-before.txt: md5s of 137 files recorded before any work (termbase, zero-shot chapters + merged file,
  both keyword files, the generators and the agents' check scripts, my5_formulas.py, terms_my5.py, regen_zeroshot.sh,
  my5-zeroshot-terms.md, notes-*.md, harmonise_pi1234.py / harmonise_align_explained.py / harmonise_scan.py /
  harmonise-notes.md, termbase/APPROVED.md, decisions-A.tsv, termbase-decisions.md, map-harmonise-notes.md, the
  pi-1 … pi-4 termbases and final rails chapters). regen_rails.sh step 0 checks all of them.
- build_rails.py: runs the eight generators in one process, each with fresh my5_formulas / make_sample modules (a
  meta-path finder serves the patched source; make_ch2-5, which never imports make_sample, still does not) and with
  the importlib blocks of make_ch11-12 … make_ch26-31 replaced at source level by the same patched load (make_ch6-10
  inside make_ch11-12, make_ch11-12 inside the later ones). A patch that does not occur exactly its stated number of
  times stops the run. `--plain DIR`: no patches, 32 of 32 files byte-identical to the zero-shot (checked every run).
- my_formulas_rails.py: the layer (PATCHES by file; layer-log.tsv lists the 152 applied patches with reasons; a reason
  names the family, the termbase headword = term and the decision or §A item). Witnessed pi-1 … pi-4 values are kept
  and the pi-5 value derived from them (SVN, _NAV, the ^2-760 list, DEVA_N).
- apply_termbase.py + residual_rules.py → apply-log.tsv: 198 rules; a rule fires only in its segment ids, only when the
  segment's Pāli holds the keyword, and must make its stated number of replacements.
- adherence_my.py (pi-4's, unchanged logic); adherence-zeroshot.txt is the input (23680 checked, 832 misses), reproduced
  each run. classify_misses.py + classify_rules.py → adherence-classified.tsv / classify-out.txt; rails_misses_check.py.
- line_scan.py → line-scan-zeroshot.txt (265 flags) / line-scan-rails.txt (0): 31 families (forbid the replaced
  zero-shot form / require the term on every Pāli line with the form), all with Pāli hits.
- make_proposals.py → termbase-proposals.tsv (coordinator item 3; run and checked in regen step 3).
- pi1234_identity.py (runs harmonise_pi1234.py on the rails folder), align_explained.py (runs
  harmonise_align_explained.py on rails/align-*.txt), check_text_pe_rails.py, diff_count.py → lines-changed.txt,
  output-md5.txt. Inspection / authoring helpers (not part of the checks): misses_view.py, ctx.py, seg.py, where.py,
  work/ (autorules.py, triage.py, addp.py, the spec files, iter.sh).

## Misses by class (zero-shot input re-run under the changed termbase: 928 zero-shot + 2 rails-introduced)
| class | rows | what |
|---|---|---|
| GENUINE | 655 | fixed (layer families L01 … L39 and the rules R…) |
| ARTEFACT | 239 | approved frames (micchā ×44, niggahetabbe, Tena hi); own entries of compounds (idappaccayatā, aññāṇa, paṇītatā, anantarāpayutta, yaṃ kiñci, bhagavā jāto, ṭhito parinibbāyati, bhāvitā bahulīkatā, ekādhippāya, sattamabhavika, mahapphala, sukhavipākā, mātāpitaro, ñāṇadassana); the approved rails-step notes; proper names; privative fragments; «(no direct equivalent)»; the idiom padakkhiṇaṃ kareyya (the 2 rails-introduced rows); kept senses with doubts. No STALE rows are left (the 56 accepted proposals are hits) |
| INFLECTION | 36 | finite «…ရမည်» of the gerundive; the one-syllable verbs «ရ / က»; the noun «(အ)ကြွင်း»; «ဝင်စားနေသူ»; «ရရှိပြီ»; dukkhapariññātaṃ |
| UNVERIFIED | 0 | |

Before this round (termbase 6f2558f8…): 832 zero-shot misses → 377 rails misses (98 of them STALE). After: 928 → 275.

## Layer families (152 patches) and rules (198)
L01 attahitāya «အကျိုးစီးပွား» · L02 upacchedo «ပြတ်စဲခြင်း» · L03 upasampajja (viharati) «ဝင်စား၍ (နေ)» · L04 issariya
«အစိုးရခြင်း» · L05 §A14 the jāta / niruddha lists = ch7 / pi-1 · L06 samāpatti «သမာပတ်», nirodhasamāpatti «ချုပ်ငြိမ်းခြင်း
သမာပတ်», vedayita «ခံစားရခြင်း», jhāyī · L07 mānusaka «လူ့» · L08 kata «ပြုခဲ့» · L09 hīna «ယုတ်ညံ့» · L10 upagā
«ရောက်သွားသော» · L11 diṭṭhadhamma «မျက်မှောက်ဘဝ» · L12 iṭṭha / iṭṭhaphala (§A23) · L13 yaṃ kiñci «မည်သည့် … မဆို»,
nirodhadhamma (§A20), the dhammacakkhu sutta ch3 = ch10, virajaṃ · L14 anuttara «ထိုထက် သာလွန်သည် မရှိသော», uttamo · L15
samanantarā · L16 sayaṃ «ကိုယ်တိုင်» · L17 ṭhito / ṭhitā «တည်နေ» · L18 §A13 ruhiruppādaka «ထွက်စေ» · L19 buddha family
«ဘုရားရှင်» · L20 saha «အတူ» · L21 niruddha «ချုပ်ငြိမ်းပြီး» · L22 tiṭṭhati / saṇṭhāti «တည်နေ» · L23 ekanirodha,
assāsapassāsā · L24 §A19 sukha «ချမ်းသာ», sukhadukkha · L25 paṭivedha family «ထိုးဖောက်၍ သိ…» (coordinator change),
abhisametuṃ, paṭivijānanti · L26 §A24 parinipphanna, arūpadhātu / rūpadhātu planes · L27 abhabba · L28 §A26 saṃvattaniya
· L29 saññī, §A27 pisuṇa, khaṇika, §A26 āneñja · L30 yoni · L31 niyato, samaṅgī, dhammaṭṭhitatā / dhammaniyāmatā · L32
manussaloka, §A28 purisayuga, sabbaso, visineti, akāsi / tapaṃ · L33 akkhātā · L34 §A3 asātarāga «… ရာဂ», dhammavinaya
«တရား» · L35 §A17 «ယောက်ျား» · L36 uppanne, bhabbo … abhisametuṃ, seṭṭho / pavaro, ādittāya · L37 §A28 āpāyiko / nerayiko, §A2 dhuva · L39 sabyābajjhaṃ / abyābajjhaṃ «ညှဉ်းဆဲမှု ရှိသော … ညှဉ်းဆဲမှု ကင်းသော» (coordinator term 2026-11-22; replaces rule R611). L38
sikkhāya withdrawn (proposal (b) rejected: sikkhāya keeps «ကျင့်စဉ်», the eight doubts «ကျင့်စဉ်အပေါ်» = pi-2 Vibhaṅga;
R081 restored at ^5-648); R001 / R336 withdrawn (proposal sattamabhavika rejected: «ခုနစ်ကြိမ်မြောက် ဘဝ၌ ရှိသော» kept,
the ordinal «သတ္တမ» only in the vagga headings; R042 sattamaṃ ^5-402 is not sattamabhavika). Rules R001 … R628: single-segment term differences (one reason each, decision cited),
incl. §A5 añño, §A18 paṭikuṭṭhāni, §A12 cakkaṃ, §A29 jīvitā (R501), §A30 Mahāniyāmo (R502), dāna as the gift (R412).

## Lines changed per chapter (non-empty lines)
preamble 0/3, 1 87/430, 2 11/150, 3 25/77, 4 11/36, 5 29/113, 6 0/23, 7 0/23, 8 2/14, 9 0/21, 10 73/348, 11 13/243,
12 60/202, 13 13/93, 14 12/95, 15 14/154, 16 26/160, 17 10/103, 18 7/103, 19 10/86, 20 9/79, 21 17/87, 22 18/93,
23 25/99, 24 21/107, 25 24/120, 26 3/91, 27 4/81, 28 16/72, 29 14/54, 30 21/56, 31 22/44 — total 597 of 3460.

## §A items (mapper-my/map-harmonise-notes.md)
Fixed: 3 (L34, R004), 4 (L01, R408), 5 (R201 … R203; ^5-488 / ^5-801 kept, doubt), 6 (suddha rule), 12 (cakkaṃ ^5-405),
13 (L18), 14 (L05, R422, R423), 15 (^5-296 rule; the Buddha's other uses keep the honorific, as the decision says), 16
(thero rule), 17 (L35), 18 (^5-480 rule), 19 (L24), 20 (L13), 23 (L12), 24 (L26), 28 purisayuga (L32), 29 (R501),
30 (R502), 31 (^5-321 rule; ^5-338 left), 32 (Arahattasacchikiriyāya rules); partly 10 (iṭṭhā / kantā / rajanīyā /
dvipadānaṃ joined; paṇidahantassa / ābhoga not changed), 26 (āneñja, visineti, ussineti, sobhagya, pariyāye,
saṃvattaniya ch8 / ch30 / ch31, sañcetanika; apacināti and ^5-777 left), 27 (pisuṇa, bhojanīya, ekāgārika; hareyya
and asuci left). Kept by decision: 1 (uddāna / saṃkhitta: the text as written), 7, 9, 21 (vagga ordinals: the harmonise
form), 22 (the siglum «(Sabbattha)» stays Roman, as the other sigla). Already right in the zero-shot: 11 (^5-371 has
«ပညာ နည်း၍ နုံအ ထုံထိုင်းသူ ဖြစ်သလော»; the keyword map is stale). Coordinator follow-up: 2 dhuvayāgū «ခိုင်ခံ့သော ယာဂု» (L37, decision dhuva|0: nicca «မြဲ» and dhuva
«ခိုင်ခံ့» stay apart; wording doubt), niccabhattaṃ «အမြဲ ထမင်း» kept (the stem «မြဲ» = nicca's term); 28 āpāyiko /
nerayiko ^5-861 «အပါယ်သို့ ရောက်သော၊ ငရဲ၌ ကျသော» (L37); 8 kept: gati «လားရာ» is the locked term «here also in the
debate headings» (Gatianuyogo «လားရာကို စစ်ဆေးမေးမြန်းခြင်း» follows it); 25 kept: puññūpacaya / puññūpacayo have
their own locked entries «ကောင်းမှု စုဆောင်းခြင်း» (upacaya «စုဆောင်းမှု» is kammūpacaya's word). Also done since: 26
apacināti (R626), saṃvattaniya ch24 (R612); 27 nillopaṃ hareyya (R613), paripanthe tiṭṭheyya (R628); asuci kept
(the decision leaves «… သုက်ထွက်ခြင်း» / «… သုက်» to the context).
The 8 lines with fewer quote marks than the Pāli (1:27, 10:157, 10:251-253, 10:342, 25:44, 26:130): not changed
(left; check_marks passes as before).

## Checks (regen_rails.sh, all pass)
- Protected files: 137 md5s unchanged against the record; the record holds the coordinator's new md5s of the termbase
  (line 35, set by the coordinator) and of termbase/APPROVED.md, decisions-A.tsv, termbase-decisions.md (changed by the
  coordinator's termbase change procedure, recorded here 2026-11-22); termbase sha256 = the new lock (ee9018fb…).
- Reproduction: build without the layer = zero-shot, 32 of 32 files byte-identical.
- check_chapter_ids, check_text_pe (wrapper) and check_marks: all 32 files OK; typography OK.
- Adherence: zero-shot 928 misses under the changed termbase (adherence-zeroshot.txt re-run; reproduced each run) →
  rails 275 = 239 ARTEFACT + 36 INFLECTION, all known rows; GENUINE fixed 655, left 0; 0 unverified.
- align_check_my: 690 repeated Pāli sentences, 1 differing = the accepted 1:426, none new; align_hidden_my: 0 unmatched.
- pi-1 … pi-4 identity: 2 / 2, 4 / 4, 2 / 21 + 19 explained, 5 / 7 + 2 explained (unchanged).
- line_scan: 0 lines left (zero-shot 265 flags; 31 of 31 families with Pāli hits).
- Rerun: a second regen_rails.sh run changes no byte (45 files).

## Termbase proposals (rails/termbase-proposals.tsv, the record of the 60 lines sent; applied 2026-11-22)
60 lines: (a) 58 stale phrase entries (the 98 STALE rows), new term = the rails wording; (b) sikkhāya «သိက္ခာ» (one word
for the training with sikkhā / sikkhaṃ / sikkhāyo «သိက္ခာ», pi-2 / pi-4 locked; «ကျင့်စဉ်» is paṭipadā's word; the text
already reads «သိက္ခာ», L38); (c) voropetvā «ချ၍» (§A29). After they are applied the STALE and the (b) / (c) rows become
hits; re-run regen_rails.sh with the new sha256 (TB_SHA, step 0).
Outcome: 56 stale phrase entries and voropetvā «ချ၍» accepted (hits now); sattamabhavika / sattamabhavikassa and
sikkhāya rejected (text reverted, see the layer section); coordinator's own new term sabyābajjhaṃ (L39).
make_proposals.py is no longer run by regen_rails.sh (the proposals are applied).

## Termbase doubts (termbase not changed)
1. **Stale phrase entries** (98 rows): many single-candidate phrase entries copy the zero-shot wording of a member word
   whose locked decision says the word «aligns» (nirodhasamāpatti «ချုပ်ငြိမ်းရာ ဈာန်» in 10 entries vs samāpatti /
   nirodhasamāpatti «သမာပတ်»; Saha upapattiyā «တစ်ပြိုင်နက်» vs saha «အတူ»; paññācakkhuṃ anuttaraṃ «အမြတ်ဆုံး» vs
   anuttaraṃ; Sukhānuppadāna «သုခ» vs sukha §A19; the Issariya headings «မိမိ၏ အစွမ်း» vs issariya; X-phalasamaṅgī
   «ရရှိထားသော» vs samaṅgissa; saṃvattaniko «ပို့ဆောင်တတ်» vs saṃvattaniyaṃ §A26; niyato okkamati …). The rails follow
   the explicit decisions; the phrase entries should be rebuilt from the rails text.
2. **sahajātaṃ**: jātaṃ «မွေးဖွားပြီးသော» covers sahajātaṃ, while sahajāta / sahajātā / sahajāto «အတူ ပေါ်ပေါက်…» in the
   same lists; kept «… အတူ ပေါ်ပေါက်သော» (one compound, one word).
3. **añño aññassa** (^5-488, ^5-801) is the reciprocal; the term «တခြားစီ» (separate) misfits; kept «… အခြား…».
4. **vācāya** «နှုတ်» (the door of speech) vs the speech itself «… စကား» (as pi-4 doubt 3).
5. **sikkhā «သိက္ခာ» vs sikkhāya «ကျင့်စဉ်»**: proposal (b).
8. **dhuvayāgū «ခိုင်ခံ့သော ယာဂု»** (regular gruel) follows decision dhuva|0 but reads «firm»; to check.
9. **seṭṭho / pavaro at ^5-799**: the termbase pavaro «အမွန်မြတ်ဆုံး» was the text's second word (seṭṭho's place); the
   rails give seṭṭho «အကောင်းဆုံး» (second) and pavaro «အမွန်မြတ်ဆုံး» (fifth).
6. **su / du gandha** (^5-522): the smell words «မွှေးသော / နံစော်သော» kept (decision du|0 «Burmese speaker to check»).
7. **Wording to check by a Burmese speaker**: issariyakāmakārikā «အစိုးရခြင်းဖြင့် အလိုရှိတိုင်း ပြုခြင်း», mātusaññī /
   dhammasaññī «မှတ်သိ», «ချမ်းသာနှင့် ဆင်းရဲ» for sukhadukkha in the ch24 views.

## Bilingual-review fixes (2026-11-22, review/fix-brief.md; details in review/fix-notes.md)
Layer families L40–L51 (28 patches: A2 + A3, B4, B6, B7, B8, B9, B12, B13, B15, A16, B1, B5; layer now 180 patches),
R501 retargeted to the new termbase «အမိကို အသက်မှ သတ်၍», R203 withdrawn (A17; 197 rules), and apply_fixes.py
(F01–F44, 43 single-segment rules, 84 replacements, log fixes-log.tsv; run by regen_rails.sh after apply_termbase.py).
Termbase dbc04869…: zero-shot input 943 misses; rails 292 = ARTEFACT 256 + INFLECTION 36, GENUINE left 0; 675 of 3460
lines changed against the zero-shot (124 against the pre-fix rails); ALL CHECKS PASSED, second run byte-identical.
