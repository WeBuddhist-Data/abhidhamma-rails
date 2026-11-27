"""pi-3 Burmese RAILS layer: the systematic termbase differences of the harmonised zero-shot, as in-memory source
patches of my3_formulas.py and of the zero-shot generators (none of them is edited on disk). Model: the approved pi-2
rails layer (pi-2-my/rails/my_formulas_rails.py, read only).

Each patch is (old, new, count, reason): build_rails.py applies it to the source text before running it and fails
unless «old» occurs exactly «count» times. Patching the source (not the finished text) keeps every derived string
(tables, frames, verses) consistent: identical Pāli = identical Burmese.
Reasons would start with the family id (Lnn), then the termbase headword(s) = term and the decision
(AI_translation/burmese/pi-3-pali-burmese-termbase-plain.md, locked; termbase/decisions-A.tsv), or the logged text
inconsistency «H n» (mapper-my/map-harmonise-notes.md, «Text inconsistencies for the rails step», item n).

RESULT OF THE RAILS PASS: the layer is EMPTY (0 patches), because nothing calls for one:
  * adherence on the zero-shot (rails/adherence-zeroshot.txt): 8430 keyword uses checked, 6 misses, none GENUINE
    (classify_misses.py: ādi «စသည့်» INFLECTION; Anuppannā / Anuppannehi «မဖြစ်ပေါ်သေးသော» ×3 and apariyāpannā /
    apariyāpannehi «ဘဝဘုံတို့၌ အကျုံးမဝင်သော» ×2 ARTEFACT privative). The termbase was built from this text's own
    keyword map: of 8442 map values, the 16 that are not a termbase term are the non-chosen candidates of the six
    multi-candidate decisions (fragments / gaps the decisions name: dukkha «နာကျင်» in «မနာကျင်», hetukā dhammā /
    hetukehi dhammehi «အမြစ် … သဘောတရား» under negation, bhavena vippayuttā «ဘဝနှင့် … ကင်းကွာသော» with items between,
    uppannā / uppannehi «ဖြစ်ပေါ်သော» in «မဖြစ်ပေါ်သေးသော»), plus 12 «(no direct equivalent)» keywords without an entry.
  * the four logged text inconsistencies (H1-H4), each checked against the locked termbase (line_scan.py H families):
    H1 maccu / mataṃ = «သေခြင်း»: the text has it at all 4 uses (^3-227, ^3-455 maccurūpaṃ; ^3-318, ^3-518
       jātijarāmataṃ); no «သေဆုံး» / «သေမင်း» anywhere: 0 changes.
    H2 pucchake «ဖော်ပြချက်» (^3-112 variant note «… မေးခွန်းများဖြင့် ဖော်ပြချက်၌လည်း») vs pucchakena «မေးခွန်း»
       (^3-318, ^3-518 «မေးခွန်း အချည်းနှီး»): the text already keeps the two senses: 0 changes.
    H3 «ထိုသဘောတရားတို့နှင့်» (tehi dhammehi, 138 uses in ch5, 6, 8, 10, 11) next to «…သဘောတရားများနှင့်» (the items) and
       «ထိုသဘောတရားများသည်» (te dhammā): no termbase term decides tehi dhammehi (no entry for tehi / tehi dhammehi / te
       dhammā; dhammehi vippayuttā «သဘောတရားများနှင့် ကင်းကွာသော» is the ITEM «X-ehi dhammehi ye dhammā vippayuttā»,
       map-harmonise rule V: «the later tehi dhammehi … does not decide»); the brief allows «တို့» / «များ» changes
       only where a termbase term decides them: kept (0 changes; termbase doubt 1).
    H4 arūpa spacing: the planes (arūpāvacara ×8 segments, Arūpabhava ×6) all have «ရုပ်မရှိသော», the non-material
       (Arūpakkhandhā ^3-352, Arūpino ^3-121, Arūpīhi ^3-217, ^3-453) all «ရုပ် မဟုတ်သော»; no «ရုပ် မရှိသော» and no
       «ရုပ်မဟုတ်သော» anywhere: 0 changes.
A patch added later must follow the format above; build_rails.py logs every applied patch in rails/layer-log.tsv.
"""

# ------------------------------------------------------------------------------------------------- my3_formulas.py
FORMULA_PATCHES = []

# ------------------------------------------------------------------------------------------------- generators
GEN_PATCHES = {
    "make_sample": [],
    "make_ch3-6-8-9": [],
    "make_ch7-10-11": [],
    "make_ch12-15": [],
}
