# pi-4 (Puggalapaññatti) Pāli→Vietnamese senses: conventions from the sample (for parts 1–3)

The sample was agg-sample.tsv (120 headwords: the first 90 rows of part 1 plus the next 30 multi-value rows, last «pahīnaṃ»). Settled 2026-11-20, awaiting user review. The brief (..\vi-senses-brief.md, with its FORBIDDEN list) and the skill (AI_translation\skills\word-sense-grouper.md) govern. Base: ..\..\pi-3-vi-ai\senses\senses-conventions.md, ..\..\pi-2-vi-ai\senses\senses-conventions.md and ..\..\pi-1-vi-ai\senses\senses-conventions.md; everything there still holds (merge rules for «sự», classifiers, tense words, «có»; shared candidates; tag pattern **short English gloss[, distinguishing context] (grammar)**). This file records only what pi-4 adds or changes.

## 1. Workflow and tool (READ-ONLY for parts 1–3: call it, do not edit it)

Files per part K (all in this folder): `decisions-partK.txt` (your hand-written tag table) → `partK-senses.md` (output). Part 1 contains the 120 sample headwords: copy their lines from decisions-sample.txt unchanged.

```
python -I -X utf8 senses_tool_vi.py todo   --part K        # headwords still without a decision line
python -I -X utf8 senses_tool_vi.py prior  --part K        # each todo headword: agg row + [pi-3 vi] + [pi-2 vi] + [pi-1 vi] + [pi-4 ru] (+ [pi-4 en] hint) lines (start here)
python -I -X utf8 senses_tool_vi.py prior  <hw> [<hw> ...] # same for named headwords
python -I -X utf8 senses_tool_vi.py words  <hw> [<value>]  # per Vietnamese value, the Pāli tokens with the stem in its segments
python -I -X utf8 senses_tool_vi.py show   <hw> [<value>] [<max segs>] [<width>]   # ids + Pāli/Vietnamese line pairs
python -I -X utf8 senses_tool_vi.py build  --part K        # builds partK-senses.md, then verifies (`sample --part K` = the same)
python -I -X utf8 senses_tool_vi.py verify --part K
python -I -X utf8 senses_tool_vi.py reuse  --part K        # lines reusing a pi-1 / pi-2 / pi-3 Vietnamese tag verbatim (for the report)
```

- In PowerShell an empty argument is dropped: write `-` for "any value" (`show rūpa - 0` lists every id with its value; max segs 0 = ids only). pi-4 paragraphs are long: pass a width (`show hoti - 7 160`).
- `words` lists tokens co-occurring in the segment, not the token the keyword came from: confirm a split with `show`.
- `prior --part K` prints a lot (about 6 lines per headword). Never redirect it to a file from PowerShell (brief); run it on a few headwords at a time (`prior hw1 hw2 …`) when the output is cut.
- `verify` lists a shared candidate once per extra sense (rūpa «hình sắc» in three senses prints twice).
- Decision lines as before (`hw: {tag}` or `hw: {tag1: v1 / v2; tag2: v3 / *}`), one per headword, any order. The sample had 0 " / " → " và " rewrites; 1 shared candidate string (rūpa «hình sắc», in three senses, §3).

## 2. Tags: which source

1. **[pi-3 vi], then [pi-2 vi], then [pi-1 vi]**: copy the approved Vietnamese tag verbatim when pi-4 has the same headword in the same sense with the same (or a «sự» / «có» / classifier / tense variant of the same) Vietnamese value. Their splits are binding (jīvita «mạng sống / sống» one sense as pi-1; rāga «tham đắm / sự tham đắm»; saddhā «niềm tin / có niềm tin»; arūpa «không hình sắc / cõi không hình sắc» one sense as pi-1). Sample: 51 of the 61 headwords with a prior line reuse a tag verbatim.
2. **Adapt only the example compound or the grammar label** when the prior example does not occur in pi-4 or the label is wrong for pi-4 (viharati «sống» 'vigatābhijjhena cetasā viharati'; ariya «bậc thánh» 'ariyapuggala'; cetanā `(compound member)`, as in cetanābhabbo; sammā Hoàn Toàn `(compound member)`, it is not a title line here; phala «trái cây» 'pavattaphalabhojī'; dhamma Giáo Pháp 'dhammamacchariya and dhammānusārī', hiện tượng 'dhammavicaya and adhipaññādhammavipassanā'; the group words, §4). Keep the gloss words of the prior tag.
3. **[pi-4 ru] word for word** when pi-1 / pi-2 / pi-3 Vietnamese have no line, or their line is for another meaning or value: paññatti (pi-1 / pi-2 «khái niệm» = the 'concept' sense; here combined from the ru tag), sekkhā (prior «thuộc về người còn đang tu học» is the adjective of sekkhā dhammā; here the persons), bhaya (prior «sự nguy hiểm»), niyato (prior «cố định», of results), gāmī (prior «dẫn đến»), ṭhito (prior «được giữ vững», of the body), hoti (prior «còn tồn tại», Tathāgata views), thành quả of phala (covers puññaphala / uṭṭhānaphala too).
4. **New or combined tags** only where the Vietnamese splits differently from all of them: Puggalapaññatti, paññatti, puggalā «hạng người», dhammo 'subject to' (two Vietnamese modals, one meaning), paṭipanno (one Vietnamese word for the two ru senses), dukkha «khó chịu» (pain AND cloth rough to the touch), hoti «nghĩ», ṭhita (two senses where ru has one), the «phân loại theo nhóm N» closer of the group words.
- Forbidden in a tag: ": ", "; ", braces, Vietnamese letters, a bare English hint (`verify` checks all of them).

## 3. One sense or several: pi-4 decisions

Split (checked with `words` / `show`):
- **puggalā** «hạng người» (types counted: «Hai hạng người –», simile groups) vs «người» (in the definitions; pi-1 / pi-2 tag `persons, individuals (nominative pl.)`).
- **viharati** «an trú» (attainment: 'kāyena phusitvā viharati', 'upasampajja viharati'; pi-2 tag) vs «sống» (way of living: 'brahmabhūtena attanā viharati', 'vigatābhijjhena cetasā viharati'; pi-2 tag, example adapted).
- **hoti** «nghĩ» ('Tassa (na) evaṃ hoti', 4-91 … 4-93) vs «xảy ra / có» (comes to be: āsavapariyādānañca hoti 4-16; ñāṇaṃ hoti 4-185; ru tag) vs «đem lại» ('taṃ hoti … ahitāya', cloth similes 4-116 / 4-117; ru tag).
- **dhamma** «Giáo Pháp» / «hiện tượng» (dhammavicaya, adhipaññādhammavipassanā) / «phẩm chất» (pāpadhammataro, kalyāṇadhammena: ru 'moral nature') / «đối tượng của ý» (dhammāyatana, dhammadhātu: pi-3 tag).
- **dhammo** «phẩm chất» (pāpa- / kalyāṇadhammo) vs 'subject to' «thể bị / phải» (kuppa- / parihānadhammo «có thể bị …»; avinipātadhammo «không còn phải …»: one meaning, two Vietnamese modals = candidates).
- **dukkha** «khổ đau» (truth: dukkhasacca, dukkhanirodho …; pi-2 / pi-3 tag) vs «khó chịu» (dukkhindriya, adukkhamasukha, AND the cloth «khi tiếp xúc thì khó chịu», dukkhasamphasso 4-116: one Vietnamese word for the ru 'pain' and 'rough' senses → combined tag). dukkhassa «khổ đau» (ru truth tag) vs «sự khó chịu» (4-183 jhāna; pi-1 / pi-2 'of pain').
- **rūpa** fine-material sphere «hình sắc / cõi hình sắc» (rūpasahagata, rūparāga, rūpānaṃ of 4-130; pi-1 tag) vs looks «hình sắc / màu lông» (rūpappamāṇo / rūpappasanno 4-171, 4-M-10; sarūpavacchāya 4-176; ru tag) vs visible form «hình sắc» (rūpāyatana, rūpadhātu of the matrix lists; pi-3 tag) vs matter «vật chất» (rūpakkhandho, 4-M-2; pi-3 tag). «hình sắc» is a shared candidate of three senses.
- **phusitvā** «chạm đến» (the liberations, figurative; ru) vs «chạm» (kāyena phoṭṭhabbaṃ phusitvā; pi-1 / pi-2 'having touched (absolutive)').
- **ṭhita** «dừng lại» (ṭhitakappī) vs «đứng vững» (ṭhitatto): ru has one sense; split because the Vietnamese meanings differ ('stand still' vs 'stand firm'). **ṭhito** «đã đứng vững» (phaleṭhito) vs «đứng yên» (water simile): ru split.
- **sammā** «Hoàn Toàn» (sammāsambuddho) vs «đúng đắn» (path factors, sammāpaṭipadā). **ariya** «cao quý» vs «bậc thánh» (ariyapuggalā, 4-14). **puthu** «phàm phu» / «rộng lớn». **phala** «thành quả» / «trái cây». **para** «người khác» / «Tha» (Paranimmitavasavattī; pi-1 tag). **saṅkhāra** «sự thúc đẩy» (sa- / asaṅkhāraparinibbāyī; ru) / «tạo tác» (saṅkhārakkhandho; pi-1 tag). **kammaṃ** «hành động» (-kammaṃ in the synonym strings) / «nghiệp» (pāpañca kammaṃ, 4-188). **āhāro** «sự ôm giữ» (paḷāsāhāro) / «thức ăn» (evamāhāro; pi-2 tag).
- **Group words ekaka … dasaka**: «nhóm N» (heading: Nuddeso «Phần nêu đề mục theo nhóm N», chapter title Npuggalapaññatti «… theo nhóm N») vs «phân loại theo nhóm N» (closer Nniddeso «Giải thích phân loại theo nhóm N.»), as the pi-2 matrix / exposition split. Expected: the matrix closers Ekakaṃ … Dasakaṃ = «phân loại theo nhóm N» (the closer tag with `(heading)`).

Merge (one sense):
- head noun «người» / «bậc» / «sa-môn» present or absent: Katamo puggalo «thế nào là người / bậc / sa-môn»; person names used as name and as attribute (kodhano «người giận dữ / giận dữ», upanāhī, makkhī, paḷāsī, issukī, niyato, parihānadhammo; expected: māyāvī, maccharī, ottappī, kalyāṇamitto, pāpamitto, kalyāṇa- / pāpadhammo, sīlasampanno, saṭho, muṭṭhassati, sampajāno).
- classifier «bậc»: sambuddho «bậc Tự Giác Ngộ / Tự Giác Ngộ / bậc … Giác» (incl. paccekasambuddho), sammāsambuddho.
- title vs common noun with «sự» / «về các»: paññatti «định danh / sự định danh»; Puggalapaññatti «Định danh các hạng người / sự định danh về các hạng người».
- tense / aspect word: pahīno / pahīnā / pahīnaṃ / pahīnāni «được dứt bỏ / đã được dứt bỏ»; paṭipanno «đang thực hành / thực hành» (one Vietnamese word for the ru path / welfare split: combined tag).
- synonyms: kasira «vất vả / chật vật», sāmaṃ «tự mình / chính mình», patto «đạt đến / đến được», samannāgato «được trang bị / mang» (4-203), gāmī «đi đến / đi», upahacca «khi gần mạng chung / khi gần», Niddeso «giải thích / phần giải thích».

## 4. Recurring pi-4 headword families: the tags

Reuse these for every form; change only the grammar label (and the numeral or the compound named).

| Family | Sense tag (source) | Vietnamese |
|---|---|---|
| paññatti | `designation, descriptive account, in the book and chapter titles and in the designation questions of the matrix (stem and nominative sg.)` (new, from ru); paññattiyo: ru `designations (nominative pl.)` | (sự) định danh |
| Puggalapaññatti / puggalapaññatti | `designation of persons, title of the fourth Abhidhamma book and the sixth designation of its matrix (compound)` (new); X-paññatti of the matrix list (khandha-, āyatana-, dhātu-, sacca-, indriya-): `designation of the X, one of the six designations of the matrix (compound)` | Định danh các hạng người / sự định danh về các X |
| Kittāvatā / Yāvatā / ettāvatā (+ X-ānaṃ) | the ru lines verbatim (`how far, to what extent (interrogative adverb)`, `as far as (relative adverb)`, `how far the designation of the aggregates extends (question phrase)`, `so far … extends (answer phrase)`) | bao quát (đến mức nào / ấy) |
| puggala / puggalo / puggalā / puggalānaṃ | puggala `individuals, as stem in the title compound` (ru); puggalo `a person, an individual (nominative sg.)` (pi-2 vi); puggalā `types of person, as counted in the group lists and similes, 'dve puggalā', 'tayo puggalā' (nominative pl.)` (new) / `persons, individuals (nominative pl.)` (pi-1 / pi-2 vi); puggalānaṃ: the same two tags with `(genitive pl.)` | hạng người / người |
| puggalo X / X puggalo (two-word keywords) | the ru line (`the individual is an obtainer (phrase)`, `the individual destroys life (phrase)`); one sense for contiguous and gapped values («người … X» / «người X») | người (…) X |
| definition frame | Katamo `interrogative 'which?' opening each definition`; Katamo puggalo `'which individual?', the definitional question`; vuccati puggalo `closing formula 'this individual is termed'`; vuccanti puggalā `closing formula 'these individuals are termed'`; Aṭṭhānaṃ `there is no possibility (opening formula)` (all ru); saṃvijjamānā, tathūpamo, Seyyathāpi: ru | thế nào (là người / bậc / sa-môn); người … được gọi là |
| person-type names (agent nouns / adjectives used as persons, with or without «người» / «bậc») | the ru line verbatim where it exists (Arahā `the perfected one (nominative sg.)`, kodhano `wrathful one (nominative sg.)`, akkodhano `one without wrath …`, sotāpanno `one who has entered the stream (nominative sg.)`, paccekasambuddho, sīlavā, dussīlo, sappuriso, asappuriso, pāpo); a pi-1 / pi-2 / pi-3 vi tag first where the value matches (puthujjano, sammāsambuddho, sambuddho, sīlavanto); plural counted names (piṇḍapātikā …) ru `(nominative pl.)` | (người / bậc / hạng người) X |
| members of the names | the ru 'in X' tag (samaya `occasion, as compound member in samayavimutto`, kuppa `shakable, in kuppadhammo`, parihāna `decline, in parihānadhammo`, gotra / bhū `… gotrabhū`, bhaya `dread, in bhayūparato`, upahacca `on approaching, in upahaccaparinibbāyī`, saṅkhāra `exertion, in sa-/asaṅkhāraparinibbāyī`, puthu `many, common, in puthujjana`) | the member's Vietnamese |
| -dhammo names and the suffix | dhammo `subject to, liable to, suffix -dhammo in kuppadhammo, parihānadhammo and avinipātadhammo (nominative sg.)` / `moral nature, in pāpa-/kalyāṇadhammo` | thể bị / phải; phẩm chất |
| a- / an- negatives | as pi-1: the negative's own ru line ('unshakable, in akuppadhammo', 'incapable (compound member)', 'one without wrath'); a fragment that lost its negative prefix (hiriko of ahiriko, eḷā of aneḷā, pahīnāni of appahīnāni) keeps the positive tag naming the a-compound (ru `having moral shame, in ahiriko (nominative sg.)`, `dumb, slow-witted, in eḷamūgā`) | the positive Vietnamese |
| -ī agent nouns of the duka / tika strings (makkhī, paḷāsī, issukī, maccharī, māyāvī …) | ru `one who X (nominative sg.)` | (người) X |
| participles «được / đã được» | pahīno / pahīnā / pahīnaṃ / pahīnāni `given up (… participle)` (ru), one sense with and without «đã» | (đã) được dứt bỏ |
| group words ekaka … dasaka | `Ns, the groups of N items (heading member)` (pi-2: duka `pairs, the dyad groups …`, tika `triads, the groups of three …`, ekaka `ones, the single-item group, in Ekakauddeso and Ekakapuggalapaññatti …`) / `classification by Ns, the N-fold exposition, in the closing label Nniddeso (heading member)` (pi-2, example adapted); matrix closers Ekakaṃ … Dasakaṃ `classification by Ns, closing label of the N-fold section of the matrix (heading)` | nhóm N / phân loại theo nhóm N |
| numerals with puggalā (Dve, Tayo, Cattāro … Dasa puggalā) | ru line; Dasa puggalā `ten types of person (phrase, nominative pl.)` style | N hạng người |
| simile nouns (X-ūpamo / X-ūpamā puggalā; the objects) | ru verbatim: stem `X as a simile (stem in compound)` / nominative `X (nominative sg.)` (valāhaka, mūsika, amba, kumbha, udakarahada, balībadda, āsīvisa, rukkha, yodhājīva, aruka, vijju, vajira, potthaka, gilāna); kumbho ru two senses (three-wisdoms pot vs four-jars jar) only if the Vietnamese differs, else one combined tag; upamā / upama / upamo `simile, likeness (compound final)` / `resembling (compound member)` / `resembling, compound final (nominative sg.)` (ru) | giống như; the object with its classifier (đám mây mưa / mây mưa: one sense) |
| book frame | abhidhamma, Abhidhammapiṭake, Niddeso (pi-3 vi); mātikā / Uddeso: pi-3 vi where the value matches | the map values |

## 5. Report items

Headword count and verify line; headwords with >1 sense; senses with >1 candidate; the `reuse` line; every shared candidate and " / " → " và " rewrite; the splits and merges against the crosscheck list (..\mapper-vi\crosscheck-values.tsv); anything unclear.
