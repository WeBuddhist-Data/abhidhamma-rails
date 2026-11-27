# pi-6 Burmese rails translation (Yamaka «အတွဲလိုက် မေးဖြေခြင်း»): notes

Method (as the approved pi-5 Burmese rails run, pi-5-my/rails/, read only; brief `pi-6-my/burmese-rails-brief.md`):
rails = the harmonised zero-shot (AI_translation/burmese/pi-6-burmese-plain-zeroshot_split_chapters, read only) brought
into agreement with the locked termbase (AI_translation/burmese/pi-6-pali-burmese-termbase-plain.md, sha256 847e49cd…,
read only; termbase/APPROVED.md, decisions-A.tsv, notes-part5.txt) and with the §A text items of
mapper-my/map-harmonise-notes.md, keeping pi-1 … pi-5 identity, identical Pāli = identical Burmese, the dash and quote
rules, «။» / «၊» and the structure. The zero-shot is built by nine formula generators (make_sample, make_ch2-02-4-5,
make_ch3, make_ch6-8, make_ch7a, make_ch7b (imports make_ch7a), make_ch9-10a, make_ch10b, make_ch10c + my6_formulas.py),
so a systematic change is a source patch of a RAILS LAYER run in memory (no generator is edited); single-segment
differences would be explicit rules on the built text (there are none). **Result: 3 source patches (family L01, §A1),
0 residual rules; 86 of 14213 non-empty lines changed; adherence 333 misses before and after, all INFLECTION; GENUINE
0 (none to fix, none left); ALL CHECKS PASSED; a second run changes no byte.** Rebuild and check everything with
`zsh 0-INBOX/temp/pipeline/pi-6-my/rails/regen_rails.sh`. Sources: the Pāli, the termbase / decisions / APPROVED.md /
notes-part5.txt, the zero-shot and its generators, its keyword map, map-harmonise-notes.md and the final pi-1 … pi-5
rails only. No Burmese translation, nissaya or web source was used; language-priority/ was not opened; nothing
committed; the system temp folder not used.

Why so few changes: the pi-6 termbase was built from this zero-shot's own keyword map and approved as built (1113 of
1128 senses single-candidate kept; the 11 decided and 4 re-aligned senses choose the text's majority form or a form
the text already has). So the zero-shot already carries every locked term; what is left for the rails step is the
§A items that no term decides (notes-part5 5d), of which only §A1 changes the text.

## Files
- protected-md5-before.txt: md5s of 188 files recorded before any work (protected_list.py builds the list): the
  termbase, the 44 zero-shot chapters + merged file, both keyword files, the nine generators and the agents' nine
  check scripts, my6_formulas.py, regen_zeroshot.sh, my6-zeroshot-terms.md, notes-*.md, harmonise-brief / -notes /
  -todo, harmonise_pi12345.py / harmonise_align_explained.py / harmonise_scan.py / harmonise_diff.py, termbase/
  APPROVED.md, decisions-A.tsv, termbase-decisions.md, notes-part5.txt, map-harmonise-notes.md, the pi-1 … pi-5
  termbases and final rails chapters. regen_rails.sh step 0 checks all of them.
- build_rails.py: runs the nine generators in one process, each with fresh my6_formulas / make_ch7a modules (a meta-path
  finder serves the patched source, so a patch applies wherever the file runs or is imported and one generator's
  in-memory table extensions never reach the next), each generator's OUT line pointed at the rails folder (make_ch7b
  uses A.OUT), its own «__main__» block run with no arguments. A patch that does not occur exactly its stated number of
  times stops the run. `--plain DIR`: no patches, 44 of 44 files byte-identical to the zero-shot (checked every run).
- my_formulas_rails.py: the layer (PATCHES by file; layer-log.tsv lists the 3 applied patches with reasons).
- apply_termbase.py + residual_rules.py → apply-log.tsv: 0 rules (header only); kept in the run for the method.
- adherence_my.py (pi-5's, unchanged logic); adherence-zeroshot.txt is the input (27353 checked, 333 misses), reproduced
  each run. classify_misses.py (pi-5's logic) + classify_rules.py → adherence-classified.tsv / classify-out.txt;
  rails_misses_check.py.
- line_adh.py (stricter, added): the adherence test per LINE (every Pāli line with the keyword, the term in the Burmese
  line of the same number): 977 line misses in the zero-shot and in the rails, every one matching an inflection
  pattern (0 unexplained; run by regen_rails.sh step 3).
- line_scan.py → line-scan-zeroshot.txt (172 flags) / line-scan-rails.txt (0): 26 families, all with Pāli hits (L01 and
  «req / forbid / eq» proofs of the decided §A items, the chosen departures and the answer register).
- pi12345_identity.py (runs harmonise_pi12345.py on the rails folder), align_explained.py (runs
  harmonise_align_explained.py on rails/align-*.txt), check_text_pe_rails.py, diff_count.py → lines-changed.txt,
  output-md5.txt (57 output files; the run logs coord-run1.txt / coord-run2.txt, identical, are not in it).
  Inspection helpers (not part of the checks): misses_view.py, seg.py, kwin.py, ctxc.py, forms.py,
  mapdiff.py (keyword-map form vs term: 19 pairs, all the grammar forms below, Atītānāgataṃ spelled out and the
  kātabbaṃ construction of ^6-5-70).

## Misses by class (adherence-classified.tsv; 333 zero-shot rows, 0 rails-introduced)
| class | rows | what |
|---|---|---|
| GENUINE | 0 | none: the termbase was built from this text's keyword map |
| INFLECTION | 333 | plural «ချုပ်ငြိမ်းကြလိမ့်မည်» of nirujjhissanti / -īti / Nirujjhissanti (116); plural «ဖြစ်ပေါ်ကြလိမ့်မည်» of uppajjissanti / -īti (84); the negative «မျက်မှောက် မပြု…» of sacchikarissati / -anti / -atīti / sacchikarittha / -āti (52, §A13: the negative stays spaced); the future participle «… နောက်ဆုံး စိတ် ဖြစ်ပေါ်မည့်သူတို့» of uppajjissati in the relative clause (15); the attributive before another person noun (agent-noun rule, APPROVED.md): upapajjantānaṃ «ပြန်လည် ဖြစ်ပေါ်ဆဲ နောက်ဆုံး ဘဝ ရှိသူတို့» (29), pañcavokārānaṃ «… ဘဝ၌ ရှိသော အခြားသူတို့» (17), (An)abhisametāvīnaṃ «… သိမြင်(ပြီး / ရသေး)သော ပြန်လည် ဖြစ်ပေါ်ဆဲသူ / စုတေဆဲသူ» (16), Pacchimabhavikānaṃ «နောက်ဆုံး ဘဝ ရှိသော မိန်းမ / ယောက်ျား» (2), Itaresaṃ «အခြား ယောက်ျားတို့» (2) |
| ARTEFACT | 0 | |
| CONTEXT | 0 | |
| UNVERIFIED | 0 | |

Each INFLECTION rule names the keyword, a text form that must match the segment, the keyword map's form (where it
differs from the term) and a Pāli check (e.g. «na sacchikar», «Pacchimabhavikānaṃ … upapajjantānaṃ»,
«Itaresaṃ catuvokārānaṃ pañcavokārānaṃ»); a row that no rule verifies fails the run.

## Layer (3 patches) and rules (0)
L01 §A1 «yassa cittassa anantarā» = «အကြင်စိတ်၏ ချက်ချင်း နောက်၌» everywhere: make_ch6-8 OWN_MIND «မိမိ စိတ်» →
«အကြင်စိတ်» (6-01 / 6-02, 61 places), make_ch10b OWN_CITTA «မိမိ {CITTA}၏» → «အကြင်{CITTA}၏» (10-05 … 10-07, 24 places),
make_ch10c OWN_MIND «မိမိ စိတ်» → «အကြင်စိတ်» (10-12, 7 places): 92 places on 86 lines; the book now has one form in
all 273 places (line_scan L01 «eq»: one «အကြင်စိတ်၏ ချက်ချင်း နောက်၌» per Pāli occurrence, no «မိမိ»). Reason: the Pāli
is the same phrase in every place; yassa is the relative pronoun in agreement with cittassa («immediately after which
mind») whatever the main clause's subject is (the last mind «… pacchimacittaṃ uppajjissati» or the persons
«… aggamaggaṃ paṭilabhissanti»), and the Pāli has no word for «own» (မိမိ). The majority correlative form reads it as
written and already stands without a following «ထိုစိတ်၏» in the persons frames of ch. 5 / 9 / 10-09 … 10-11. cittassa
«စိတ်» and anantarā «ချက်ချင်း နောက်» (locked) are unchanged. harmonise B10 had kept two renderings by the subject of
the main clause; the rails step was asked to choose one (§A1), and the subject is not part of this phrase.

## Lines changed per chapter (non-empty lines)
6-01 19/473, 6-02 36/345, 10-05 6/393, 10-06 12/318, 10-07 6/99, 10-12 7/340; the other 38 files 0 —
total 86 of 14213.

## §A items (mapper-my/map-harmonise-notes.md; termbase notes-part5 5d)
Decided by a term (the text already has the locked term; proved by line_scan where a family fits): 2 kāmāvacarānaṃ two
senses (adjective «ကာမဘုံနှင့် ဆိုင်သော နောက်ဆုံး စိတ်» 24 of 24, the beings «ကာမဘုံ၌ ရှိသူတို့၊ နောက်ဆုံး စိတ်၏» 16 of
16); 6 the keyed slips (each the intended word's term); 8 aggamagga / aggaphala apart; 9 sadisa «တူညီ…» (kātabbaṃ
«တူညီအောင် ပြုရမည်» kept, ^6-3-201 / ^6-4-18 / ^6-5-70; «sadisaṃ vitthāretabbā» ^6-6-136 «တူညီစွာ» is the adverb of the
same word); 10 sotaṃ «နား»; 11 uppāda (moment «ဖြစ်ခြင်း ခဏ» 959 hits, vāra «ဖြစ်ပေါ်ခြင်း(အလိုက်)» 37); 12 kāyasaṅkhāra
«ကိုယ်၏ …» (564 hits); 13 sacchikaroti joined, negative spaced (210 hits).
Left for the rails step:
- 1 **fixed** (L01, above).
- 3 **kept**: the colophons «Uddesavāro / Niddesavāro niṭṭhito» «“အကျဉ်း / အကျယ် ဖော်ပြချက်” ပြီးဆုံးပြီ» = the locked
  uddesavāro / niddesavāro «အကျဉ်း / အကျယ် ဖော်ပြချက်» (vāro is the «ဖော်ပြချက်» of the term).
- 4 **kept**: heading IDs out of order in the keyword files; no effect on the text.
- 5 **kept**: keyword gaps; no effect on the text (Catuvokārā is rendered «အစုအဝေး လေးပါး ရှိသော ဘဝ» beside
  pañcavokārā, ^6-2-79 / ^6-2-81; the other gaps are keyword-file splits).
- 6 punctuation / label slips **kept, as written where the Burmese shows them**: ^6-2-36 «.» for «?» (the question is
  rendered as a question; «။» ends both, nothing to change); ^6-2-61 «(Ka)» for «(Kha)» (the label follows the Pāli
  «(က)», as check_marks requires; the «vā pana» question keeps «တစ်ဖန်»); ^6-2-44 split line (the structure rule: one
  Burmese line per Pāli line); ^6-1-99 «nāmahetū ti» and ^6-2-111 nirujjhattha (spelling only: the intended word,
  already so).
- 7 **kept**: heading layout (^6-6-65 «4 (င) နေရာအလိုက် အငြင်းပြ ပုံစံ» and ^6-8-82 «(14) ကာလ ကျော်လွန်ပြီးခြင်း
  ဖော်ပြချက်» stay in the body line, as the Pāli; ^6-9-4-0 / ^6-9-5-0 keep the digit without a dot).
- 14 **kept** (Burmese needs a head noun; no keyword carries them): «သဘောတရား» after kusalānaṃ / akusalānaṃ /
  kusalākusalānaṃ («ကုသိုလ် သဘောတရားတို့၏ ဖြစ်ခြင်း ခဏ၌»); «အရာ(များ)» after the bare anaññātaññassāmīti and abyākatā;
  «အတွဲ» after saraṇaaraṇā (8-cittayamaka lines 420 and 863, the last pair of the list: «“ပဋိပက္ခ ရှိသော” “ပဋိပက္ခ မရှိသော”
  အတွဲ တိုင်အောင်»); «ပုဂ္ဂိုလ်» after Aṭṭhamako («အဋ္ဌမ ပုဂ္ဂိုလ်» = pi-5); «ထိုသူတို့၏ပင်» (the plural pronoun of
  tesaṃ with yeva «ပင်»).

## Checks (regen_rails.sh, all pass)
- Protected files: 188 md5s unchanged; termbase sha256 = the lock (847e49cd…).
- Reproduction: build without the layer = zero-shot, 44 of 44 files byte-identical.
- check_chapter_ids, check_text_pe (wrapper) and check_marks: all 44 files OK; typography OK.
- Adherence: zero-shot 333 misses (input reproduced) → rails 333, all known INFLECTION rows; GENUINE fixed 0, left 0;
  0 unverified. Line-level: 977 line misses, 0 outside the inflection patterns.
- align_check_my: 659 repeated Pāli sentences, 0 differing (zero-shot 0); align_hidden_my: 0 unmatched;
  align_explained: 0 unexplained.
- pi-1 … pi-5 identity: 10 / 10, 14 / 14, 10 / 332 + 322 explained (answer register), 10 / 10, 2791 / 2791 (as the
  zero-shot; none worse).
- line_scan: 0 lines left (zero-shot 172 flags: 86 L01 × 2 families; 26 of 26 families with Pāli hits).
- Rerun: a second regen_rails.sh run changes no byte.

## Termbase proposals (rails/termbase-proposals.tsv)
None (header only). No phrase entry is stale: the layer's one change («မိမိ စိတ်» → «အကြင်စိတ်») occurs in no termbase
entry (the termbase has no entry for yassa cittassa anantarā; cittassa «စိတ်» and anantarā «ချက်ချင်း နောက်» hold).

## Termbase doubts (termbase not changed)
1. **kāmāvacarānaṃ pacchimacittaṃ** (§A2): the termbase keeps sense 0 «ကာမဘုံနှင့် ဆိုင်သော» (the adjective of
   pacchimacitta) for «anantarā kāmāvacarānaṃ pacchimacittaṃ»; grammatically the genitive plural is «the last mind of
   the kāma beings», as in «Kāmāvacarānaṃ pacchimacittassa uppādakkhaṇe» «ကာမဘုံ၌ ရှိသူတို့၊ …» in the same segments.
   The meaning is the same; kept as decided.
2. **uppajjissanti** gloss «coming into being (verb, present or future)»: the term «ဖြစ်ပေါ်လိမ့်မည်» is the future only,
   right for the text; the gloss could say «3rd pl. future» as nirujjhissanti does (gloss only, no text effect).
3. **§A1 versus harmonise B10**: the rails unify «yassa cittassa anantarā» to «အကြင်စိတ်၏ ချက်ချင်း နောက်၌» (L01); if
   the coordinator prefers the person reading «မိမိ စိတ်၏» for the persons frames, it must then also apply to the
   «… aggamaggaṃ paṭilabhissanti» frames (identical Pāli), i.e. the other 181 places. A Burmese speaker may check
   «အကြင်စိတ်၏ ချက်ချင်း နောက်၌ … ဖြစ်ပေါ်မည့်သူတို့» without a following «ထိုစိတ်၏».
4. **Agent-noun terms** (upapajjantānaṃ, pañcavokārānaṃ, …): 333 of the 333 misses (977 line misses) are the attributive
   or other grammar forms of the agent noun or the future, as APPROVED.md foresees; no text change.
