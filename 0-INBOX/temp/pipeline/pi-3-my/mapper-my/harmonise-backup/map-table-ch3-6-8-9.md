# pi-3 Burmese keyword mapping: rules and review table (Dhātukathā «ဓာတ်များအကြောင်း ဆွေးနွေးခြင်း», chapters 3-dutiyanayo, 4-tatiyanayo, 5-catutthanayo, 6-pancamanayo, 8-sattamanayo, 9-atthamanayo)

Written by map_ch3-6-8-9.py. Burmese from the FINAL pi-3 text of this track only (AI_translation/burmese/pi-3-burmese-plain-zeroshot_split_chapters); pi-1 / pi-2 values from AI_translation/burmese/pi-1- and pi-2-keywords-by-reference-pali-burmese-plain.md. No other Burmese source.

## Verification

| chapter | lines | keyword preservation | presence failures | comma / ၊ / « / » | rule-matched chunks | (no direct equivalent) |
|---|---|---|---|---|---|---|
| 3-dutiyanayo | 10 | bad [] | 0 | [] | 2 | 1 |
| 4-tatiyanayo | 14 | bad [] | 0 | [] | 4 | 1 |
| 5-catutthanayo | 4 | bad [] | 0 | [] | 2 | 1 |
| 6-pancamanayo | 37 | bad [] | 0 | [] | 7 | 1 |
| 8-sattamanayo | 13 | bad [] | 0 | [] | 2 | 0 |
| 9-atthamanayo | 4 | bad [] | 0 | [] | 7 | 0 |

## Reuse of pi-1 / pi-2

- Keyword uses: 1227; distinct keywords: 336.
- Keywords that pi-1 or pi-2 also has: 129 distinct; their values taken **unchanged from pi-1 / pi-2**: 123 distinct keyword-value pairs, 520 uses (a pi-2 value: 112 pairs, 502 uses; a pi-1 value only: 11 pairs, 18 uses).
- Keywords new in pi-3 (in neither mapping): 207 distinct; of their uses, 130 take the pi-1 / pi-2 value of the same word in the nominative (M11).
- Sources of the 1227 values: table 587, pi2 288, compose 208, pi2-case 68, pi1-case 62, pi1 10, ctx 4 (table / ctx = this script's or the approved sample's tables; compose = the compose rules).

### Values that differ from pi-1 / pi-2 for the same keyword

| keyword | pi-3 value (uses) | pi-2 value(s) | pi-1 value(s) | reason |
|---|---|---|---|---|
| antare | ကြားညှပ် (1) | အကြား (1) | - | aparante «နောက် ကြားညှပ်တွင်» = the intermediate dyads: the text's «ကြားညှပ်» (pi-1 antara, M13); pi-2 «အကြား» (between) is not in the segment |
| aññāta | သိရသော (3) | - | သိသော (3) | pi-1 «သိသော» is not in the segment: the text renders anaññāta «မသိရသေးသည်ကို», positive part «သိရ» + «သော» (rule 8, M7) |
| bodhi | ဗောဇ္ဈင် (3) | ဗောဓိ (2) | - | pi-2 «ဗောဓိ» is not in the segment: the text renders bojjhaṅgā by the one word «ဗောဇ္ဈင်» (aṅgā = no direct equivalent) |
| dukkha | နာကျင် (1) | ဒုက္ခ (136) · ဆင်းရဲ (7) · ခက်ခဲသော (7) · နာကျင်သော (3) | ခက်ခဲသော (77) · နာကျင်သော (6) · နာကျင်မှု (5) · ဒုက္ခ (4) | fragment of adukkhamasukhāya: the positive part of the text's «မနာကျင်» (rule 8); one sense per segment |
| maccu | သေခြင်း (1) | သေမင်း (2) | - | the verse's jāti jarā maccu = «မွေးဖွားခြင်း၊ အိုခြင်း၊ သေခြင်း»: the text names death «သေခြင်း»; pi-2 «သေမင်း» (Death personified) is not in the segment |
| nayo | ခွဲနည်း (7) | - | နည်း (4) | the pi-3 text's one word «ခွဲနည်း» (M8); pi-1 «နည်း» stands alone in its text |
| saṅkhārena | ပြုပြင်ဖန်တီးမှု (3) | - | တိုက်တွန်းမှု (12) | avijjāpaccayā saṅkhārena: the text's «ပြုပြင်ဖန်တီးမှု» (pi-2 saṅkhārā); pi-1 «တိုက်တွန်းမှု» is sasaṅkhārena (with prompting), another sense |
| vidhā | မျိုး (1) | နှိုင်းယှဉ် ချိန်ဆမှု (3) | - | tiṃsavidhā «သုံးဆယ်မျိုး» = kinds (pi-1 vidhena = မျိုး); pi-2 «နှိုင်းယှဉ် ချိန်ဆမှု» is vidhā = the discriminations (conceit), another sense |
| āyatanena | အာရုံခံ နယ်ပယ် (26) | (no direct equivalent) (9) | - | the counted noun «အာရုံခံ နယ်ပယ် N-ပါး» (ekenāyatanena); pi-2 (no direct equivalent) is a compound member inside one Burmese word |

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

## Approved sample rules M1–M9 (map-table.md, user 2026-11-18; binding, copied unchanged)

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

## NEW rules in chapters 3, 4, 5, 6, 8, 9 (for the user's review)

M10. **kehici** (in «ekenāyatanena ekāya dhātuyā kehici vippayuttā») = «အချို့»: the text says «…တို့၏ အချို့နှင့်
     ကင်းကွာကြသည်» (dissociated from some of them, i.e. from part of the base and the element). pi-2 N9 kenaci =
     «တစ်စုံတစ်ခုသော စိတ်» is the singular «by some consciousness», another construction, not in these segments.
M11. **Case forms of a pi-1 / pi-2 lemma**: the subjects of the frames stand in the instrumental (Vedanākkhandhena,
     Sanidassanehi dhammehi, saṃkilesikehi, cittānuparivattīhi …), which pi-1 / pi-2 hardly have. They get the pi-2
     (then pi-1) value of the SAME word in the nominative where it occurs in the segment (rule 1: the text's
     «…နှင့်» goes): the script derives the nominative keys (-ehi → -ā / -a / -aṃ / -o, -īhi → -ino / -ī, -ūhi → -ū,
     -ena → -o / -aṃ, -āya → -ā, -iyā → -i, -esu → -ā; dhammehi → dhammā) and applies the usual pi_get (phrase first,
     then literal chunks, then an ending rule). «X dhammehi» = the pi-1 «X dhammā» value where the text has it as a
     phrase, else «X» + « သဘောတရား» (rule 5). Words that neither mapping has in any case (Cakkhāyatanena,
     cakkhudhātuyā, saccena, upāyāsena …) are in the table with the pi-1 / pi-2 value of their members.
M12. **Frame biterms of methods 2–8**: «dhammā asaṅgahitā» = «သဘောတရား … အကျုံးမဝင်သော», «dhammā vippayuttā» =
     «သဘောတရား … ကင်းကွာသော» (the sample's «dhammā saṅgahitā» with the other predicates); «āyatanasaṅgahena
     saṅgahitā» = «အာရုံခံ နယ်ပယ် အကျုံးဝင်ခြင်း … အကျုံးဝင်သော»; khandhasaṅgahena = «အစုအဝေး အကျုံးဝင်ခြင်း»,
     āyatanasaṅgahena = «အာရုံခံ နယ်ပယ် အကျုံးဝင်ခြင်း» (the verbal noun keeps «ခြင်း», the instrumental «ဖြင့်»
     goes, rule 1). Any other two- or three-word keyword of the extractor (dhammehi khandhasaṅgahena, indriyena
     khandhasaṅgahena, paccayā āyatanena) = its members in Pāli order, « … » where they are not adjacent in the
     Burmese (pi-1 rule 10): dhammehi khandhasaṅgahena = «သဘောတရား … အစုအဝေး အကျုံးဝင်ခြင်း».
M13. **Colophon verse words** (the text's own words): gocchaka / gocchakesu / gocchake = «အစု» (the clusters: «အစု
     ဆယ်ပါးတို့တွင်», «အစုတို့၏ ပုဒ်», «အစုတို့တွင်»); upari / Uddhaṃ = «အထက်»; Samatiṃsa = «သုံးဆယ်ပါး အပြည့်»;
     cuddasa = «ဆယ့်လေးပါး»; antarā / antare = «ကြားညှပ်» (pi-1 antara); tathariva = «ထို့အတူ» (pi-2 tathā); vidhā
     (tiṃsavidhā «သုံးဆယ်မျိုး») = «မျိုး» (pi-1 vidhena); manasi (adhimuccanā manasi = manasikāra) = «နှလုံးသွင်းခြင်း»;
     manena yuttā «စိတ်နှင့် ယှဉ်သော»: manena = «စိတ်», yuttā = «ယှဉ်သော»; vicāraṇā = «ဆက်လက်သုံးသပ်မှု»;
     Samucchede = «ပိုင်းဖြတ်ခြင်း»; labbhare = «တွေ့ရသည်» (verb rule 4; the separate na is not a keyword, the text
     «မတွေ့ရကြ» matches by the negative-verb rule, as pi-1 rule 8); mataṃ (jātijarāmataṃ) = «သေခြင်း»; mogha =
     «အချည်းနှီး», pucchakena = «မေးခွန်း» (moghapucchakena «မေးခွန်း အချည်းနှီး ဖြစ်သောကြောင့်»; the sample's
     pucchake = «ဖော်ပြချက်» is the section of the variant note «dukapañhāpucchake»); sattacattālīsa = «လေးဆယ့်ခုနစ်ပါး»,
     sattacattālīsa dhammā = «သဘောတရား လေးဆယ့်ခုနစ်ပါး» (a counted noun keeps its count, as pi-2 aṭṭhārasa dhātuyo);
     3-227 (one segment, CTX): su / buddho (subuddho) = «ကောင်းစွာ» / «နားလည်အပ်သော» (participle, rule 3; text
     «နားလည်အပ်သည်»), maccu = «သေခြင်း» (the text's word, not pi-2 «သေမင်း»), pumaṃ (itthipumaṃ) = «ယောက်ျား».

Applied as before (no new rule): the ordinals pañcama(o) / sattama(o) / aṭṭhama(o) = «ပဉ္စမ / သတ္တမ / အဋ္ဌမ»
(my3-zeroshot-terms); the heading members asaṅgahita / sampayutta / vippayutta = «အကျုံးမဝင်သော / ယှဉ်တွဲသော /
ကင်းကွာသော» (the sample's asaṅgahitaṃ …, text «…သည့်အရာ», N11); the predicates sampayuttā / vippayuttā =
«ယှဉ်တွဲသော / ကင်းကွာသော» (text «…ကြသည်», «…ကြသနည်း»); punareva = (no direct equivalent) (only in the variant
bracket, pi-1 brief); aṅgehi in bojjhaṅgehi = (no direct equivalent) (sample: «ဗောဇ္ဈင်» is one word); sahabhūmi (the
reading Cittasahabhūmi) = «အတူ တည်ရှိသော» (= sahabhū, pi-1 / pi-2); Natthi = «မရှိသည်» (pi-1 / pi-2; text «မရှိ။»);
the fragments of negated words keep the positive part (rule 8): saṃsaṭṭhaṃ in visaṃsaṭṭhaṃ, ārammaṇaṃ in
anārammaṇaṃ, pariyāpannehi in apariyāpannehi, upādinna in anupādinna, kāmāvacarehi after na; one sense per
segment: rūpa in 3-227 = «သိမ်မွေ့သော ရုပ်» (its first rūpa compound is rūpāvacarehi), dukkha in 3-312 = «နာကျင်»
(adukkhamasukhāya), sukha in 3-210 = «သာယာသော» (sukhāya vedanāya first).

## Presence: chunks matched by an ending rule (not literally in the segment)

Every other chunk of every value occurs literally in its segment's Burmese.

| segment | keyword | chunk | rule |
|---|---|---|---|
| 3-3-1-0 | asaṅgahita | အကျုံးမဝင်သော | attr |
| 3-175 | sanidassana | မြင်နိုင်သော | attr |
| 3-4-1-0 | asaṅgahita | အကျုံးမဝင်သော | attr |
| 3-182 | ñassāmi | သိရတော့သည် | verb |
| 3-182 | aññāta | သိရသော | attr |
| 3-190 | asaṅgahita | အကျုံးမဝင်သော | attr |
| 3-192 | ñassāmi | သိရတော့သည် | verb |
| 3-192 | aññāta | သိရသော | attr |
| 3-6-1-0 | asaṅgahita | အကျုံးမဝင်သော | attr |
| 3-200 | ñassāmi | သိရတော့သည် | verb |
| 3-200 | aññāta | သိရသော | attr |
| 3-210 | saṃkiliṭṭha | ညစ်နွမ်းသော | attr |
| 3-210 | asaṃkiliṭṭha | မညစ်နွမ်းသော | attr |
| 3-227 | pariyāpannehi | အကျုံးဝင်သော | attr |
| 3-227 | buddho | နားလည်အပ်သော | attr |
| 3-8-1-0 | sampayutta | ယှဉ်တွဲသော | attr |
| 3-8-1-0 | vippayutta | ကင်းကွာသော | attr |
| 3-9-1-0 | sampayutta | ယှဉ်တွဲသော | attr |
| 3-9-1-0 | vippayutta | ကင်းကွာသော | attr |
| 3-317 | sampayuttā | ယှဉ်တွဲသော | attr |
| 3-317 | Natthi | မရှိသည် | verb |
| 3-318 | sampayuttā | ယှဉ်တွဲသော | attr |
| 3-318 | labbhare | တွေ့ရသည် | verb |
| 3-318 | Natthi | မရှိသည် | verb |

## Keyword → Burmese (uses)

«pi-2» / «pi-1» = the value is a pi-2 / pi-1 value of the same keyword. Several values = the keyword reads differently by context.

| Pāli keyword | Burmese (uses) |
|---|---|
| adhipatīhi | အကြီးအမှူး (1) |
| Ajjhattikehi | အတွင်းပိုင်း (1) |
| Ajjhattikehi dhammehi | အတွင်းပိုင်း သဘောတရား (1) |
| akusalehi | အကုသိုလ် (1, pi-2) |
| akusalehi dhammehi | အကုသိုလ် သဘောတရား (1, pi-2) |
| anidassana | မမြင်နိုင်သော (2, pi-2) |
| Anidassanaṃ | မမြင်နိုင်သော (1, pi-2) |
| antara | ကြားညှပ် (1, pi-1) |
| antare | ကြားညှပ် (1) |
| antarā | ကြားညှပ် (1) |
| anuparivatti | နောက်သို့ လိုက်ပါသော (1, pi-1) |
| anuparivattīhi | နောက်သို့ လိုက်ပါသော (5) |
| anuparivattīhi dhammehi | နောက်သို့ လိုက်ပါသော သဘောတရား (2) |
| anuttarehi | ထိုထက် သာလွန်သည် မရှိသော (1) |
| anuttarehi dhammehi | ထိုထက် သာလွန်သည် မရှိသော သဘောတရား (1) |
| Anāsavehi | စိတ်အစွန်းအထင်း၏ အာရုံ မဖြစ်နိုင်သော (1) |
| Anāsavehi dhammehi | စိတ်အစွန်းအထင်း၏ အာရုံ မဖြစ်နိုင်သော သဘောတရား (1) |
| apacaya | လျော့ပါးခြင်း (1, pi-2) |
| appamaññāya | အပ္ပမညာ (3) |
| appamāṇehi | အတိုင်းအဆ မရှိသော (1) |
| appamāṇehi dhammehi | အတိုင်းအဆ မရှိသော သဘောတရား (1) |
| ariyena | အရိယာ (3) |
| arūpa | ရုပ်မရှိသော (2, pi-2) |
| Arūpīhi | ရုပ် မဟုတ်သော (1) |
| Arūpīhi dhammehi | ရုပ် မဟုတ်သော သဘောတရား (1) |
| asaṃkiliṭṭha | ကိလေသာဖြင့် မညစ်နွမ်းသော (1, pi-2) |
| asaṅgahita | အကျုံးမဝင်သော (4) |
| asaṅgahitā | အကျုံးမဝင်သော (43) |
| asaṅkhataṃ | ပြုပြင်ဖန်တီးထားခြင်း မရှိသော (9, pi-2) |
| asaṅkhataṃ ṭhapetvā | ပြုပြင်ဖန်တီးထားခြင်း မရှိသော … ချန်ထား၍ (9) |
| asaṅkhatehi | ပြုပြင်ဖန်တီးထားခြင်း မရှိသော (2) |
| asaṅkhatehi dhammehi | ပြုပြင်ဖန်တီးထားခြင်း မရှိသော သဘောတရား (2) |
| asekkhehi | ကျင့်ကြံမှု ပြီးဆုံးသူ၏ (1) |
| avacarehi | ဘုံနှင့် ဆိုင်သော (1) |
| Avijjāya | အမှန်ကို မသိမှု (1, pi-1) |
| avijjāya | အမှန်ကို မသိမှု (2, pi-1) |
| avitakka dhammehi | စတင်ကြံစည်မှု မရှိသော … သဘောတရား (1) |
| aññā / aññātāvī | အပြည့်အဝ သိမြင်ခြင်း … အပြည့်အဝ သိမြင်ပြီးသူ (3) |
| aññāta | သိရသော (3) |
| aṅgehi | (no direct equivalent) (3) |
| aṭṭhama | အဋ္ဌမ (1, pi-1) |
| aṭṭhamo | အဋ္ဌမ (1, pi-2) |
| aṭṭhaṅgikena | အင်္ဂါ ရှစ်ပါး ရှိသော (3) |
| bahiddhā | မိမိ၏ ပြင်ပ၌ (1, pi-2) |
| balehi | စွမ်းအား (3) |
| bhavena | ဘဝ (6) |
| bhavo | ဘဝ (1, pi-2) |
| bhāvanāya pahātabbehi | ဘာဝနာ ပွားများခြင်းဖြင့် ပယ်ရမည့် (2) |
| bodhi | ဗောဇ္ဈင် (3) |
| buddho | နားလည်အပ်သော (1) |
| Bāhiraṃ | ပြင်ပ (1, pi-2) |
| bāhirehi | ပြင်ပ (1) |
| bāhirehi dhammehi | ပြင်ပ သဘောတရား (1) |
| cakkhu | မျက်စိ (4, pi-2) |
| cakkhudhātuyā | မျက်စိ ဓာတ် (2) |
| Cakkhundriyena | မျက်စိ၏ စွမ်းရည် (2) |
| cakkhuviññāṇa | မျက်စိ သိစိတ် (3, pi-2) |
| Cakkhuviññāṇadhātuyā | မျက်စိ သိစိတ် ဓာတ် (2) |
| cakkhuviññāṇadhātuyā | မျက်စိ သိစိတ် ဓာတ် (1) |
| Cakkhāyatanena | မျက်စိ အာရုံခံ နယ်ပယ် (2) |
| cetanāya | စေ့ဆော်မှု (4, pi-2) |
| Cetasikehi | စိတ်၏ အဖော် (2) |
| cetasikehi | စိတ်၏ အဖော် (1) |
| citta | စိတ် (3, pi-2) |
| cittasaṃsaṭṭhasamuṭṭhānānuparivattīhi | စိတ်နှင့် ရောနှော၍ စိတ်မှ ဖြစ်ပေါ်လာပြီး စိတ်နောက်သို့ လိုက်ပါသော (3) |
| cittaṃ | စိတ် (1, pi-2) |
| Cittehi | စိတ် (2) |
| cittehi | စိတ် (1) |
| Cittena | စိတ် (1, pi-2) |
| cittena | စိတ် (1, pi-2) |
| cittānuparivattīhi | စိတ်နောက်သို့ လိုက်ပါသော (2) |
| cittānuparivattīhi dhammehi | စိတ်နောက်သို့ လိုက်ပါသော သဘောတရား (2) |
| Cuddasa | ဆယ့်လေးပါး (1) |
| cuddasa | ဆယ့်လေးပါး (1) |
| dasa | ဆယ်ပါး (10, pi-2) |
| dasahi dhātūhi | ဓာတ် ဆယ်ပါး (7) |
| dasahāyatanehi | အာရုံခံ နယ်ပယ် ဆယ်ပါး (8) |
| dasasu | ဆယ်ပါး (1, pi-2) |
| dassanena | သစ္စာကို မြင်ခြင်း (2, pi-2) |
| Dasāyatanā | အာရုံခံ နယ်ပယ် ဆယ်ပါး (1, pi-2) |
| dhamma | သဘောတရား (3, pi-2) |
| dhammehi khandhasaṅgahena | သဘောတရား … အစုအဝေး အကျုံးဝင်ခြင်း (11) |
| dhammā asaṅgahitā | သဘောတရား … အကျုံးမဝင်သော (43) |
| dhammā saṅgahitā | သဘောတရား … အကျုံးဝင်သော (14) |
| dhammā vippayuttā | သဘောတရား … ကင်းကွာသော (11) |
| dhātu | ဓာတ် (58, pi-2) |
| dhātuyā | ဓာတ် (29, pi-2) |
| dhātūhi | ဓာတ် (9) |
| domanassa | စိတ်ဆင်းရဲမှု (3, pi-2) |
| domanassena | စိတ်ဆင်းရဲမှု (2) |
| dukkha | နာကျင်မှု (3, pi-2) · နာကျင် (1) |
| dukkhena | ကိုယ်ဆင်းရဲခြင်း (2) |
| dukkhāya | နာကျင်သော (1, pi-2) |
| dukā | နှစ်မျိုးတွဲ (1) |
| dvādasahi | ဆယ့်နှစ်ပါး (1) |
| dvādasahi dhātūhi | ဓာတ် ဆယ့်နှစ်ပါး (1) |
| ekādasa | ဆယ့်တစ်ပါး (18, pi-2) |
| ekādasahi dhātūhi | ဓာတ် ဆယ့်တစ်ပါး (4) |
| ekādasahāyatanehi | အာရုံခံ နယ်ပယ် ဆယ့်တစ်ပါး (17) |
| ganthehi | အထုံး (3) |
| ghāna | နှာခေါင်း (1, pi-2) |
| ghānaviññāṇa | နှာခေါင်း သိစိတ် (1, pi-2) |
| ghānaviññāṇadhātuyā | နှာခေါင်း သိစိတ် ဓာတ် (1) |
| gocchaka | အစု (1) |
| gocchake | အစု (1) |
| gocchakesu | အစု (1) |
| gāmīhi dhammehi | ဦးတည်သော သဘောတရား (1) |
| hetukehi | အမြစ် (3) |
| hetukehi dhammehi | အမြစ် ရှိသော သဘောတရား (2) |
| Hetūhi | အမြစ် (2) |
| hetūhi | အမြစ် (1) |
| hīnehi | ယုတ်ညံ့သော (1) |
| hīnehi dhammehi | ယုတ်ညံ့သော သဘောတရား (1) |
| iddhi | ဣဒ္ဓိ (1, pi-2) |
| indriyato | စွမ်းရည် (1) |
| indriyehi | စွမ်းရည် (3) |
| indriyena | စွမ်းရည် (10) |
| indriyena khandhasaṅgahena | စွမ်းရည် … အစုအဝေး အကျုံးဝင်ခြင်း (4) |
| indriyā | စွမ်းရည် (1, pi-2) |
| indriyāni | စွမ်းရည် (1, pi-2) |
| itthi | မိန်းမ (5, pi-2) |
| jarā | အိုခြင်း (2, pi-2) |
| jarāya | အိုခြင်း (2) |
| jhānena | ဈာန် (2) |
| jivhā | လျှာ (1, pi-2) |
| jivhāviññāṇa | လျှာ သိစိတ် (1, pi-2) |
| jivhāviññāṇadhātuyā | လျှာ သိစိတ် ဓာတ် (1) |
| jāti | မွေးဖွားခြင်း (2, pi-2) |
| Jātiyā | မွေးဖွားခြင်း (1, pi-2) |
| jātiyā | မွေးဖွားခြင်း (1, pi-2) |
| jīvita | အသက် (2, pi-1) |
| jīvitaṃ | အသက် (2, pi-2) |
| kehici | အချို့ (4) |
| khandha | အစုအဝေး (57, pi-2) |
| khandhato | အစုအဝေး ရေတွက်ရာ (9) |
| khandhehi | အစုအဝေး (14) |
| khandhena | အစုအဝေး (21) |
| kilesa | ကိလေသာ (1, pi-2) |
| kilesehi | ကိလေသာ (3) |
| Kusalehi | ကုသိုလ် (1) |
| Kusalehi dhammehi | ကုသိုလ် သဘောတရား (1) |
| kāma / āyatana | ကာမ … အာရုံခံ နယ်ပယ် (1) |
| kāmāvacarehi | ကာမဘုံနှင့် ဆိုင်သော (1) |
| kāya | ကိုယ် (2, pi-2) |
| kāyaviññāṇa | ကိုယ် သိစိတ် (1, pi-2) |
| kāyaviññāṇadhātuyā | ကိုယ် သိစိတ် ဓာတ် (1) |
| labbhare | တွေ့ရသည် (1) |
| lokuttarehi | လောကကို ကျော်လွန်သော (1) |
| maccu | သေခြင်း (1) |
| magga | မဂ် (4, pi-2) |
| maggena | မဂ် (3) |
| mahaggatehi | ကြီးမြတ်သော (1) |
| mahaggatehi dhammehi | ကြီးမြတ်သော သဘောတရား (1) |
| mana | မနော (3, pi-1) |
| manasi | နှလုံးသွင်းခြင်း (1) |
| manasikārena | နှလုံးသွင်းခြင်း (4) |
| manena | စိတ် (1) |
| mano | မနော (2, pi-2) |
| manodhātuyā | မနော ဓာတ် (3, pi-2) |
| manoviññāṇa | မနော သိစိတ် (3, pi-2) |
| manoviññāṇadhātuyā | မနော သိစိတ် ဓာတ် (3) |
| manāyatanena | မနော အာရုံခံ နယ်ပယ် (2) |
| maraṇena | သေခြင်း (2) |
| mataṃ | သေခြင်း (1) |
| micchatta | မှားယွင်းမှု (1, pi-2) |
| mogha | အချည်းနှီး (1) |
| Natthi | မရှိသည် (2, pi-2) |
| nayo | ခွဲနည်း (7) |
| niddeso | အကျယ် ဖော်ပြချက် (12, pi-2) |
| nirodha | ချုပ်ငြိမ်းခြင်း (2, pi-2) |
| niyatehi | ကျိန်းသေသော (2) |
| niyatehi dhammehi | ကျိန်းသေသော သဘောတရား (2) |
| niyyānikehi dhammehi | လွတ်မြောက်ရာသို့ ပို့ဆောင်သော သဘောတရား (1) |
| nāmarūpa | စိတ်ပိုင်းနှင့် ရုပ်ပိုင်း (1, pi-2) |
| nāmarūpaṃ | စိတ်ပိုင်းနှင့် ရုပ်ပိုင်း (2, pi-2) |
| nāmarūpena | စိတ်ပိုင်းနှင့် ရုပ်ပိုင်း (1) |
| nāsaññā | မှတ်သိမှု မရှိသည် မဟုတ်သော (1, pi-1) |
| nīvaraṇehi | အတားအဆီး (3, pi-2) |
| oghehi | ရေအလျဉ် (3) |
| paccayā | ကြောင့် (8, pi-2) |
| paccayā āyatanena | ကြောင့် … အာရုံခံ နယ်ပယ် (1) |
| padhānena | ကြိုးပမ်းအားထုတ်ခြင်း (3) |
| pahātabbehi | ပယ်ရမည့် (2) |
| pannarasa | ဆယ့်ငါးပါး (1, pi-2) |
| Paridevena | ငိုကြွေးခြင်း (2) |
| paridevena | ငိုကြွေးခြင်း (1) |
| Paridevo | ငိုကြွေးခြင်း (1, pi-2) |
| paritta | အကန့်အသတ် ရှိသော (1, pi-2) |
| pariyāpannehi | ဘဝဘုံတို့၌ အကျုံးဝင်သော (1) |
| parāmaṭṭhehi | မှားယွင်းသော ယူဆမှု၏ အာရုံ ဖြစ်နိုင်သော (3) |
| parāmāsa | မှားယွင်းသော ယူဆမှု (1, pi-2) |
| parāmāsehi | မှားယွင်းသော ယူဆမှု (3) |
| pañcama | ပဉ္စမ (1) |
| pañcamo | ပဉ္စမ (1, pi-2) |
| paññā | ပညာ (3, pi-2) |
| paṇītehi | မွန်မြတ်သော (1) |
| paṇītehi dhammehi | မွန်မြတ်သော သဘောတရား (1) |
| paṭicca | အကြောင်းတို့ကို မှီ၍ (2, pi-2) |
| phassa | တွေ့ထိမှု (1, pi-2) |
| phassena | တွေ့ထိမှု (6) |
| phoṭṭhabba | အထိအတွေ့ (2, pi-2) |
| phoṭṭhabbadhātuyā | အထိအတွေ့ ဓာတ် (2) |
| phoṭṭhabbāyatanena | အထိအတွေ့ အာရုံခံ နယ်ပယ် (2) |
| pucchakena | မေးခွန်း (1) |
| pumaṃ | ယောက်ျား (1) |
| punareva | (no direct equivalent) (1) |
| purisa | ယောက်ျား (4, pi-2) |
| pīti | ပီတိ (2, pi-2) |
| raṇehi | ပဋိပက္ခ (2) |
| rūpa | ရုပ် (2, pi-2) · သိမ်မွေ့သော ရုပ် (1, pi-2) |
| Rūpakkhandhena | ရုပ် အစုအဝေး (2) |
| Rūpaṃ | ရုပ် (1, pi-2) |
| Rūpīhi | ရုပ် ဖြစ်သော (1) |
| Rūpīhi dhammehi | ရုပ် ဖြစ်သော သဘောတရား (1) |
| saccena | သစ္စာ (4) |
| saccā | သစ္စာ (2, pi-2) |
| saddhā | ယုံကြည်မှု (3, pi-2) |
| sahabhu | အတူ တည်ရှိသော (1, pi-2) |
| sahabhūhi | အတူ တည်ရှိသော (4) |
| sahabhūhi dhammehi | အတူ တည်ရှိသော သဘောတရား (1) |
| sahabhūmi | အတူ တည်ရှိသော (1) |
| sahabhūmi dhammehi | အတူ တည်ရှိသော သဘောတရား (1) |
| sahagatehi | အတူ ဖြစ်သော (4) |
| sahagatehi dhammehi | အတူ ဖြစ်သော သဘောတရား (4) |
| sahetukehi | အမြစ် ရှိသော (1) |
| Samatiṃsa | သုံးဆယ်ပါး အပြည့် (1) |
| sammatta | မှန်ကန်မှု (1, pi-2) |
| sammā | မှန်ကန်သော (3, pi-2) |
| sampayutta | ယှဉ်တွဲသော (2, pi-1) |
| sampayuttehi | ယှဉ်တွဲသော (14) |
| sampayuttā | ယှဉ်တွဲသော (13, pi-2) |
| Samucchede | ပိုင်းဖြတ်ခြင်း (1) |
| samudaya | ဖြစ်ပေါ်ခြင်း (3, pi-2) |
| samuṭṭhāna | ဖြစ်ပေါ်လာသော (1, pi-1) |
| samuṭṭhānehi | ဖြစ်ပေါ်လာသော (4) |
| samuṭṭhānehi dhammehi | ဖြစ်ပေါ်လာသော သဘောတရား (1) |
| samādhi | သမာဓိ (3, pi-2) |
| sanidassana | မြင်နိုင်သော (3, pi-2) |
| Sanidassanehi | မြင်နိုင်သော (2) |
| Sanidassanehi dhammehi | မြင်နိုင်သော သဘောတရား (2) |
| sappītikehi dhammehi | ပီတိ ရှိသော သဘောတရား (1) |
| saraṇehi dhammehi | ပဋိပက္ခ ရှိသော သဘောတရား (2) |
| sati | သတိ (5, pi-2) |
| sattacattālīsa | လေးဆယ့်ခုနစ်ပါး (1) |
| sattacattālīsa dhammā | သဘောတရား လေးဆယ့်ခုနစ်ပါး (1) |
| sattama | သတ္တမ (1) |
| sattamo | သတ္တမ (1, pi-2) |
| sattarasahi | ဆယ့်ခုနစ်ပါး (12) |
| sattarasahi dhātūhi | ဓာတ် ဆယ့်ခုနစ်ပါး (12) |
| savicārehi dhammehi | ဆက်လက်သုံးသပ်မှု ရှိသော သဘောတရား (2) |
| savitakka dhammehi | စတင်ကြံစည်မှု ရှိသော … သဘောတရား (2) |
| Savitakkehi dhammehi | စတင်ကြံစည်မှု ရှိသော သဘောတရား (1) |
| savitakkehi dhammehi | စတင်ကြံစည်မှု ရှိသော သဘောတရား (1) |
| saññā | မှတ်သိမှု (8, pi-2) |
| saññākkhandhena | မှတ်သိမှု အစုအဝေး (4) |
| saññāya | မှတ်သိမှု (3, pi-1) |
| saṃkilesikehi | ကိလေသာ၏ အာရုံ ဖြစ်နိုင်သော (5) |
| saṃkiliṭṭha | ကိလေသာဖြင့် ညစ်နွမ်းသော (1, pi-2) |
| saṃkiliṭṭhehi | ကိလေသာဖြင့် ညစ်နွမ်းသော (4) |
| saṃkiliṭṭhehi dhammehi | ကိလေသာဖြင့် ညစ်နွမ်းသော သဘောတရား (1) |
| saṃsaṭṭhaṃ | ရောနှောသော (1, pi-2) |
| saṃsaṭṭhehi | ရောနှောသော (4) |
| saṃsaṭṭhehi dhammehi | ရောနှောသော သဘောတရား (3) |
| Saṃyojanehi | နှောင်ကြိုး (2) |
| saṃyojanehi | နှောင်ကြိုး (1) |
| saṅkhāra | ပြုပြင်ဖန်တီးမှု (6, pi-2) |
| saṅkhārakkhandhena | ပြုပြင်ဖန်တီးမှု အစုအဝေး (4) |
| saṅkhārena | ပြုပြင်ဖန်တီးမှု (3) |
| sekkhehi | ကျင့်ကြံဆဲသူ၏ (1) |
| Sokena | စိုးရိမ်ခြင်း (2) |
| sokena | စိုးရိမ်ခြင်း (1) |
| somanassa | ဝမ်းမြောက်မှု (3, pi-2) |
| sota | နား (1, pi-2) |
| sotaviññāṇa | နား သိစိတ် (1, pi-2) |
| sotaviññāṇadhātuyā | နား သိစိတ် ဓာတ် (1) |
| soḷasa | ဆယ့်ခြောက်ပါး (1, pi-2) |
| soḷasahi | ဆယ့်ခြောက်ပါး (1) |
| soḷasahi dhātūhi | ဓာတ် ဆယ့်ခြောက်ပါး (1) |
| su | ကောင်းစွာ (1) |
| sukha | သာယာမှု (4, pi-2) · သာယာသော (1, pi-2) |
| sukhāya | သာယာသော (2, pi-2) |
| tathariva | ထို့အတူ (1) |
| tathā | ထို့အတူ (1, pi-2) |
| taṇhāya | တပ်မက်မှု (3, pi-2) |
| tiṃsa | သုံးဆယ် (1, pi-2) |
| Uddhaṃ | အထက် (1) |
| upari | အထက် (1) |
| upaṭṭhānena | ပဋ္ဌာန် (3) |
| upekkhā | ဥပေက္ခာ (8, pi-2) |
| upādinna | ကံကြောင့် ဖြစ်သော (1, pi-2) |
| upādā | မူလဓာတ်ကြီးများကို မှီ၍ ဖြစ်သော (3, pi-2) |
| upādādhammehi | မူလဓာတ်ကြီးများကို မှီ၍ ဖြစ်သော သဘောတရား (2) |
| Upādānehi | စွဲလမ်းမှု (2) |
| upādānena | စွဲလမ်းမှု (3) |
| upādāniyehi | စွဲလမ်းမှု၏ အာရုံ ဖြစ်နိုင်သော (1) |
| upāyāsena | ပြင်းစွာ ပူပန်ခြင်း (3) |
| vedanā | ခံစားမှု (5, pi-2) |
| Vedanākkhandhena | ခံစားမှု အစုအဝေး (4) |
| vedanāya | ခံစားမှု (7, pi-2) |
| vicāraṇā | ဆက်လက်သုံးသပ်မှု (1) |
| vicārehi | ဆက်လက်သုံးသပ်မှု (4) |
| vidhā | မျိုး (1) |
| vippayutta | ကင်းကွာသော (2, pi-2) |
| vippayuttehi | ကင်းကွာသော (4) |
| vippayuttehi dhammehi | ကင်းကွာသော သဘောတရား (4) |
| vippayuttā | ကင်းကွာသော (13, pi-2) |
| visaṃsaṭṭhehi dhammehi | မရောနှောသော သဘောတရား (1) |
| vitakka | စတင်ကြံစည်မှု (3, pi-2) |
| vitakka / vicāraṇā | စတင်ကြံစည်မှု … ဆက်လက်သုံးသပ်မှု (1) |
| vitakka / vicārehi | စတင်ကြံစည်မှု … ဆက်လက်သုံးသပ်မှု (2) |
| vitakkehi | စတင်ကြံစည်မှု (2) |
| vitakkehi / vicārehi | စတင်ကြံစည်မှု … ဆက်လက်သုံးသပ်မှု (2) |
| viññāṇa | သိစိတ် (4, pi-2) |
| Viññāṇakkhandhena | သိစိတ် အစုအဝေး (1) |
| viññāṇakkhandhena | သိစိတ် အစုအဝေး (2) |
| viññāṇena | သိစိတ် (2) |
| vokāra | အစုအဝေး (4) |
| yogehi | ထမ်းပိုး (3) |
| yuttā | ယှဉ်သော (1) |
| ñassāmi | သိရတော့သည် (3) |
| ācaya | စုပုံခြင်း (1, pi-2) |
| ākāre | အခြင်းအရာ (1, pi-2) |
| ārammaṇaṃ | အာရုံ (1, pi-2) |
| ārammaṇehi | အာရုံ (3) |
| Āsavehi | စိတ်အစွန်းအထင်း (2) |
| āsavehi | စိတ်အစွန်းအထင်း (2) |
| āyatana | အာရုံခံ နယ်ပယ် (57, pi-2) |
| āyatanasaṅgahena saṅgahitā | အာရုံခံ နယ်ပယ် အကျုံးဝင်ခြင်း … အကျုံးဝင်သော (12) |
| āyatanehi | အာရုံခံ နယ်ပယ် (10) |
| āyatanehi dasahi | အာရုံခံ နယ်ပယ် … ဆယ်ပါး (7) |
| āyatanehi dvādasahi | အာရုံခံ နယ်ပယ် … ဆယ့်နှစ်ပါး (1) |
| āyatanehi ekādasahi | အာရုံခံ နယ်ပယ် … ဆယ့်တစ်ပါး (4) |
| āyatanehi sattarasahi | အာရုံခံ နယ်ပယ် … ဆယ့်ခုနစ်ပါး (12) |
| āyatanehi soḷasahi | အာရုံခံ နယ်ပယ် … ဆယ့်ခြောက်ပါး (1) |
| āyatanena | အာရုံခံ နယ်ပယ် (26) |
| ṭhapetvā | ချန်ထား၍ (9, pi-2) |
