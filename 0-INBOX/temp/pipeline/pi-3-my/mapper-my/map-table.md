# pi-3 Burmese keyword mapping: rules and review table (Dhātukathā «ဓာတ်များအကြောင်း ဆွေးနွေးခြင်း», SAMPLE: preamble, 1-uddeso, 2-pathamanayo)

Written by map_all.py. Burmese from the FINAL pi-3 text of this track only (AI_translation/burmese/pi-3-burmese-plain-zeroshot_split_chapters); pi-1 / pi-2 values from AI_translation/burmese/pi-1- and pi-2-keywords-by-reference-pali-burmese-plain.md. No other Burmese source.

## Verification

| chapter | lines | keyword preservation | presence failures | comma / ၊ / « / » | rule-matched chunks | (no direct equivalent) |
|---|---|---|---|---|---|---|
| preamble | 3 | bad [] | 0 | [] | 1 | 0 |
| 1-uddeso | 11 | bad [] | 0 | [] | 3 | 1 |
| 2-pathamanayo | 173 | bad [] | 0 | [] | 252 | 1 |

## Reuse of pi-1 / pi-2

- Keyword uses: 2614; distinct keywords: 419.
- Keywords that pi-1 or pi-2 also has: 321 distinct; their values taken **unchanged from pi-1 / pi-2**: 316 distinct keyword-value pairs, 1003 uses (a pi-2 value: 261 pairs, 916 uses; a pi-1 value only: 55 pairs, 87 uses).
- Keywords new in pi-3 (in neither mapping): 98 distinct.

### Values that differ from pi-1 / pi-2 for the same keyword

| keyword | pi-3 value (uses) | pi-2 value(s) | pi-1 value(s) | reason |
|---|---|---|---|---|
| aññāta | သိရသော (2) | - | သိသော (3) | pi-1 «သိသော» is not in the segment: the text renders anaññāta «မသိရသေးသည်ကို», positive part «သိရ» + «သော» (rule 8, M7) |
| Bahiddhā dhammā | မိမိ၏ ပြင်ပ၌ ရှိသော သဘောတရား (1) | - | သူတစ်ပါး၌ ရှိသော သဘောတရား (1) | pi-1 «သူတစ်ပါး၌ …» does not occur: the pi-3 text has the pi-2 term «မိမိ၏ ပြင်ပ၌ ရှိသော» (pi-2 N10) |
| bodhi | ဗောဇ္ဈင် (2) | ဗောဓိ (2) | - | pi-2 «ဗောဓိ» is not in the segment: the text renders bojjhaṅgā by the one word «ဗောဇ္ဈင်» (aṅgā = no direct equivalent) |
| dukkha | နာကျင် (1) | ဒုက္ခ (136) · ဆင်းရဲ (7) · ခက်ခဲသော (7) · နာကျင်သော (3) | ခက်ခဲသော (77) · နာကျင်သော (6) · နာကျင်မှု (5) · ဒုက္ခ (4) | fragment of adukkhamasukhāya: the positive part of the text's «မနာကျင်» (rule 8); one sense per segment |
| dukkhaṃ | ကိုယ်ဆင်းရဲခြင်း (1) | နာကျင်မှု (17) · ဒုက္ခ (15) · နာကျင်သော (1) | နာကျင်မှု (7) | the jāti list (soko … dukkhaṃ … upāyāso): the pi-3 text's word «ကိုယ်ဆင်းရဲခြင်း» (my3 terms, pi-2 ^2-206 rails); pi-2 «နာကျင်မှု / ဒုက္ခ» are not in the segment |
| hetukā dhammā | အမြစ် … သဘောတရား (2) | - | အမြစ် ရှိသော သဘောတရား (3) | negated pahātabbahetukā («…အမြစ် ရှိသည် မဟုတ်သော သဘောတရား»): the pi-1 phrase is not in the text, gap (M4); the positive segments keep pi-1 |
| nayo | ခွဲနည်း (1) | - | နည်း (4) | the pi-3 text's one word «ခွဲနည်း» (M8); pi-1 «နည်း» stands alone in its text |
| saṅgaha | အကျုံးဝင်ခြင်း (2) | အကျဉ်းချုပ် (2) | - | the method «inclusion» (text «အကျုံးဝင်ခြင်း»); pi-2 «အကျဉ်းချုပ်» is «summary» |
| saṅgaho | အကျုံးဝင်ခြင်း (2) | - | စုစည်းခြင်း (22) | the method «inclusion» (text «အကျုံးဝင်ခြင်း»); pi-1 «စုစည်းခြင်း» is the compendium (Rūpasaṅgaho) |
| vippayogo | ကင်းကွာခြင်း (2) | ကွေကွင်းရခြင်း (2) | - | the method «dissociation» (text «ကင်းကွာခြင်း»); pi-2 «ကွေကွင်းရခြင်း» is separation from the loved |
| āyatanena | အာရုံခံ နယ်ပယ် (55) | (no direct equivalent) (9) | - | the counted noun «အာရုံခံ နယ်ပယ် N-ပါး» (ekenāyatanena); pi-2 (no direct equivalent) is a compound member inside one Burmese word |

## Rules

The value is the word or phrase of THAT segment's Burmese (the FINAL pi-3 text) that carries the keyword, in the
dictionary form of the approved pi-1 and pi-2 Burmese mappings. **Binding and unchanged:** pi-1 `map-table.md`
rules 1–11 (approved sample), the agreed later pi-1 rules (`map-table-2-01 … -5.md`, `map-harmonise-notes.md`:
absolutives keep «…၍»; «samaye X» = «အချိန်၌ ရှိသော X» (none here); relative pronouns = (no direct equivalent)
where the Burmese builds the clause with «ရှိသော / ရှိသမျှ» (none here); one sense per segment; no « / »
alternatives; caya = (no direct equivalent) where apacaya is one word (none here)) and pi-2's approved rules N1–N11
and harmonise decisions (compound members inside one Burmese word = (no direct equivalent); the ONE presence check).
pi-2 and pi-1 values are reused for the same keyword where they occur in the pi-3 segment: the script looks every
keyword not in its own table up in the final pi-2 mapping, then pi-1 (a value the text has as a phrase first; for
«X dhammā» keywords only such a phrase).

Rules this sample uses that pi-1 / pi-2 already had, applied to the Dhātukathā's shapes:

- **Nouns** (pi-1 rule 1): no case particle, no plural at the end: khandhehi / khandhena = အစုအဝေး, āyatanehi /
  āyatanena = အာရုံခံ နယ်ပယ်, dhātūhi / dhātuyā = ဓာတ် (text «… တို့တွင်», «… မည်မျှတို့တွင်»); saṅkhārā =
  ပြုပြင်ဖန်တီးမှု (text «…မှုများ»); sabbā = အားလုံး (text «အားလုံးသည်လည်း»). Verbal nouns keep «ခြင်း»: saṅgaho =
  အကျုံးဝင်ခြင်း, asaṅgaho = အကျုံးမဝင်ခြင်း, vippayogo = ကင်းကွာခြင်း; saṅgahāsaṅgaha keeps its inner «နှင့်».
- **Participles** (pi-1 rule 3; pi-2 saṅgahitaṃ = အကျုံးဝင်သော): the predicate saṅgahito / -ā / -aṃ / -āni =
  အကျုံးဝင်သော, asaṅgahito / -ā / -aṃ / -āni = အကျုံးမဝင်သော, whatever the text's ending (statement «…သည်။»,
  plural «…ကြသည်», negative answer «…မဝင်။», question «…သနည်း», «where» clause «…ရာ»); in the Uddesa
  sampayuttaṃ / vippayuttaṃ / asaṅgahitaṃ = ယှဉ်တွဲသော / ကင်းကွာသော / အကျုံးမဝင်သော: the text's «…သည့်အရာ» (N11)
  supplies the head noun «အရာ», which is not the keyword (rule 3). asaṅkhataṃ = ပြုပြင်ဖန်တီးထားခြင်း မရှိသော (pi-2;
  the text's head «သဘောတရား» is not the keyword).
- **Numerals** (pi-1 harmonise decision 5): the text's count with its classifier: ekādasa = ဆယ့်တစ်ပါး, dasa =
  ဆယ်ပါး, dvādasa = ဆယ့်နှစ်ပါး (pi-1 / pi-2), aṭṭhārasa = ဆယ့်ရှစ်ပါး, bāvīsati = နှစ်ဆယ့်နှစ်ပါး, and every
  instrumental count (sattarasahi = ဆယ့်ခုနစ်ပါး …); a counted noun keeps its count (rule 1): ekādasahāyatanehi =
  အာရုံခံ နယ်ပယ် ဆယ့်တစ်ပါး, sattarasahi dhātūhi = ဓာတ် ဆယ့်ခုနစ်ပါး, aṭṭhārasa dhātuyo = ဓာတ် ဆယ့်ရှစ်ပါး (pi-2).
- **«X dhammā»** (pi-1 rule 5): the qualifier + « သဘောတရား»; «na / no X» = the text's «…သည် မဟုတ်သော» (na sahagatā
  dhammā = အတူ ဖြစ်သည် မဟုတ်သော သဘောတရား). Mātikā items keep the pi-1 / pi-2 values (Rūpino = ရုပ် ဖြစ်သော, hetukā
  = အမြစ် (rule 2), raṇā = ပဋိပက္ခ, avacarā = ဘုံနှင့် ဆိုင်သော …).
- **Subject + predicate pairs** (pi-1 5 rule 21, pi-2 «khandhā siyā»): the biterms of the frame «X saṅgahito /
  -ā / -aṃ / -āni» = X … အကျုံးဝင်သော (Rūpakkhandho … saṅgahito: «ရုပ် အစုအဝေးသည် … အကျုံးဝင်သည်»; khandhā
  saṅgahitā = အစုအဝေး … အကျုံးဝင်သော; dhammā saṅgahitā = သဘောတရား … အကျုံးဝင်သော; Aṭṭhārasa dhātuyo saṅgahitā =
  ဓာတ် ဆယ့်ရှစ်ပါး … အကျုံးဝင်သော); «asaṅkhataṃ ṭhapetvā» = ပြုပြင်ဖန်တီးထားခြင်း မရှိသော … ချန်ထား၍ (absolutive
  «၍» kept, pi-1 harmonise decision 1).
- **Fragments** (pi-1 rule 8): the positive part of a negated word: aññāta (anaññāta) = သိရသော, dukkha in
  adukkhamasukhāya = နာကျင် (the text builds the pair «မနာကျင် မသာယာသော» with one «သော», so the fragment keeps the
  text's form, pi-1 rule 3), uppannā in anuppannā = ဖြစ်ပေါ်သော (pi-1: no «ပြီး» in the text), paṭighā in
  (a)ppaṭighā = ထိခိုက်မှု (rule 2), pariyāpannā (apariyāpannā) = ဘဝဘုံတို့၌ အကျုံးဝင်သော (pi-2 Mātikā value).
- **Verbs** (pi-1 rule 4): ñassāmi (anaññātaññassāmītindriya) = သိရတော့သည် (text future «သိရတော့မည်», pi-2 N12
  ending «မည်»); namo = ရှိခိုးသည်.
- **Compound members inside one Burmese word** (pi-2 harmonise decision 4): bojjhaṅga «ဗောဇ္ဈင်»: bodhi = ဗောဇ္ဈင်,
  aṅgā = (no direct equivalent) (pi-2 ^2-522 aṅgo); upaṭṭhānā / upaṭṭhānaṃ (satipaṭṭhāna) = ပဋ္ဌာန် and pādā
  (iddhipāda) = ပါဒ် (the pi-2 values); kāma in kāmabhavo / kāmāvacarā = ကာမ (inside «ကာမဘုံ»).
- **Sense by context, one sense per segment** (pi-1 harmonise decision 3): rūpa by the first rūpa compound of the
  Pāli segment (rūpakkhandha «ရုပ်»; rūpāyatana / rūpadhātu «အဆင်းအရောင်»; rūpāvacara and now rūpabhava
  «သိမ်မွေ့သော ရုပ်», text «သိမ်မွေ့သော ရုပ်ဘုံ၌ ဖြစ်သော ဘဝ»); the same for dukkha (dukkhasacca «ဒုက္ခ»,
  dukkhindriya «နာကျင်မှု», dukkhāya vedanāya «နာကျင်သော», adukkhamasukha «နာကျင်») and sukha (sukhindriya /
  sukhasahagata «သာယာမှု», sukhāya vedanāya «သာယာသော»); sammā = အပြည့်အဝ in the homage (pi-1 / pi-2 preamble),
  မှန်ကန်သော in sammappadhāna (pi-1 / pi-2); bahiddhā = မိမိ၏ ပြင်ပ၌ (pi-2 N10).
- **Titles and headings** (pi-1 rule 7, decision 4): Dhātukathā / dhātukathāya = ဓာတ်များအကြောင်း ဆွေးနွေးခြင်း (the
  approved title whole; the dative's «၏» goes), its members kathā = ဆွေးနွေးခြင်း, dhātu = ဓာတ်; dhammasaṅgaṇī =
  သဘောတရားများကို စုစည်းရေတွက်ခြင်း, saṅgaṇī, dhamma (pi-1 [1-0]); Uddeso = အကျဉ်း ဖော်ပြချက် (pi-1); mātikā =
  ခေါင်းစဉ်စာရင်း; niddeso = အကျယ် ဖော်ပြချက်; paṭicca / samuppāda / ādi (pi-2); the mātikā names naya, abbhantara,
  nayamukha, lakkhaṇa, bāhira = the heading's own words.

## NEW rules (for the user's review)

M1. **The count biterms of the frame** «āyatanehi N» (from «…āyatanehi N-hi dhātūhi») = «အာရုံခံ နယ်ပယ် …
    N-ပါး»: the āyatana noun of the compound before and the count that belongs to the dhātus after; the gap holds
    the āyatana count and «ဓာတ်» (text «အာရုံခံ နယ်ပယ် ဆယ့်တစ်ပါး၊ ဓာတ် ဆယ့်ခုနစ်ပါး»). The pair «N dhātūhi» is
    contiguous in Burmese order: «ဓာတ် N-ပါး».
M2. **«A / B» keywords** (the extractor's pair of two Pāli words: āyatanāni / pādā, vitakka / vicārā, vitakkā /
    vicārā, vitakka / vicāra, aññā / aññātāvī, kāma / āyatanehi) = «A … B», both members in text order (no « / »
    alternatives allowed in a value): vitakka / vicārā = စတင်ကြံစည်မှု … ဆက်လက်သုံးသပ်မှု.
M3. **khandhato** (in «asaṅkhataṃ khandhato ṭhapetvā») = «အစုအဝေး ရေတွက်ရာ»: the text says «from the count of the
    aggregates» («အစုအဝေး ရေတွက်ရာမှ»); only the ablative «မှ» goes (rule 1), «ရေတွက်ရာ» carries the ablative's
    meaning here (the aggregates as a class counted), like pi-2 N9 kenaci = «တစ်စုံတစ်ခုသော စိတ်».
M4. **«X dhammā» with a gap** (pi-1 rule 10 applied by the script): where the head noun does not follow the
    qualifier in the text, « … » marks the gap: the fragments hetukā dhammā in the negated «na … pahātabbahetukā»
    («…အမြစ် ရှိသည် မဟုတ်သော သဘောတရား») = အမြစ် … သဘောတရား, avitakka dhammā (avitakkavicāramattā, avitakkaavicārā)
    = စတင်ကြံစည်မှု မရှိသော … သဘောတရား, savitakka dhammā (savitakkasavicārā) = စတင်ကြံစည်မှု ရှိသော … သဘောတရား,
    saṃsaṭṭha dhammā (cittasaṃsaṭṭhasamuṭṭhānā) = ရောနှောသော … သဘောတရား, no saṃsaṭṭha dhammā = ရောနှောသော …
    မဟုတ်သော သဘောတရား. Where the text has the pi-1 / pi-2 «X dhammā» value as a phrase, that value is used.
M5. **The colophon members**: Ekamūlakaṃ = «တစ်မျိုးတွဲကို အခြေခံသော» (pi-2 N8 mūlakaṃ «အခြေခံသော», the head
    «ခွဲနည်း» is not the keyword); eka (its member) = «တစ်မျိုးတွဲ», as pi-2 duka / tika / catukka = «နှစ်မျိုးတွဲ /
    သုံးမျိုးတွဲ / လေးမျိုးတွဲ» for the members of Dukamūlakaṃ … (eka is not ekena: the counts are «တစ်ပါး»).
    Dvādasakaṃ / Aṭṭhārasakaṃ (none keywords here) would be «ဆယ့်နှစ်မျိုးတွဲ / ဆယ့်ရှစ်မျိုးတွဲ».
M6. **The Lakkhaṇamātikā**: visabhāgo = «ကွဲပြားသော သဘော» (a noun, the whole noun phrase of the text, rule 1);
    bhāga (the member of sabhāga / visabhāga) = «သဘော».
M7. **Presence check, three more endings for «Xသော»** (ATTR_FROM): «သနည်း» (the question «အကျုံးမဝင်သနည်း»),
    «ရာ» (the «where» clause «အကျုံးမဝင်ရာ … မရှိ») and «သေးသည်» (aññāta in «မသိရသေးသည်ကို», as pi-1's «သေးသော»).
    pi-2 accepts «သနည်း» and «ရာ» for «Xသည်» already (12-14 M1); a participle in a question / «where» clause is
    the same normalisation (rule 3). All other endings are pi-2's merged list, unchanged.
M8. **nayo / naya** = «ခွဲနည်း» (one word in the pi-3 text and the pi-1 rails text, my3-zeroshot-terms), not pi-1's
    «နည်း» (a separate word in its text: «ဈာန် လေးပါး နည်း»).
M9. **vokāra** (in eka- / catu- / pañcavokārabhavo «အစုအဝေး N-ပါး ရှိသော ဘဝ») = «အစုအဝေး»; **pucchake** (in the
    variant note «vibha. dukapañhāpucchakepi» = «… နှစ်မျိုးတွဲ မေးခွန်းများဖြင့် ဖော်ပြချက်၌လည်း») = «ဖော်ပြချက်»,
    pañhā = «မေးခွန်း» (pi-2): the note is translated, so its words have a Burmese equivalent (pi-1's (no direct
    equivalent) is for Pāli kept in Roman script inside a variant bracket).

## Presence: chunks matched by an ending rule (not literally in the segment)

Every other chunk of every value occurs literally in its segment's Burmese.

| segment | keyword | chunk | rule |
|---|---|---|---|
| T-1 | namo | ရှိခိုးသည် | verb |
| 3-1 | sampayuttaṃ | ယှဉ်တွဲသော | attr |
| 3-1 | vippayuttaṃ | ကင်းကွာသော | attr |
| 3-1 | asaṅgahitaṃ | အကျုံးမဝင်သော | attr |
| 3-6 | asaṅgahito | အကျုံးမဝင်သော | attr |
| 3-7 | asaṅgahito | အကျုံးမဝင်သော | attr |
| 3-8 | asaṅgahito | အကျုံးမဝင်သော | attr |
| 3-9 | asaṅgahito | အကျုံးမဝင်သော | attr |
| 3-9 | saṅkhāra saṅgahito | အကျုံးဝင်သော | attr |
| 3-10 | viññāṇa saṅgahito | အကျုံးဝင်သော | attr |
| 3-10 | asaṅgahito | အကျုံးမဝင်သော | attr |
| 3-11 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-12 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-13 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-14 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-15 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-16 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-17 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-18 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-18 | saṅkhāra saṅgahitā | အကျုံးဝင်သော | attr |
| 3-19 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-20 | viññāṇa saṅgahitā | အကျုံးဝင်သော | attr |
| 3-20 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-21 | khandhā saṅgahitā | အကျုံးဝင်သော | attr |
| 3-21 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-22 | āyatanaṃ saṅgahitaṃ | အကျုံးဝင်သော | attr |
| 3-22 | asaṅgahitaṃ | အကျုံးမဝင်သော | attr |
| 3-22 | Cakkhāyatanaṃ saṅgahitaṃ | အကျုံးဝင်သော | attr |
| 3-23 | asaṅgahitaṃ | အကျုံးမဝင်သော | attr |
| 3-24 | asaṅgahitaṃ | အကျုံးမဝင်သော | attr |
| 3-25 | asaṅgahitaṃ | အကျုံးမဝင်သော | attr |
| 3-26 | āyatanaṃ saṅgahitā | အကျုံးဝင်သော | attr |
| 3-26 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-27 | āyatanaṃ saṅgahitā | အကျုံးဝင်သော | attr |
| 3-27 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-28 | āyatanaṃ saṅgahitā | အကျုံးဝင်သော | attr |
| 3-28 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-29 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-30 | āyatanāni saṅgahitā | အကျုံးဝင်သော | attr |
| 3-30 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-31 | dhātu saṅgahitā | အကျုံးဝင်သော | attr |
| 3-31 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-31 | Cakkhudhātu saṅgahitā | အကျုံးဝင်သော | attr |
| 3-32 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-33 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-34 | dhātu saṅgahitā | အကျုံးဝင်သော | attr |
| 3-34 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-35 | dhātu saṅgahitā | အကျုံးဝင်သော | attr |
| 3-35 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-36 | dhātu saṅgahitā | အကျုံးဝင်သော | attr |
| 3-36 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-37 | dhātu saṅgahitā | အကျုံးဝင်သော | attr |
| 3-37 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-38 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-39 | Aṭṭhārasa dhātuyo saṅgahitā | အကျုံးဝင်သော | attr |
| 3-39 | dhātuyo saṅgahitā | အကျုံးဝင်သော | attr |
| 3-39 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-40 | asaṅgahitaṃ | အကျုံးမဝင်သော | attr |
| 3-41 | asaṅgahitaṃ | အကျုံးမဝင်သော | attr |
| 3-42 | asaṅgahitaṃ | အကျုံးမဝင်သော | attr |
| 3-43 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-44 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-45 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-46 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-47 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-48 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-49 | asaṅgahitāni | အကျုံးမဝင်သော | attr |
| 3-50 | asaṅgahitaṃ | အကျုံးမဝင်သော | attr |
| 3-50 | Cakkhundriyaṃ saṅgahitaṃ | အကျုံးဝင်သော | attr |
| 3-51 | asaṅgahitaṃ | အကျုံးမဝင်သော | attr |
| 3-52 | asaṅgahitaṃ | အကျုံးမဝင်သော | attr |
| 3-53 | asaṅgahitaṃ | အကျုံးမဝင်သော | attr |
| 3-54 | asaṅgahitaṃ | အကျုံးမဝင်သော | attr |
| 3-54 | ñassāmi | သိရတော့သည် | verb |
| 3-54 | aññāta | သိရသော | attr |
| 3-55 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-56 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-57 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-58 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-59 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-59 | ñassāmi | သိရတော့သည် | verb |
| 3-59 | aññāta | သိရသော | attr |
| 3-60 | asaṅgahitāni | အကျုံးမဝင်သော | attr |
| 3-61 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-62 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-63 | asaṅgahitaṃ | အကျုံးမဝင်သော | attr |
| 3-64 | asaṅgahitaṃ | အကျုံးမဝင်သော | attr |
| 3-65 | asaṅgahitaṃ | အကျုံးမဝင်သော | attr |
| 3-66 | asaṅgahito | အကျုံးမဝင်သော | attr |
| 3-67 | asaṅgahito | အကျုံးမဝင်သော | attr |
| 3-68 | asaṅgahito | အကျုံးမဝင်သော | attr |
| 3-69 | asaṅgahito | အကျုံးမဝင်သော | attr |
| 3-70 | asaṅgahito | အကျုံးမဝင်သော | attr |
| 3-71 | asaṅgahitaṃ | အကျုံးမဝင်သော | attr |
| 3-72 | asaṅgahitaṃ | အကျုံးမဝင်သော | attr |
| 3-73 | asaṅgahito | အကျုံးမဝင်သော | attr |
| 3-74 | asaṅgahitaṃ | အကျုံးမဝင်သော | attr |
| 3-75 | asaṅgahito | အကျုံးမဝင်သော | attr |
| 3-76 | asaṅgahitaṃ | အကျုံးမဝင်သော | attr |
| 3-77 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-77 | dhammā saṅgahitā | အကျုံးဝင်သော | attr |
| 3-77 | akusalā dhammā saṅgahitā | အကျုံးဝင်သော | attr |
| 3-78 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-79 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-80 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-81 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-82 | saṃkiliṭṭha | ညစ်နွမ်းသော | attr |
| 3-82 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-83 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-84 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-84 | upādinna | ဖြစ်သော | attr |
| 3-85 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-86 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-86 | upādinna | ဖြစ်သော | attr |
| 3-86 | asaṃkiliṭṭha | မညစ်နွမ်းသော | attr |
| 3-87 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-88 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-89 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-89 | avitakka dhammā | မရှိသော | attr |
| 3-90 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-91 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-92 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-93 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-93 | dhammā saṅgahitā | အကျုံးဝင်သော | attr |
| 3-94 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-94 | gāmino dhammā | ဦးတည်သော | attr |
| 3-95 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-95 | dhammā saṅgahitā | အကျုံးဝင်သော | attr |
| 3-96 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-96 | dhammā saṅgahitā | အကျုံးဝင်သော | attr |
| 3-97 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-97 | paritta | ရှိသော | attr |
| 3-98 | mahaggata | ကြီးမြတ်သော | attr |
| 3-98 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-98 | appamāṇa | မရှိသော | attr |
| 3-99 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-99 | dhammā saṅgahitā | အကျုံးဝင်သော | attr |
| 3-100 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-101 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-101 | dhammā saṅgahitā | အကျုံးဝင်သော | attr |
| 3-102 | uppannā | ဖြစ်ပေါ်သော | attr |
| 3-102 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-103 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-104 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-105 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-105 | dhammā saṅgahitā | အကျုံးဝင်သော | attr |
| 3-106 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-107 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-108 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-108 | paṭighā saṅgahitā | အကျုံးဝင်သော | attr |
| 3-108 | sanidassana | မြင်နိုင်သော | attr |
| 3-109 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-109 | paṭighā saṅgahitā | အကျုံးဝင်သော | attr |
| 3-110 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-110 | paṭighā saṅgahitā | အကျုံးဝင်သော | attr |
| 3-110 | anidassana | မမြင်နိုင်သော | attr |
| 3-111 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-112 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-113 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-114 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-114 | dhammā saṅgahitā | အကျုံးဝင်သော | attr |
| 3-115 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-115 | dhammā saṅgahitā | အကျုံးဝင်သော | attr |
| 3-116 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-116 | dhammā saṅgahitā | အကျုံးဝင်သော | attr |
| 3-117 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-117 | dhammā saṅgahitā | အကျုံးဝင်သော | attr |
| 3-118 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-118 | paṭighā saṅgahitā | အကျုံးဝင်သော | attr |
| 3-119 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-119 | paṭighā saṅgahitā | အကျုံးဝင်သော | attr |
| 3-120 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-120 | dhammā saṅgahitā | အကျုံးဝင်သော | attr |
| 3-121 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-121 | dhammā saṅgahitā | အကျုံးဝင်သော | attr |
| 3-122 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-122 | dhammā saṅgahitā | အကျုံးဝင်သော | attr |
| 3-123 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-124 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-125 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-126 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-127 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-128 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-129 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-130 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-131 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-132 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-133 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-134 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-135 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-136 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-137 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-137 | Cittā saṅgahitā | အကျုံးဝင်သော | attr |
| 3-138 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-138 | cittā saṅgahitā | အကျုံးဝင်သော | attr |
| 3-139 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-139 | citta saṅgahitā | အကျုံးဝင်သော | attr |
| 3-140 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-141 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-141 | citta saṅgahitā | အကျုံးဝင်သော | attr |
| 3-142 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-142 | citta saṅgahitā | အကျုံးဝင်သော | attr |
| 3-143 | anuparivattino | လိုက်ပါသော | attr |
| 3-143 | cittānuparivattino | လိုက်ပါသော | attr |
| 3-143 | samuṭṭhānā | ဖြစ်ပေါ်လာသော | attr |
| 3-143 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-143 | sahabhuno | တည်ရှိသော | attr |
| 3-143 | citta saṅgahitā | အကျုံးဝင်သော | attr |
| 3-144 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-144 | citta saṅgahitā | အကျုံးဝင်သော | attr |
| 3-145 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-145 | saṃsaṭṭha | ရောနှောသော | attr |
| 3-145 | citta saṅgahitā | အကျုံးဝင်သော | attr |
| 3-145 | saṃsaṭṭha dhammā | ရောနှောသော | attr |
| 3-146 | anuparivattino | လိုက်ပါသော | attr |
| 3-146 | citta anuparivattino | လိုက်ပါသော | attr |
| 3-146 | samuṭṭhānā | ဖြစ်ပေါ်လာသော | attr |
| 3-146 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-146 | sahabhuno | တည်ရှိသော | attr |
| 3-146 | saṃsaṭṭha | ရောနှောသော | attr |
| 3-146 | citta saṅgahitā | အကျုံးဝင်သော | attr |
| 3-146 | no saṃsaṭṭha dhammā | ရောနှောသော | attr |
| 3-147 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-147 | dhammā saṅgahitā | အကျုံးဝင်သော | attr |
| 3-148 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-148 | dhammā saṅgahitā | အကျုံးဝင်သော | attr |
| 3-149 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-149 | dhammā saṅgahitā | အကျုံးဝင်သော | attr |
| 3-150 | upādā | ဖြစ်သော | attr |
| 3-150 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-151 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-152 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-153 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-154 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-155 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-156 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-157 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-158 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-159 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-160 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-161 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-162 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-163 | sahagatā | ဖြစ်သော | attr |
| 3-163 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-164 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-165 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-166 | sahagatā | ဖြစ်သော | attr |
| 3-166 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-167 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-168 | pariyāpannā | အကျုံးဝင်သော | attr |
| 3-168 | kāmāvacarā | ဆိုင်သော | attr |
| 3-168 | avacarā | ဆိုင်သော | attr |
| 3-168 | dhammā saṅgahitā | အကျုံးဝင်သော | attr |
| 3-169 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-170 | asaṅgahitā | အကျုံးမဝင်သော | attr |
| 3-170 | avacarā | ဆိုင်သော | attr |

## Keyword → Burmese (uses)

«pi-2» / «pi-1» = the value is a pi-2 / pi-1 value of the same keyword. Several values = the keyword reads differently by context.

| Pāli keyword | Burmese (uses) |
|---|---|
| abbhantara | အတွင်း (1) |
| abhidhamma | အဘိဓမ္မာ (1, pi-2) |
| Abhidhammapiṭake | အဘိဓမ္မာပိဋက (1, pi-2) |
| Abyākatā | ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော (1, pi-2) |
| adhipatino | အကြီးအမှူး (1, pi-1) |
| Ajjhattikā | အတွင်းပိုင်း (1, pi-2) |
| Ajjhattikā dhammā | အတွင်းပိုင်း သဘောတရား (1, pi-1) |
| akusalā | အကုသိုလ် (1, pi-2) |
| akusalā dhammā | အကုသိုလ် သဘောတရား (1, pi-2) |
| akusalā dhammā saṅgahitā | အကုသိုလ် သဘောတရား … အကျုံးဝင်သော (1) |
| anidassana | မမြင်နိုင်သော (2, pi-2) |
| Anidassanā | မမြင်နိုင်သော (1, pi-2) |
| anuparivattino | နောက်သို့ လိုက်ပါသော (4, pi-1) |
| anuparivattino dhammā | နောက်သို့ လိုက်ပါသော သဘောတရား (1, pi-1) |
| anuttarā | ထိုထက် သာလွန်သည် မရှိသော (1, pi-2) |
| anuttarā dhammā | ထိုထက် သာလွန်သည် မရှိသော သဘောတရား (1, pi-1) |
| Anāsavā | စိတ်အစွန်းအထင်း၏ အာရုံ မဖြစ်နိုင်သော (1, pi-2) |
| Anāsavā dhammā | စိတ်အစွန်းအထင်း၏ အာရုံ မဖြစ်နိုင်သော သဘောတရား (1, pi-1) |
| apacaya | လျော့ပါးခြင်း (2, pi-2) |
| Appamaññā | အပ္ပမညာ (1, pi-2) |
| appamaññāyo | အပ္ပမညာ (1, pi-2) |
| appamāṇa | အတိုင်းအဆ မရှိသော (1, pi-1) |
| Appamāṇā | အတိုင်းအဆ မရှိသော (1, pi-2) |
| Appamāṇā dhammā | အတိုင်းအဆ မရှိသော သဘောတရား (1, pi-1) |
| arahato | ရဟန္တာ (1, pi-2) |
| ariyo | အရိယာ (2, pi-2) |
| arūpa | ရုပ်မရှိသော (3, pi-2) |
| Arūpino | ရုပ် မဟုတ်သော (1, pi-2) |
| Arūpino dhammā | ရုပ် မဟုတ်သော သဘောတရား (1, pi-1) |
| asaṃkiliṭṭha | ကိလေသာဖြင့် မညစ်နွမ်းသော (2, pi-2) |
| asaṃkiliṭṭhā | ကိလေသာဖြင့် မညစ်နွမ်းသော (1, pi-2) |
| asaṅgaha | အကျုံးမဝင်ခြင်း (2) |
| asaṅgahitaṃ | အကျုံးမဝင်သော (20) |
| asaṅgahito | အကျုံးမဝင်သော (12) |
| asaṅgahitā | အကျုံးမဝင်သော (132) |
| asaṅgahitāni | အကျုံးမဝင်သော (2) |
| asaṅgaho | အကျုံးမဝင်ခြင်း (2) |
| asaṅkhataṃ | ပြုပြင်ဖန်တီးထားခြင်း မရှိသော (46, pi-2) |
| asaṅkhataṃ ṭhapetvā | ပြုပြင်ဖန်တီးထားခြင်း မရှိသော … ချန်ထား၍ (46) |
| asaṅkhatā | ပြုပြင်ဖန်တီးထားခြင်း မရှိသော (1, pi-2) |
| asaṅkhatā dhammā | ပြုပြင်ဖန်တီးထားခြင်း မရှိသော သဘောတရား (1, pi-1) |
| asekkhā | ကျင့်ကြံမှု ပြီးဆုံးသူ၏ (2, pi-2) |
| avacarā | ဘုံနှင့် ဆိုင်သော (4, pi-1) |
| Avijjā | အမှန်ကို မသိမှု (1, pi-2) |
| avijjā | အမှန်ကို မသိမှု (1, pi-2) |
| avitakka dhammā | စတင်ကြံစည်မှု မရှိသော … သဘောတရား (2) |
| Avitakkā dhammā | စတင်ကြံစည်မှု မရှိသော သဘောတရား (1, pi-1) |
| aññā / aññātāvī | အပြည့်အဝ သိမြင်ခြင်း … အပြည့်အဝ သိမြင်ပြီးသူ (2) |
| aññāta | သိရသော (2) |
| aṅgā | (no direct equivalent) (2, pi-2) |
| aṭṭhaṅgiko | အင်္ဂါ ရှစ်ပါး ရှိသော (2, pi-2) |
| Aṭṭhārasa | ဆယ့်ရှစ်ပါး (1, pi-2) |
| aṭṭhārasa | ဆယ့်ရှစ်ပါး (1, pi-2) |
| Aṭṭhārasa dhātuyo | ဓာတ် ဆယ့်ရှစ်ပါး (1, pi-2) |
| aṭṭhārasa dhātuyo | ဓာတ် ဆယ့်ရှစ်ပါး (1, pi-2) |
| Aṭṭhārasa dhātuyo saṅgahitā | ဓာတ် ဆယ့်ရှစ်ပါး … အကျုံးဝင်သော (1) |
| aṭṭhārasahi | ဆယ့်ရှစ်ပါး (40) |
| aṭṭhārasahi dhātūhi | ဓာတ် ဆယ့်ရှစ်ပါး (40) |
| Bahiddhā | မိမိ၏ ပြင်ပ၌ (1, pi-2) |
| bahiddhā | မိမိ၏ ပြင်ပ၌ (2, pi-2) |
| Bahiddhā dhammā | မိမိ၏ ပြင်ပ၌ ရှိသော သဘောတရား (1) |
| balāni | စွမ်းအား (2, pi-2) |
| bhagavato | မြတ်စွာဘုရား (1, pi-2) |
| bhavo | ဘဝ (5, pi-2) |
| bhāga | သဘော (1) |
| bhāvanāya pahātabbā | ဘာဝနာ ပွားများခြင်းဖြင့် ပယ်ရမည့် (3, pi-1) |
| bodhi | ဗောဇ္ဈင် (2) |
| bāhira | ပြင်ပ (1) |
| Bāhiramātikā | ပြင်ပ ခေါင်းစဉ်စာရင်း (1) |
| Bāhirā | ပြင်ပ (1, pi-2) |
| Bāhirā dhammā | ပြင်ပ သဘောတရား (1, pi-1) |
| bāvīsati | နှစ်ဆယ့်နှစ်ပါး (2) |
| cakkhu | မျက်စိ (17, pi-2) |
| Cakkhudhātu | မျက်စိ ဓာတ် (6, pi-2) |
| Cakkhudhātu saṅgahitā | မျက်စိ ဓာတ် … အကျုံးဝင်သော (1) |
| Cakkhundriyaṃ | မျက်စိ၏ စွမ်းရည် (6, pi-2) |
| Cakkhundriyaṃ saṅgahitaṃ | မျက်စိ၏ စွမ်းရည် … အကျုံးဝင်သော (1) |
| cakkhuviññāṇa | မျက်စိ သိစိတ် (2, pi-2) |
| cakkhuviññāṇadhātu | မျက်စိ သိစိတ် ဓာတ် (2, pi-2) |
| Cakkhāyatanaṃ | မျက်စိ အာရုံခံ နယ်ပယ် (5, pi-2) |
| Cakkhāyatanaṃ saṅgahitaṃ | မျက်စိ အာရုံခံ နယ်ပယ် … အကျုံးဝင်သော (1) |
| catukka | လေးမျိုးတွဲ (1, pi-2) |
| cetanā | စေ့ဆော်မှု (2, pi-2) |
| Cetasikā | စိတ်၏ အဖော် (1, pi-2) |
| cetasikā | စိတ်၏ အဖော် (1, pi-2) |
| citta | စိတ် (7, pi-2) |
| citta anuparivattino | စိတ်နောက်သို့ လိုက်ပါသော (2) |
| citta saṅgahitā | စိတ် … အကျုံးဝင်သော (7) |
| Cittaṃ | စိတ် (1, pi-2) |
| cittaṃ | စိတ် (1, pi-2) |
| Cittā | စိတ် (1, pi-2) |
| cittā | စိတ် (1, pi-2) |
| Cittā saṅgahitā | စိတ် … အကျုံးဝင်သော (1) |
| cittā saṅgahitā | စိတ် … အကျုံးဝင်သော (1) |
| cittānuparivattino | စိတ်နောက်သို့ လိုက်ပါသော (2, pi-1) |
| cittānuparivattino dhammā | စိတ်နောက်သို့ လိုက်ပါသော သဘောတရား (1, pi-1) |
| dasa | ဆယ်ပါး (54, pi-2) |
| dasahi | ဆယ်ပါး (4) |
| dasahi dhātūhi | ဓာတ် ဆယ်ပါး (15) |
| dasahāyatanehi | အာရုံခံ နယ်ပယ် ဆယ်ပါး (54) |
| Dassanena | သစ္စာကို မြင်ခြင်း (2, pi-2) |
| dassanena | သစ္စာကို မြင်ခြင်း (2, pi-2) |
| dhamma | သဘောတရား (5, pi-2) |
| dhammasaṅgaṇī | သဘောတရားများကို စုစည်းရေတွက်ခြင်း (1, pi-1) |
| dhammā saṅgahitā | သဘောတရား … အကျုံးဝင်သော (19) |
| Dhātu | ဓာတ် (1, pi-2) |
| dhātu | ဓာတ် (10, pi-2) |
| dhātu saṅgahitā | ဓာတ် … အကျုံးဝင်သော (5) |
| Dhātukathā | ဓာတ်များအကြောင်း ဆွေးနွေးခြင်း (1) |
| dhātukathāya | ဓာတ်များအကြောင်း ဆွေးနွေးခြင်း (1) |
| dhātuyo | ဓာတ် (1, pi-2) |
| dhātuyo saṅgahitā | ဓာတ် … အကျုံးဝင်သော (1) |
| dhātuyā | ဓာတ် (36, pi-2) |
| dhātūhi | ဓာတ် (165) |
| domanassa | စိတ်ဆင်းရဲမှု (2, pi-2) |
| domanassaṃ | စိတ်ဆင်းရဲမှု (1, pi-2) |
| duka | နှစ်မျိုးတွဲ (5, pi-2) |
| dukkha | ဒုက္ခ (7, pi-2) · နာကျင်မှု (2, pi-2) · နာကျင် (1) |
| Dukkhasaccaṃ | ဒုက္ခ သစ္စာ (7, pi-2) |
| dukkhaṃ | ကိုယ်ဆင်းရဲခြင်း (1) |
| dukkhāya | နာကျင်သော (1, pi-2) |
| dvādasa | ဆယ့်နှစ်ပါး (46, pi-2) |
| dvādasahi | ဆယ့်နှစ်ပါး (4) |
| dvādasahi dhātūhi | ဓာတ် ဆယ့်နှစ်ပါး (4) |
| dvādasahāyatanehi | အာရုံခံ နယ်ပယ် ဆယ့်နှစ်ပါး (43) |
| dvādasāyatanehi | အာရုံခံ နယ်ပယ် ဆယ့်နှစ်ပါး (1) |
| Dvādasāyatanāni | အာရုံခံ နယ်ပယ် ဆယ့်နှစ်ပါး (1, pi-2) |
| dvādasāyatanāni | အာရုံခံ နယ်ပယ် ဆယ့်နှစ်ပါး (1, pi-2) |
| eka | တစ်မျိုးတွဲ (5) |
| Ekamūlakaṃ | တစ်မျိုးတွဲကို အခြေခံသော (5) |
| ekādasa | ဆယ့်တစ်ပါး (55, pi-2) |
| ekādasahi | ဆယ့်တစ်ပါး (3) |
| ekādasahi dhātūhi | ဓာတ် ဆယ့်တစ်ပါး (21) |
| ekādasahāyatanehi | အာရုံခံ နယ်ပယ် ဆယ့်တစ်ပါး (55) |
| gandha | အနံ့ (4, pi-2) |
| gandhadhātu | အနံ့ ဓာတ် (2, pi-2) |
| gandhāyatanaṃ | အနံ့ အာရုံခံ နယ်ပယ် (2, pi-2) |
| ganthā | အထုံး (1, pi-2) |
| ghāna | နှာခေါင်း (6, pi-2) |
| ghānadhātu | နှာခေါင်း ဓာတ် (2, pi-2) |
| ghānaviññāṇa | နှာခေါင်း သိစိတ် (2, pi-2) |
| ghānaviññāṇadhātu | နှာခေါင်း သိစိတ် ဓာတ် (2, pi-2) |
| ghānāyatanaṃ | နှာခေါင်း အာရုံခံ နယ်ပယ် (2, pi-2) |
| gāmino dhammā | ဦးတည်သော သဘောတရား (2, pi-1) |
| hetukā | အမြစ် (6, pi-2) |
| hetukā dhammā | အမြစ် ရှိသော သဘောတရား (2, pi-1) · အမြစ် … သဘောတရား (2) |
| Hetū | အမြစ် (1, pi-2) |
| hetū | အမြစ် (1, pi-2) |
| hīnā | ယုတ်ညံ့သော (1, pi-2) |
| hīnā dhammā | ယုတ်ညံ့သော သဘောတရား (1, pi-1) |
| iddhi | ဣဒ္ဓိ (2, pi-2) |
| Indriyaṃ | စွမ်းရည် (1, pi-2) |
| indriyaṃ | စွမ်းရည် (10, pi-2) |
| indriyāni | စွမ်းရည် (3, pi-2) |
| itthi | မိန်းမ (2, pi-2) |
| jarā | အိုခြင်း (1, pi-2) |
| Jhānaṃ | ဈာန် (1, pi-2) |
| jhānāni | ဈာန် (1, pi-2) |
| jivhā | လျှာ (6, pi-2) |
| jivhādhātu | လျှာ ဓာတ် (2, pi-2) |
| jivhāviññāṇa | လျှာ သိစိတ် (2, pi-2) |
| jivhāviññāṇadhātu | လျှာ သိစိတ် ဓာတ် (2, pi-2) |
| jivhāyatanaṃ | လျှာ အာရုံခံ နယ်ပယ် (2, pi-2) |
| Jāti | မွေးဖွားခြင်း (1, pi-2) |
| jīvita | အသက် (2, pi-1) |
| kathā | ဆွေးနွေးခြင်း (2) |
| khandhato | အစုအဝေး ရေတွက်ရာ (46) |
| khandhehi | အစုအဝေး (165) |
| khandhena | အစုအဝေး (59) |
| Khandho | အစုအဝေး (1, pi-2) |
| khandho | အစုအဝေး (15, pi-2) |
| khandhā | အစုအဝေး (1, pi-2) |
| khandhā saṅgahitā | အစုအဝေး … အကျုံးဝင်သော (1) |
| kilesa | ကိလေသာ (2, pi-2) |
| kilesā | ကိလေသာ (3, pi-2) |
| Kusalā | ကုသိုလ် (1, pi-2) |
| Kusalā dhammā | ကုသိုလ် သဘောတရား (1, pi-2) |
| kāma | ကာမ (1, pi-2) |
| kāma / āyatanehi | ကာမ … အာရုံခံ နယ်ပယ် (3) |
| kāmāvacarā | ကာမဘုံနှင့် ဆိုင်သော (2, pi-2) |
| kāya | ကိုယ် (6, pi-2) |
| kāyadhātu | ကိုယ် ဓာတ် (2, pi-2) |
| kāyaviññāṇa | ကိုယ် သိစိတ် (2, pi-2) |
| kāyaviññāṇadhātu | ကိုယ် သိစိတ် ဓာတ် (2, pi-2) |
| kāyāyatanaṃ | ကိုယ် အာရုံခံ နယ်ပယ် (2, pi-2) |
| lakkhaṇa | လက္ခဏာ (1) |
| Lokiyā | လောကနှင့် သက်ဆိုင်သော (1, pi-2) |
| Lokiyā dhammā | လောကနှင့် သက်ဆိုင်သော သဘောတရား (1, pi-1) |
| Lokuttarā | လောကကို ကျော်လွန်သော (1, pi-2) |
| magga | မဂ် (5, pi-2) |
| maggo | မဂ် (2, pi-2) |
| mahaggata | ကြီးမြတ်သော (1, pi-1) |
| mahaggatā | ကြီးမြတ်သော (1, pi-2) |
| mahaggatā dhammā | ကြီးမြတ်သော သဘောတရား (1, pi-1) |
| Majjhimā | အလယ်အလတ် (1, pi-2) |
| Majjhimā dhammā | အလယ်အလတ် သဘောတရား (1, pi-1) |
| mana | မနော (4, pi-1) |
| manasikāro | နှလုံးသွင်းခြင်း (2, pi-2) |
| mano | မနော (2, pi-2) |
| manodhātu | မနော ဓာတ် (2, pi-2) |
| manoviññāṇa | မနော သိစိတ် (2, pi-2) |
| manoviññāṇadhātu | မနော သိစိတ် ဓာတ် (2, pi-2) |
| Manāyatanaṃ | မနော အာရုံခံ နယ်ပယ် (1, pi-2) |
| manāyatanaṃ | မနော အာရုံခံ နယ်ပယ် (1, pi-2) |
| maraṇaṃ | သေခြင်း (1, pi-2) |
| micchatta | မှားယွင်းမှု (1, pi-2) |
| mātikā | ခေါင်းစဉ်စာရင်း (6, pi-2) |
| na sahagatā dhammā | အတူ ဖြစ်သည် မဟုတ်သော သဘောတရား (2) |
| namo | ရှိခိုးသည် (1, pi-2) |
| naya | ခွဲနည်း (1) |
| nayamukha | ခွဲနည်း၏ တံခါးဝ (1) |
| nayo | ခွဲနည်း (1) |
| niddeso | အကျယ် ဖော်ပြချက် (2, pi-2) |
| nirodha | ချုပ်ငြိမ်းခြင်း (4, pi-2) |
| niyatā | ကျိန်းသေသော (4, pi-2) |
| niyatā dhammā | ကျိန်းသေသော သဘောတရား (2, pi-1) |
| niyyānikā dhammā | လွတ်မြောက်ရာသို့ ပို့ဆောင်သော သဘောတရား (1, pi-1) |
| no saṃsaṭṭha dhammā | ရောနှောသော … မဟုတ်သော သဘောတရား (1) |
| nāmarūpa | စိတ်ပိုင်းနှင့် ရုပ်ပိုင်း (1, pi-2) |
| nāmarūpaṃ | စိတ်ပိုင်းနှင့် ရုပ်ပိုင်း (1, pi-2) |
| nāsaññā | မှတ်သိမှု မရှိသည် မဟုတ်သော (1, pi-1) |
| nīvaraṇā | အတားအဆီး (1, pi-2) |
| oghā | ရေအလျဉ် (1, pi-2) |
| paccayā | ကြောင့် (5, pi-2) |
| padhānaṃ | ကြိုးပမ်းအားထုတ်ခြင်း (1, pi-2) |
| padhānā | ကြိုးပမ်းအားထုတ်ခြင်း (1, pi-2) |
| pahātabbā | ပယ်ရမည့် (4, pi-2) |
| pannarasahi | ဆယ့်ငါးပါး (5) |
| pannarasahi dhātūhi | ဓာတ် ဆယ့်ငါးပါး (5) |
| paridevo | ငိုကြွေးခြင်း (1, pi-2) |
| paritta | အကန့်အသတ် ရှိသော (1, pi-2) |
| Parittā | အကန့်အသတ် ရှိသော (1, pi-2) |
| Parittā dhammā | အကန့်အသတ် ရှိသော သဘောတရား (1, pi-1) |
| pariyāpannā | ဘဝဘုံတို့၌ အကျုံးဝင်သော (2) |
| Parāmaṭṭhā | မှားယွင်းသော ယူဆမှု၏ အာရုံ ဖြစ်နိုင်သော (1, pi-2) |
| parāmaṭṭhā | မှားယွင်းသော ယူဆမှု၏ အာရုံ ဖြစ်နိုင်သော (2, pi-2) |
| Parāmaṭṭhā dhammā | မှားယွင်းသော ယူဆမှု၏ အာရုံ ဖြစ်နိုင်သော သဘောတရား (1, pi-1) |
| parāmāsa | မှားယွင်းသော ယူဆမှု (4, pi-2) |
| parāmāsā | မှားယွင်းသော ယူဆမှု (3, pi-2) |
| pañhā | မေးခွန်း (1, pi-2) |
| paññā | ပညာ (2, pi-2) |
| paṇītā | မွန်မြတ်သော (1, pi-2) |
| paṇītā dhammā | မွန်မြတ်သော သဘောတရား (1, pi-1) |
| paṭicca | အကြောင်းတို့ကို မှီ၍ (2, pi-2) |
| paṭighā saṅgahitā | ထိခိုက်မှု … အကျုံးဝင်သော (5) |
| phasso | တွေ့ထိမှု (3, pi-2) |
| phoṭṭhabba | အထိအတွေ့ (4, pi-2) |
| phoṭṭhabbadhātu | အထိအတွေ့ ဓာတ် (2, pi-2) |
| phoṭṭhabbāyatanaṃ | အထိအတွေ့ အာရုံခံ နယ်ပယ် (2, pi-2) |
| pucchake | ဖော်ပြချက် (1) |
| purisa | ယောက်ျား (2, pi-2) |
| pīti | ပီတိ (3, pi-2) |
| rasa | အရသာ (4, pi-2) |
| rasadhātu | အရသာ ဓာတ် (2, pi-2) |
| rasāyatanaṃ | အရသာ အာရုံခံ နယ်ပယ် (2, pi-2) |
| raṇā | ပဋိပက္ခ (2, pi-1) |
| rūpa | ရုပ် (11, pi-2) · အဆင်းအရောင် (4, pi-2) · သိမ်မွေ့သော ရုပ် (3, pi-2) |
| rūpadhātu | အဆင်းအရောင် ဓာတ် (2, pi-2) |
| Rūpakkhandho | ရုပ် အစုအဝေး (11, pi-2) |
| Rūpino | ရုပ် ဖြစ်သော (1, pi-1) |
| Rūpino dhammā | ရုပ် ဖြစ်သော သဘောတရား (1, pi-1) |
| rūpāyatanaṃ | အဆင်းအရောင် အာရုံခံ နယ်ပယ် (2, pi-2) |
| sabbā | အားလုံး (1) |
| Saccaṃ | သစ္စာ (1, pi-2) |
| saccaṃ | သစ္စာ (9, pi-2) |
| saccāni | သစ္စာ (2, pi-2) |
| sadda | အသံ (4, pi-2) |
| saddadhātu | အသံ ဓာတ် (2, pi-2) |
| saddhā | ယုံကြည်မှု (2, pi-2) |
| saddāyatanaṃ | အသံ အာရုံခံ နယ်ပယ် (2, pi-2) |
| sahabhuno | အတူ တည်ရှိသော (4, pi-2) |
| sahabhuno dhammā | အတူ တည်ရှိသော သဘောတရား (1) |
| sahagatā | အတူ ဖြစ်သော (8, pi-2) |
| sahagatā dhammā | အတူ ဖြစ်သော သဘောတရား (6, pi-1) |
| sambuddha | အမှန်ကို ကိုယ်တိုင် … သိမြင်တော်မူသော ဘုရားရှင် (1) |
| sammatta | မှန်ကန်မှု (1, pi-2) |
| sammā | မှန်ကန်သော (2, pi-2) · အပြည့်အဝ (1, pi-2) |
| sammāsambuddhassa | အမှန်ကို ကိုယ်တိုင် အပြည့်အဝ သိမြင်တော်မူသော ဘုရားရှင် (1, pi-2) |
| sampayuttaṃ | ယှဉ်တွဲသော (1, pi-2) |
| sampayuttā | ယှဉ်တွဲသော (10, pi-2) |
| samudaya | ဖြစ်ပေါ်ခြင်း (5, pi-2) |
| samuppāda | ဖြစ်ပေါ်ပုံ (1, pi-2) |
| samuppādo | ဖြစ်ပေါ်ပုံ (1) |
| samuṭṭhānā | ဖြစ်ပေါ်လာသော (4, pi-2) |
| samuṭṭhānā dhammā | ဖြစ်ပေါ်လာသော သဘောတရား (1, pi-1) |
| samādhi | သမာဓိ (2, pi-2) |
| sanidassana | မြင်နိုင်သော (1, pi-2) |
| Sanidassanā | မြင်နိုင်သော (1, pi-2) |
| Sanidassanā dhammā | မြင်နိုင်သော သဘောတရား (1, pi-1) |
| Sappītikā dhammā | ပီတိ ရှိသော သဘောတရား (1, pi-1) |
| saraṇā dhammā | ပဋိပက္ခ ရှိသော သဘောတရား (1, pi-1) |
| sati | သတိ (4, pi-2) |
| sattarasahi | ဆယ့်ခုနစ်ပါး (39) |
| sattarasahi dhātūhi | ဓာတ် ဆယ့်ခုနစ်ပါး (39) |
| sauttarā | ထိုထက် သာလွန်သည် ရှိသေးသော (1, pi-2) |
| savicārā dhammā | ဆက်လက်သုံးသပ်မှု ရှိသော သဘောတရား (1, pi-1) |
| savitakka dhammā | စတင်ကြံစည်မှု ရှိသော … သဘောတရား (1) |
| Savitakkā dhammā | စတင်ကြံစည်မှု ရှိသော သဘောတရား (1, pi-1) |
| saññā | မှတ်သိမှု (11, pi-2) |
| Saññākkhandho | မှတ်သိမှု အစုအဝေး (1, pi-2) |
| saññākkhandho | မှတ်သိမှု အစုအဝေး (5, pi-2) |
| Saṃkilesikā | ကိလေသာ၏ အာရုံ ဖြစ်နိုင်သော (1, pi-2) |
| saṃkilesikā | ကိလေသာ၏ အာရုံ ဖြစ်နိုင်သော (5, pi-2) |
| Saṃkilesikā dhammā | ကိလေသာ၏ အာရုံ ဖြစ်နိုင်သော သဘောတရား (1, pi-1) |
| saṃkilesikā dhammā | ကိလေသာ၏ အာရုံ ဖြစ်နိုင်သော သဘောတရား (1, pi-1) |
| saṃkiliṭṭha | ကိလေသာဖြင့် ညစ်နွမ်းသော (1, pi-2) |
| Saṃkiliṭṭhā | ကိလေသာဖြင့် ညစ်နွမ်းသော (1, pi-2) |
| saṃkiliṭṭhā | ကိလေသာဖြင့် ညစ်နွမ်းသော (1, pi-2) |
| Saṃkiliṭṭhā dhammā | ကိလေသာဖြင့် ညစ်နွမ်းသော သဘောတရား (1, pi-1) |
| saṃsaṭṭha | ရောနှောသော (2, pi-2) |
| saṃsaṭṭha dhammā | ရောနှောသော … သဘောတရား (1) |
| saṃsaṭṭhā | ရောနှောသော (2, pi-2) |
| saṃsaṭṭhā dhammā | ရောနှောသော သဘောတရား (1, pi-1) |
| Saṃyojanā | နှောင်ကြိုး (1, pi-2) |
| saṅgaha | အကျုံးဝင်ခြင်း (2) |
| saṅgaho | အကျုံးဝင်ခြင်း (2) |
| saṅgaho asaṅgaho | အကျုံးဝင်ခြင်း အကျုံးမဝင်ခြင်း (1) |
| saṅgahāsaṅgaha | အကျုံးဝင်ခြင်းနှင့် အကျုံးမဝင်ခြင်း (2) |
| saṅgaṇī | စုစည်းရေတွက်ခြင်း (1, pi-1) |
| saṅkhatā | ပြုပြင်ဖန်တီးထားသော (1, pi-2) |
| saṅkhāra | ပြုပြင်ဖန်တီးမှု (6, pi-2) |
| saṅkhāra saṅgahito | ပြုပြင်ဖန်တီးမှု … အကျုံးဝင်သော (1) |
| saṅkhāra saṅgahitā | ပြုပြင်ဖန်တီးမှု … အကျုံးဝင်သော (1) |
| Saṅkhārakkhandho | ပြုပြင်ဖန်တီးမှု အစုအဝေး (1, pi-2) |
| saṅkhārakkhandho | ပြုပြင်ဖန်တီးမှု အစုအဝေး (4, pi-2) |
| saṅkhārā | ပြုပြင်ဖန်တီးမှု (1, pi-2) |
| sekkha | ကျင့်ကြံဆဲသူ၏ (1, pi-2) |
| sekkhā | ကျင့်ကြံဆဲသူ၏ (1, pi-2) |
| Soko | စိုးရိမ်ခြင်း (1, pi-2) |
| somanassa | ဝမ်းမြောက်မှု (2, pi-2) |
| sota | နား (6, pi-2) |
| Sotadhātu | နား ဓာတ် (1, pi-2) |
| sotadhātu | နား ဓာတ် (1, pi-2) |
| sotaviññāṇa | နား သိစိတ် (2, pi-2) |
| sotaviññāṇadhātu | နား သိစိတ် ဓာတ် (2, pi-2) |
| Sotāyatanaṃ | နား အာရုံခံ နယ်ပယ် (1, pi-2) |
| sotāyatanaṃ | နား အာရုံခံ နယ်ပယ် (1, pi-2) |
| soḷasahi | ဆယ့်ခြောက်ပါး (35) |
| soḷasahi dhātūhi | ဓာတ် ဆယ့်ခြောက်ပါး (35) |
| sukha | သာယာမှု (5, pi-2) |
| Sukhāya | သာယာသော (1, pi-2) |
| sukhāya | သာယာသော (1, pi-2) |
| Sāsavā dhammā | စိတ်အစွန်းအထင်း၏ အာရုံ ဖြစ်နိုင်သော သဘောတရား (1, pi-1) |
| sāsavā dhammā | စိတ်အစွန်းအထင်း၏ အာရုံ ဖြစ်နိုင်သော သဘောတရား (1, pi-1) |
| taṇhā | တပ်မက်မှု (1, pi-2) |
| terasahi | ဆယ့်သုံးပါး (3) |
| terasahi dhātūhi | ဓာတ် ဆယ့်သုံးပါး (3) |
| tika | သုံးမျိုးတွဲ (2, pi-2) |
| Uddeso | အကျဉ်း ဖော်ပြချက် (1, pi-1) |
| upapatti | ပြန်လည် ဖြစ်ပေါ်ခြင်း (1, pi-2) |
| upaṭṭhānaṃ | ပဋ္ဌာန် (1) |
| upaṭṭhānā | ပဋ္ဌာန် (1) |
| upekkhā | ဥပေက္ခာ (5, pi-2) |
| Uppannā | ဖြစ်ပေါ်ပြီးသော (1, pi-2) |
| uppannā | ဖြစ်ပေါ်သော (1, pi-1) |
| Uppannā dhammā | ဖြစ်ပေါ်ပြီးသော သဘောတရား (1, pi-1) |
| Uppādino | ဖြစ်ပေါ်လာမည့် (1, pi-2) |
| upādinna | ကံကြောင့် ဖြစ်သော (3, pi-2) |
| Upādinnā | ကံကြောင့် ဖြစ်သော (1, pi-2) |
| upādinnā | ကံကြောင့် ဖြစ်သော (1, pi-2) |
| Upādā | မူလဓာတ်ကြီးများကို မှီ၍ ဖြစ်သော (1, pi-2) |
| upādā | မူလဓာတ်ကြီးများကို မှီ၍ ဖြစ်သော (1, pi-2) |
| Upādā dhammā | မူလဓာတ်ကြီးများကို မှီ၍ ဖြစ်သော သဘောတရား (1, pi-1) |
| upādānaṃ | စွဲလမ်းမှု (1, pi-2) |
| upādāniyā | စွဲလမ်းမှု၏ အာရုံ ဖြစ်နိုင်သော (3, pi-2) |
| Upādānā | စွဲလမ်းမှု (1, pi-2) |
| upāyāso | ပြင်းစွာ ပူပန်ခြင်း (1, pi-2) |
| vedanā | ခံစားမှု (11, pi-2) |
| Vedanākkhandho | ခံစားမှု အစုအဝေး (1, pi-2) |
| vedanākkhandho | ခံစားမှု အစုအဝေး (7, pi-2) |
| vedanāya | ခံစားမှု (2, pi-2) |
| vicāra | ဆက်လက်သုံးသပ်မှု (1, pi-2) |
| vicārā | ဆက်လက်သုံးသပ်မှု (4, pi-2) |
| vippayogo | ကင်းကွာခြင်း (2) |
| vippayuttaṃ | ကင်းကွာသော (1, pi-2) |
| vippayuttā | ကင်းကွာသော (11, pi-2) |
| vippayuttā dhammā | ကင်းကွာသော သဘောတရား (11, pi-1) |
| visabhāgo | ကွဲပြားသော သဘော (1) |
| visaṃsaṭṭhā dhammā | မရောနှောသော သဘောတရား (1, pi-1) |
| vitakka | စတင်ကြံစည်မှု (3, pi-2) |
| vitakka / vicāra | စတင်ကြံစည်မှု … ဆက်လက်သုံးသပ်မှု (1) |
| vitakka / vicārā | စတင်ကြံစည်မှု … ဆက်လက်သုံးသပ်မှု (2) |
| vitakkā | စတင်ကြံစည်မှု (2, pi-2) |
| vitakkā / vicārā | စတင်ကြံစည်မှု … ဆက်လက်သုံးသပ်မှု (2) |
| viññeyyā | သိနိုင်သော (1, pi-2) |
| viññāṇa | သိစိတ် (6, pi-2) |
| viññāṇa saṅgahito | သိစိတ် … အကျုံးဝင်သော (1) |
| viññāṇa saṅgahitā | သိစိတ် … အကျုံးဝင်သော (1) |
| Viññāṇakkhandho | သိစိတ် အစုအဝေး (1, pi-2) |
| viññāṇakkhandho | သိစိတ် အစုအဝေး (4, pi-2) |
| viññāṇaṃ | သိစိတ် (1, pi-2) |
| vokāra | အစုအဝေး (3) |
| yogā | ထမ်းပိုး (1, pi-2) |
| ñassāmi | သိရတော့သည် (2) |
| ācaya | စုပုံခြင်း (2, pi-2) |
| ādi | စသည် (1, pi-2) |
| ārammaṇā | အာရုံ (6, pi-2) |
| āsava | စိတ်အစွန်းအထင်း (1, pi-2) |
| Āsavā | စိတ်အစွန်းအထင်း (1, pi-2) |
| āsavā | စိတ်အစွန်းအထင်း (3, pi-2) |
| āyatana | အာရုံခံ နယ်ပယ် (1, pi-2) |
| Āyatanaṃ | အာရုံခံ နယ်ပယ် (1, pi-2) |
| āyatanaṃ | အာရုံခံ နယ်ပယ် (1, pi-2) |
| āyatanaṃ saṅgahitaṃ | အာရုံခံ နယ်ပယ် … အကျုံးဝင်သော (1) |
| āyatanaṃ saṅgahitā | အာရုံခံ နယ်ပယ် … အကျုံးဝင်သော (3) |
| āyatanehi | အာရုံခံ နယ်ပယ် (163) |
| āyatanehi aṭṭhārasahi | အာရုံခံ နယ်ပယ် … ဆယ့်ရှစ်ပါး (41) |
| āyatanehi dasahi | အာရုံခံ နယ်ပယ် … ဆယ်ပါး (15) |
| āyatanehi dvādasahi | အာရုံခံ နယ်ပယ် … ဆယ့်နှစ်ပါး (4) |
| āyatanehi ekādasahi | အာရုံခံ နယ်ပယ် … ဆယ့်တစ်ပါး (21) |
| āyatanehi pannarasahi | အာရုံခံ နယ်ပယ် … ဆယ့်ငါးပါး (5) |
| āyatanehi sattarasahi | အာရုံခံ နယ်ပယ် … ဆယ့်ခုနစ်ပါး (39) |
| āyatanehi soḷasahi | အာရုံခံ နယ်ပယ် … ဆယ့်ခြောက်ပါး (35) |
| āyatanehi terasahi | အာရုံခံ နယ်ပယ် … ဆယ့်သုံးပါး (3) |
| āyatanena | အာရုံခံ နယ်ပယ် (55) |
| āyatanāni | အာရုံခံ နယ်ပယ် (1, pi-2) |
| āyatanāni / pādā | အာရုံခံ နယ်ပယ် … ပါဒ် (1) |
| āyatanāni saṅgahitā | အာရုံခံ နယ်ပယ် … အကျုံးဝင်သော (1) |
| ṭhapetvā | ချန်ထား၍ (46, pi-2) |
