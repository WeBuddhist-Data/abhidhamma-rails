# pi-5 (Kathāvatthu) Pāli→Vietnamese senses: conventions from the sample (for parts 1–6)

The sample was agg-sample.tsv (120 headwords: the first 90 rows of part 1 plus the next 30 multi-value rows, last «pathavī»). Settled 2026-11-21, awaiting user review. The brief (..\vi-senses-brief.md, with its FORBIDDEN list) and the skill (AI_translation\skills\word-sense-grouper.md) govern. Base: ..\..\pi-4-vi-ai\senses\senses-conventions.md, ..\..\pi-3-vi-ai\senses\senses-conventions.md, ..\..\pi-2-vi-ai\senses\senses-conventions.md and ..\..\pi-1-vi-ai\senses\senses-conventions.md; everything there still holds (merge rules for «sự», classifiers, tense / aspect words, «có», «khi» / «trong khi» / «sau khi», «điều», letter case; shared candidates; tag pattern **short English gloss[, distinguishing context] (grammar)**). This file records only what pi-5 adds or changes.

## 1. Workflow and tool (READ-ONLY for parts 1–6: call it, do not edit it)

Files per part K (all in this folder): `decisions-partK.txt` (your hand-written tag table) → `partK-senses.md` (output). Part 1 contains the 120 sample headwords: copy their lines from decisions-sample.txt unchanged.

```
python -I -X utf8 -B senses_tool_vi.py todo   --part K               # headwords still without a decision line
python -I -X utf8 -B senses_tool_vi.py prior  --part K [all] [lo hi] # todo (or all) headwords of the part, rows lo..hi: agg row
                                                                     # + [pi-4 vi] [pi-3 vi] [pi-2 vi] [pi-1 vi] [pi-5 ru] (+ [pi-5 en] hint)
python -I -X utf8 -B senses_tool_vi.py prior  <hw> [<hw> ...]        # same for named headwords
python -I -X utf8 -B senses_tool_vi.py words  <hw> [<value>]         # per Vietnamese value, the Pāli tokens with the stem in its segments
python -I -X utf8 -B senses_tool_vi.py show   <hw> [<value>] [<max segs>] [<width>]   # ids + Pāli/Vietnamese line pairs
python -I -X utf8 -B senses_tool_vi.py build  --part K               # builds partK-senses.md, then verifies (`sample --part K` = the same)
python -I -X utf8 -B senses_tool_vi.py verify --part K               # also fails on any CR in the output
python -I -X utf8 -B senses_tool_vi.py reuse  --part K               # lines reusing a pi-1 … pi-4 Vietnamese tag verbatim (for the report)
```

- `prior --part K` prints about 7 lines per headword: page it with a row range (`prior --part 2 1 40`, then `41 80` …). Never redirect it to a file from PowerShell.
- In PowerShell an empty argument is dropped: write `-` for "any value" (`show pada - 2 160`; max segs 0 = ids only). The debate paragraphs are long: always pass a width (160–220).
- `words` lists tokens co-occurring in the segment, not the token the keyword came from (sañña «Tưởng» lists saññākkhandho from the same segment): confirm a split with `show`.
- Decision lines as before (`hw: {tag}` or `hw: {tag1: v1 / v2; tag2: v3 / *}`), one per headword, any order. The sample had 0 " / " → " và " rewrites and 1 shared candidate string (rūpa «hình sắc», visible form and fine-material sphere, §3).

## 2. Tags: which source

1. **[pi-4 vi], then [pi-3 vi], [pi-2 vi], [pi-1 vi]**: copy the approved Vietnamese tag verbatim when pi-5 has the same headword in the same sense with the same (or a «sự» / «có» / classifier / tense / case variant of the same) Vietnamese value. Their splits are binding (ariya, para, khandha, phala, dukkha, cakkhu «mắt» / «nhãn», ṭhiti «sự tồn tại» = life list, rūpa, upekkhā and sati one sense each). Sample: 50 headwords have a prior Vietnamese line; 25 reuse a tag verbatim, 11 more adapt an example (rule 2); the other 14 had a different Vietnamese value or meaning there (rule 3).
2. **Adapt only the example compound or the grammar label** when the prior example does not occur in pi-5 or would point to the wrong sense; keep the gloss words: puggala 'Puggalakathā, ariyapuggala and puggalapaññatti'; naya 'Catukkanayasaṃsandanaṃ'; lakkhaṇa 'Lakkhaṇayuttikathā'; gati 'Gatianuyogo, Chagatikathā and duggati'; purisa 'purisapuggalā, Purisakārānuyogo and purisuttama'; vāda 'Vādayutti'; ñāṇa 'ñāṇadassana and aññāṇa'; nirodha 'nirodhasamāpatti and dukkhanirodhagāminī' (the pi-4 'third noble truth' tag is too narrow here); dibba 'dibbacakkhu and dibbasota'; upapatti 'upapattesiya and upapattikāla'; sammuti 'sammutiñāṇa and sammutisacca'; paṭicca '+ the free absolutive'; rūpa (visible form 'rūpāyatana and rūpataṇhā': rūpadhātu is the fine-material plane in pi-5, Rūpadhātukathā; matter '+ rūpajīvitindriya' for «thuộc vật chất»). Where pi-4 and an earlier book differ, take the one whose example occurs in pi-5 (phala, khandha «thân cây»: pi-2 / pi-1 'lists of smells and tastes'; dukkha «khó chịu»: pi-3, without pi-4's cloth).
3. **[pi-5 ru] word for word** when pi-1 … pi-4 Vietnamese have no line, or their line is for another meaning or value (kathā, catukka «bốn cách», suddhika «thuần túy», abhiññā, anuyoga, odhiso, paṭiññāya, parama «tối hậu» … see the sample). The pi-5 Russian tags are terse and mostly carry no grammar label: copy them as they are, do not add labels.
4. **New or combined tags** only where (a) the Vietnamese splits differently from the Russian (kathā, vata «chắc chắn» / «Quả thật», micchā, atthi, buddho, sañña, Sabbattha, purisa, hattha, pathavī, Bodhiyā), (b) one Vietnamese value covers two Russian senses (sutta: discourse + Suttanipāta title), or (c) the Russian tag is a bare English hint, which `verify` rejects (niggaha 'refutation', upādā 'clinging', Bodhiyā 'awakening', kathā 'discussion', hattha 'hand'): then write gloss + context (`rebuttal of a thesis in the debate (compound member)`).
- Forbidden in a tag: ": ", "; ", braces, Vietnamese letters, a bare English hint (`verify` checks all of them).

## 3. One sense or several: pi-5 decisions

Split (checked with `words` / `show`):
- **kathā** «Bàn về / Bàn … về / Phần» (heading word; «Phần» in Suttāharaṇakathā / Nasuttāharaṇakathā) vs «tranh luận» (the title Kathāvatthu). **vatthu** «ngọn» (tālāvatthukata) vs «vấn đề» (title).
- **vata** «chắc chắn» ('tena vata re vattabbe') vs «nghi thức» (sīlabbata; pi-1 tag) vs «Quả thật / quả thật» ('ime vata bhonto sattā' 5-377, 'bahūnaṃ vata no' 5-748; pi-2 tag, letter case = one sense).
- **micchā** «sai» (verdict 'idaṃ te micchā') vs «sai lầm» (micchādiṭṭhi …, kāmesumicchācāra; pi-4 tag).
- **niggaha** «sự bác bỏ» (debate) vs «sự chế ngự» (restraining the mind, ch24 / ch31; ru tag 'restraining the mind'). Expected: niggaho «sự chế ngự» = ru `curbing`; the numbered closers (Pañcamo niggaho …) «sự bác bỏ».
- **atthi** «tồn tại» (the existence theses, 'sabbaṃ atthi', 'puggalo atthi') vs «có» (possessive 'samāpannassa atthi vacībhedo' 5-332, 5-604).
- **vādī** «người theo học thuyết» (saka- / paravādī; ru) vs «nói / người nói» (saccavādī … ; musāvādī; pi-4 tag, head noun = one sense). **vāda** «học thuyết» (Vādayutti) vs «nói» (musāvāda; ru). **aṭṭho** «thực tại» vs «ý nghĩa» (atthaṭṭho 5-304 … 306). **anuyogo** «Chất vấn» vs «sự chuyên tâm thực hành». **upādā** «bám víu» (anupādāparinibbāna) vs «phụ thuộc» (Upādāpaññattānuyogo). **gati** «cõi tái sinh / cõi» (one sense: «cõi» in duggati) vs «lui tới» (access of monks, 5-271). **lakkhaṇa** «tướng» (marks of a great man) vs «đặc tính». **bheda**, **pada**, **citta** «nhiều màu», **khandha** «thân cây», **phala** «trái cây», **para** «Tha» / «địch»: as the ru / earlier vi splits.
- **rūpa** visible form «hình sắc» (rūpāyatana, rūpataṇhā) vs fine-material sphere «hình sắc / cõi hình sắc» (rūpāvacara, rūpabhava, rūparāga, Rūpadhātu) vs matter «vật chất / thuộc vật chất» (rūpakkhandha, rūpajīvitindriya). «hình sắc» is a shared candidate. No 'looks' sense (pi-4 only).
- **ṭhiti** «chỗ trú» (viññāṇaṭṭhiti; ru 'station') vs «sự duy trì / duy trì» (cittaṭṭhiti, ṭhitikāla; ru 'duration') vs «sự tồn tại» (the life list āyu ṭhiti yapanā …, 5-540; pi-1 / pi-2 tag).
- **Sabbattha** «ở mọi nơi» (adverb) vs «mọi bản / tất cả các bản» (edition notes; pi-4 tag) vs «mọi nơi» (sabbatthagāminī; pi-2 tag).
- **buddho** «Đức Phật» vs «bậc giác ngộ» (the thesis 'bodhiyā buddho'); **Bodhiyā** «sự giác ngộ» vs «cây Bồ-đề».
- **sañña** «có tri giác» (saññasatta, Asaññakathā) vs «Tưởng» (the realm name «chúng sinh Vô Tưởng», asaññasatta): name vs description.
- **cakkhu** «mắt» (pi-4 tag) vs «nhãn» (Dibbacakkhukathā «thiên nhãn»; pi-2 tag). **hattha** «tay / bàn tay» vs «cử chỉ tay» (hatthasaṃvācikā; ru).
- **pathavī** «đất» (element and kasiṇa; pi-1 tag) vs «mặt đất / địa» (the earth under the sky, 'nabhañca pathavī ca', and mahāpathavī «đại địa»: one meaning).
- **purisa** «người / con người / loài người» (one sense, person) vs «nam tính» (pi-1 tag).

Merge (one sense):
- head noun / classifier present or absent: puggala «bậc / người / hạng người»; vādī «nói / người nói»; paṭijānantaṃ «người thừa nhận».
- modal / gap variants: niggahetabbe «nên bị bác bỏ / nên bác bỏ»; «Bàn về / Bàn … về»; nominaliser: jahati «dứt bỏ / sự dứt bỏ», nirodha, sati, upekkhā, upapatti, samāpatti, sammuti, dukkha «khó chịu / sự khó chịu».
- synonyms: sabbaṃ «tất cả / toàn bộ / mọi» (pi-1 tag); Sabbadā «vào mọi lúc / luôn luôn»; dibba «thiên / thuộc cõi trời» (one meaning, divine faculties: dibbacakkhu «thiên nhãn», dibbasota; the termbase step has to pick per compound, see the report); paṭicca «tùy thuộc vào điều kiện / tùy thuộc vào» (pi-2 split).
- letter case: vaggo «chương / Chương», yutti «Lập luận / lập luận», sādhanaṃ, vata «Quả thật / quả thật».

## 4. Recurring pi-5 headword families: the tags

Reuse these for every form; change only the grammar label (and the compound named). Where a family form has its own [pi-5 ru] line, copy that line (rule 3); the patterns below are for forms without one.

| Family | Sense tag (source) | Vietnamese |
|---|---|---|
| assent / denial frame | Āmantā `assent of the respondent`; Nanu `'is it not so that…?'`; hevaṃ `thus indeed` (all ru); Na hevaṃ vattabbe, vattabbe: ru line, else `it should not be said thus, the respondent's denial (formula)` / `ought to be said (gerundive)` | Đúng vậy; Chẳng phải; như vậy; (không) nên nói |
| question particles -ti / nu | no keyword of their own (frame «Có phải … không?»); fused forms are tagged by the content word, naming the particle: Atītaṃ nvatthi `the past does not exist?, with the question particle nu (phrase)` | the content word |
| ājānāhi / rebuttal pentad | Ājānāhi `imperative 'admit it!'`; niggahaṃ `rebuttal of the opponent's thesis`; paṭikammaṃ `rejoinder turning the argument back`, paṭikamme `in the rejoinder`; upanayana `applying the analogy back to the case`; niggamana `drawing the final inference`; paṭipādanā `setting forth a case`; paṭiññāya `by the proposition`; hetāya `by the reason`; tava `of you`; paṭijānantaṃ / paṭijānantā `acknowledging`; dukkaṭe `badly done` (all ru) | the map values |
| niggaha- forms | niggaha `rebuttal of a thesis in the debate (compound member)` (new) / `restraining the mind` (ru); niggaho / niggahe: the rebuttal tag with their label, or ru `curbing` for «sự chế ngự»; niggaṇhāma `we rebut`, niggaṇhāsi `you rebut`, niggahetabbe / niggahetabbā `ought to be rebutted`, niggahite `when rebutted`, Suniggahito `well rebutted`, dunniggahite `badly rebutted`, Dunniggahitā `improperly rebutted` (ru) | sự bác bỏ / sự chế ngự; (nên bị) bác bỏ |
| micchā | `false, in the debate verdict 'idaṃ te micchā' 'what you say here is false' (indeclinable)` (new) / `wrong, false (compound member, as in micchādiṭṭhi)` (pi-4) | sai / sai lầm |
| vata | `emphatic 'surely', in 'tena vata re vattabbe' 'then surely, friend, it must be said' (indeclinable)` (new from ru) / `rituals, ascetic vows and observances, in sīlabbata (compound member)` (pi-1) / `truly, indeed, emphatic particle in 'ime vata bhonto sattā' of the divine-eye knowledge (indeclinable)` (pi-2) | chắc chắn / nghi thức / quả thật |
| saccikaṭṭha / paramattha | saccikaṭṭhaparamatthena `in the sense of truly real and highest reality`; saccikaṭṭho / saccikaṭṭha `truly real thing`; paramattho `highest reality`; paramatthena `in the highest sense`; parama `highest`; atthena `in the sense of a reality`; aṭṭho `reality, fact` / `meaning of a word`; aṭṭha `a reality` (all ru) | (như một) thực tại chân thật (và tối hậu); thực tại … tối hậu |
| upalabbhati | upalabbhati `is apprehended`, upalabbhanti `are apprehended` (ru); nupalabbhati: ru line, else `is not apprehended`; X upalabbhati / X nupalabbhati phrases: the ru line (`'the individual is apprehended'`, `'the individual is not apprehended'`); contiguous and gapped values one sense | (không) được tìm thấy |
| sakavādī / paravādī | sakavādī / sakavādi `the proponent of one's own doctrine` (ru); paravādī: ru line, else `the proponent of the other doctrine, the opponent (nominative)`; vādī `adherent of a doctrine` / `one who speaks, compound final in musāvādī` (ru / pi-4) | người theo học thuyết (của chúng ta / khác) |
| atthi / natthi | atthi `exists, is real, the predicate of the existence theses as in 'sabbaṃ atthi' (3rd sg. verb)` / `there is, one has, possessive as in 'samāpannassa atthi vacībhedo' (3rd sg. verb)` (new); natthi ru `there is not` for «không có»; a «không tồn tại» value: `does not exist, the negated existence predicate (3rd sg. verb)`; X atthi phrases: the ru line (`thesis phrase 'the individual exists'`, `'matter exists'`, `what has gone by is existent`) | tồn tại / có; không có / không tồn tại |
| atīta / anāgata / paccuppanna | single words: pi-2 atītaṃ `past, gone by (neuter sg.)`, anāgataṃ `future, not yet come (neuter sg.)` (paccuppannaṃ on the same pattern: `present, arisen now (neuter sg.)`), with or without «thuộc» one sense; phrases and compounds (Atītaṃ atthi, atītaṃ niruddhaṃ, Atītaṃ viññāṇaṃ atthi, atītakkhandha, Anāgatañāṇakathā …): the ru line verbatim; where ru splits matter vs visible form (Atītaṃ / Anāgataṃ / Paccuppannaṃ rūpaṃ) keep it: «vật chất (…) thuộc X» vs «hình sắc thuộc X» | (thuộc) quá khứ / tương lai / hiện tại |
| a- / an- negatives | as pi-1 / pi-4: the negative's own ru line; a fragment that lost its negative prefix keeps the positive tag and names the a-compound (ñāṇa '… and aññāṇa') | the positive Vietnamese |
| person words | Puggalo / puggalo `a person, an individual (nominative sg.)` (pi-4); puggala `individuals, as stem in Puggalakathā, ariyapuggala and puggalapaññatti (stem and compound member)` (pi-4, adapted); puggalā `types of person, as counted …` «hạng người» (aṭṭhapurisapuggalā 5-791) / `persons, individuals (nominative pl.)` «người» (pi-4); purisa (§3); attā `self, the soul posited by views (nominative sg.)` (pi-1 / pi-2); koci / kehici / añño / Aññaṃ: the ru line where pi-1 … pi-4 values differ (koci «ai đó» ≠ pi-2 «nào»), pi-1 / pi-2 aññaṃ `another, different, …` where «khác» | người / bậc / hạng người |
| agent nouns with «người» (kattā, kāretā, paṭisaṃvedī, kārako, saccavādī …) | the ru line; «người X» and «X» one sense | (người) X |
| book frame and headings | abhidhamma, Abhidhammapiṭake (pi-4); kathā (§3); kathāvatthu, vaggo, anuyogo / anuyoga, pucchā, sodhanaṃ, saṃsandanaṃ / saṃsandana, opamma, Anulomapaccanīkaṃ / Paccanīkānulomaṃ, anuloma(ṃ), paccanīka(ṃ), okāsa, avayava, suddha / suddhika, ṭīkā, oloketabbā, dassitā, lakkhaṇena (ru); X-kathā / X-anuyogo heading compounds: the ru line (`heading 'inquiry into penetration'`) | the map values |

Expected later (decide with `words` / `show`; the brief's known splits): eva «thật» (Attheva suttanto) / «chỉ» / «ngay» / «cũng» / «chính» (+ «hoàn toàn», «vẫn», «y»: check each; pi-1 / pi-4 tags for «hoàn toàn», «chỉ»); sukha «hạnh phúc» / «dễ chịu»; dhamma «hiện tượng» / «Giáo Pháp» / «đối tượng của ý» / «hành vi» / «lẽ phải» (+ «pháp», 1 case: check); rūpaṃ / Rūpaṃ «vật chất» vs «hình sắc»; dhātu «yếu tố» / «cõi»; sammā «đúng đắn» / «Hoàn Toàn» («một cách đúng đắn» = the adverb variant of «đúng đắn»); hetu «gốc rễ» / «nguyên nhân»; kāma «dục lạc» / «cõi dục lạc» (pi-2 kāmadhātu split); ārammaṇaṃ «đối tượng / có đối tượng / lấy … làm đối tượng / có … làm đối tượng» one sense (pi-1 tag); arahatta «A-la-hán / trạng thái A-la-hán» one sense; phalaṃ «thành quả / kết quả / quả»: check path fruit vs result of action.

## 5. Report items

Headword count and verify line; headwords with >1 sense; senses with >1 candidate; the `reuse` line; every shared candidate and " / " → " và " rewrite; the splits and merges against the crosscheck list (..\mapper-vi\crosscheck-values.tsv); anything unclear.
