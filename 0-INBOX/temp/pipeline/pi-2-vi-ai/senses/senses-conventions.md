# pi-2 (Vibhaṅga) Pāli→Vietnamese senses: conventions from the sample (for parts 1–8)

The sample was agg-sample.tsv (120 headwords: the first 90 rows of part 1 plus the next 30 multi-value rows, last «icchatā»). Follow these conventions so all eight parts read as one file.
The brief (..\vi-senses-brief.md, with its FORBIDDEN list) and the skill (AI_translation\skills\word-sense-grouper.md) govern. Base: the pi-1 Vietnamese file ..\..\pi-1-vi-ai\senses\senses-conventions.md; everything there still holds (merge rules for «sự», classifiers, tense words, «có»; shared candidates; tag pattern). This file records only what pi-2 adds or changes. The pi-2 Russian conventions (..\..\pi-2-ru\senses\senses-conventions.md) are the model for the splits.

## 1. Workflow and tool

Files per part K (all in this folder): `decisions-partK.txt` (your hand-written tag table) → `partK-senses.md` (output).

```
python -I -X utf8 senses_tool_vi.py todo   --part K        # headwords still without a decision line
python -I -X utf8 senses_tool_vi.py prior  --part K        # each todo headword: agg row + [pi-1 vi] + [pi-2 ru] (+ [pi-2 en] hint) lines (start here)
python -I -X utf8 senses_tool_vi.py prior  <hw> [<hw> ...] # same for named headwords
python -I -X utf8 senses_tool_vi.py words  <hw> [<value>]  # per Vietnamese value, the Pāli tokens with the stem in its segments
python -I -X utf8 senses_tool_vi.py show   <hw> [<value>] [<max segs>] [<width>]   # ids + Pāli/Vietnamese line pairs
python -I -X utf8 senses_tool_vi.py build  --part K        # builds partK-senses.md, then verifies
python -I -X utf8 senses_tool_vi.py verify --part K
python -I -X utf8 senses_tool_vi.py reuse  --part K        # lines reusing a pi-1 Vietnamese tag verbatim (for the report)
```

- In PowerShell an empty argument is dropped: write `-` for "any value" (`show rūpa - 0` lists every id with its value; max segs 0 = ids only).
- pi-2 paragraphs are long: pass a width (`show Hetu "nguyên nhân" 3 200`).
- `words` lists tokens co-occurring in the segment, not the token the keyword came from; confirm a split with `show` when a segment holds several compounds.
- Decision lines as in pi-1 (`hw: {tag}` or `hw: {tag1: v1 / v2; tag2: v3 / *}`), one per headword, any order.
- The sample had 0 " / " → " và " rewrites and 1 shared candidate (rūpa «hình sắc», see §3).

## 2. Tags: which source

1. **[pi-1 vi] first**: copy the approved pi-1 Vietnamese tag verbatim when pi-2 has the same headword in the same sense with the same Vietnamese value (sample: 48 of the 60 shared headwords).
2. **[pi-2 ru] next**: when the headword has no pi-1 Vietnamese line, or the pi-1 tag's example compound / context does not occur in pi-2 (pi-1 Sacca «idaṃsaccābhinivesa», Indriya «indriyabaddha», Dhamma «Dhammasaṅgaṇī», āyatana «(accusative sg.)»), copy the pi-2 Russian tag verbatim.
3. **New or adapted** only where the Vietnamese values split differently from both (§3), or one Vietnamese value covers two Russian senses (combined tag).
- Pattern and grammar labels: as pi-1/pi-2 Russian, incl. `(phrase, nominative sg.)`, `(verb phrase)`, `(present passive)`, `(heading and heading member)`. Forbidden: ": ", "; ", braces, Vietnamese letters, a bare English hint.

## 3. One sense or several: pi-2 additions

Merge (one sense):
- classifier / nominaliser / «có» / tense word, as pi-1: cảm giác / loại cảm giác (vedanā), tri giác / loại tri giác / có tri giác (saññā; «có tri giác» = saññābhava), hiểu biết / sự hiểu biết / loại hiểu biết (Ñāṇa; title «các loại hiểu biết»), tạo tác / sự tạo tác (saṅkhāra), sự bình thản / bình thản, tu học / sự tu học, sinh / đã sinh ra (jātaṃ; «sinh» is the member of «cùng sinh» = sahajātaṃ), đã sinh / đã sinh ra, sinh khởi / đã sinh khởi, sau khi sinh khởi / đã sinh khởi, ở dạng thô / thô, ưu việt / ở mức ưu việt, tùy thuộc vào điều kiện / tùy thuộc vào.
- synonyms: đã hiện ra / đã xuất hiện (pātubhūtā), đã phát sinh / đã phát khởi (nibbattā), tham muốn / ước muốn (icchatā; both in pāpicchatā), cảm giác … khó chịu / cảm giác khó chịu (gapped vs contiguous).
- one value for two Russian senses → combined tag: vatthu «chỗ dựa» = basis (ñāṇavatthu, physical base) AND kusītavatthu «chỗ dựa của sự lười biếng»; saṅkhāra «sự tạo tác» also renders padhānasaṅkhāra «sự tạo tác bằng nỗ lực».

Split (checked with `show`):
- **N-groups, NEW pattern for Vietnamese:** the Vietnamese splits by matrix vs exposition, in BOTH the knowledge chapter (16) and the minor-topics chapter (17): «bộ N» = the group in Nmātikā («Ma trận bộ một»), Dukamūlaka / Tikamūlaka («Dựa trên bộ đôi»), the Pañhāpucchaka subheadings Tikaṃ / Dukaṃ, Kusalattikaṃ, Rūpadukaṃ, and the tetrads of dependent origination (Hetucatukkaṃ «Bộ bốn về nguyên nhân»); «phân loại theo nhóm N» = Nniddesa («Giải thích phân loại theo nhóm một») and the closing labels «Dukaṃ.» / «Tikaṃ.» / «Catukkaṃ.» of ch16 and ch17. Tags: Russian group tag for «bộ N»; `classification by twos, the twofold exposition, in Dukaniddesa of the knowledge and minor-topics chapters (heading member)` / closing label `classification by twos, closing label of the twofold sections of the knowledge and minor-topics chapters (heading)`. (The Russian "division into N kinds … knowledge chapter" does not fit ch17, and the Vietnamese value says «phân loại».) Expected later: Catukkaṃ / Pañcakaṃ «phương pháp chia bốn» (jhāna method, pi-1 Catukka/Pañcaka tags) as a third sense.
- rūpa (stem): vật chất (matter) vs hình sắc (visible form; also rūpadhātu of ch3 «yếu tố hình sắc») vs hình sắc again for the fine-material sphere (rūpabhava, the plane rūpadhātu of ch18 «cõi hình sắc»): shared candidate, as pi-1. rūpaṃ: vật chất / phần vật chất / thuộc vật chất (matter, nāmarūpa, predicate) vs hình sắc vs **«điều»** (piyarūpaṃ sātarūpaṃ «điều đáng yêu, điều khoan khoái», 4-sacca and 16-ñāṇa). rūpā: hình sắc vs thuộc vật chất / vật chất.
- Dhātu: yếu tố vs cõi (only the plane headings and lines of ch18; ch3 kāmadhātu etc. stay «yếu tố», so the cõi tag names the Dhammahadaya chapter).
- Dukkha: khổ đau vs khó chịu / sự khó chịu (pain; incl. sukhadukkha of the past-lives formula) vs khó khăn; dukkhā: khó chịu vs khổ đau (aggregates / sense pleasures are suffering).
- āhāro: dưỡng chất (pi-1 tag, incl. kabaḷīkāro āhāro) vs **thức ăn** (evamāhāro, "such was my food", past-lives recollection, 2-829). Not the Russian food/nutriment split.
- āyatana / āyatanaṃ: lĩnh vực nhận biết (sense base, incl. saḷāyatana, chaṭṭhāyatana) vs lĩnh vực (head of a named base: cakkhāyatana, ākāsānañcāyatana …).
- upādāya: phái sinh từ / dựa vào (ajjhattikassa upādāya) / tùy thuộc vào (2-809, the possible and impossible).
- Jāti: sự sinh vs **xuất thân** (jātimada «sự say sưa vì xuất thân»; new split, the Russian has one sense).
- As the Russian: Khandha khối / thân cây; Hetu gốc rễ / nguyên nhân; kiriyā mang tính chức năng / việc làm (pāpakiriyā); pāda nền tảng / chân; vatthu chỗ dựa / chủ đề (Khuddakavatthu title); Dhamma hiện tượng / đối tượng của ý / Giáo Pháp.

## 4. Recurring headword families: the tags of the sample

Reuse these whenever the same Vietnamese value turns up under any form; adapt only the grammar label and the example compound.

| Family | Sense tag (source) | Vietnamese |
|---|---|---|
| khandha | `aggregate, a group of phenomena (nominative sg.)`; pl. `aggregates, groups of phenomena (nominative pl.)`; X-kkhandho `the aggregate of X (nominative sg.)` (pi-1 vi) | khối; khối X |
| | Khandha `aggregates, in Khandhavibhaṅga and khandhadhātuāyatana (stem and compound member)` / `stems, plant stalks, in the list of tastes (compound member)` (ru) | khối / thân cây |
| rūpa | `matter, material form (heading and compound member, as in rūpakkhandha and Rūpadukaṃ)` | vật chất |
| | `visible form, the object of the eye (compound member, as in rūpāyatana, rūpataṇhā and the element rūpadhātu)` | hình sắc |
| | `the fine-material sphere, as in rūpabhava and the plane rūpadhātu of the Dhammahadaya chapter (compound member)` | hình sắc (cõi hình sắc) |
| | rūpaṃ `of such a nature, a thing that is, as final member of piyarūpaṃ … sātarūpaṃ … (compound final)` (new) | điều |
| rūpaṃ + adj. | `coarse matter, gross material form (phrase, nominative sg.)`, `matter gone by, past matter …` (ru) | vật chất X |
| saṅkhāra | `formations, volitional activity, of the fourth aggregate and of dependent origination, also in padhānasaṅkhāra 'formation of striving' (stem and compound member)` (new, combined) | tạo tác / sự tạo tác |
| dhātu | `element, an irreducible constituent (stem and compound final)` (pi-1 vi) / `plane of existence, in kāmadhātu, rūpadhātu and arūpadhātu of the Dhammahadaya chapter (compound final)` (new) | yếu tố / cõi |
| āyatana | `sense bases, the sense fields, as in Āyatanavibhaṅga (stem and compound member)`; āyatanaṃ `sense base, sense field (nominative/accusative sg.)` / `base, sphere, as head of a named base such as cakkhāyatana or ākāsānañcāyatana (compound final)` (ru) | lĩnh vực nhận biết / lĩnh vực |
| dhamma | `phenomena, states, as in Dhammahadaya and dhammapaṭisambhidā (stem and compound member)` (ru) / `mind-objects, … (compound member, as in dhammadhātu and dhammataṇhā)` (ru) / `the Buddha's teaching, in dhammamacchariya and dhammapaṭisanthāra (compound member)` (pi-1 vi) | hiện tượng / đối tượng của ý / Giáo Pháp |
| dukkha | `suffering in general, as in dukkhasacca …` / `pain, painful feeling or contact, as in dukkhasamphassa and dukkhadhātu …` / `difficult, of the mode of progress in dukkhapaṭipadā (compound member)` (ru) | khổ đau / khó chịu, sự khó chịu / khó khăn |
| hetu | `root, a root condition, as in 'na hetu' and hetusampayutta …` / `cause, in Hetucatukkaṃ of dependent origination and Hetuvāra of the analytical knowledges (heading member)` (ru) | gốc rễ / nguyên nhân |
| N-groups | `pairs, the dyad groups (heading member)` (pi-1 vi), Ekaka `ones, the single-item group, in Ekakamātikā (heading member)`, Tika `triads, the groups of three …`, Catukka … Dasaka `Ns, the groups of N items (heading member)` (ru); Tikaṃ / Dukaṃ / catukkaṃ: ru group tags | bộ một … bộ mười |
| N-exposition | `classification by Ns, the N-fold exposition, in Nniddesa of the knowledge and minor-topics chapters (heading member)`; closing line `classification by Ns, closing label of the N-fold sections of the knowledge and minor-topics chapters (heading)` (new) | phân loại theo nhóm N |
| āhāra | `nutriment, a sustaining condition, including edible food in kabaḷīkāro āhāro (nominative sg.)` (pi-1 vi) / `food one ate, in evamāhāro of the recollection of past lives (compound member)` (new) | dưỡng chất / thức ăn |
| upādāya | ru three tags | phái sinh từ / dựa vào / tùy thuộc vào |
| vatthu | `basis, ground, as in ñāṇavatthu and the physical base of consciousness, also the grounds for laziness in kusītavatthu (compound final)` (combined) / `topic, subject matter, in the title Khuddakavatthuvibhaṅga (compound member)` (ru) | chỗ dựa / chủ đề |
| jāti | `birth, being born (stem and nominative)` / `birth as social standing, family origin, in jātimada 'pride of birth' (compound member)` (new) | sự sinh / xuất thân |
| past/future frame, quality pairs, headings | the ru tags (atīta, anāgata, paccuppanna, niruddha …, Pañhāpucchakaṃ, vibhaṅgo, Suttanta) and the pi-1 vi tags (oḷārika, sukhuma, hīna, paṇīta, bhājanīyaṃ, Tattha, uppanna, pātubhūtā, jātā, nibbattā) | the map values |

Expected later: sukha hạnh phúc / dễ chịu / dễ dàng (three senses in pi-2, per the brief); viharati sống / an trú; pasāda chất nhạy cảm / lòng tin trong sáng; vossagga sự buông xả / sự buông lơi; kāmadhātu yếu tố dục lạc / cõi dục lạc; sati = sự tỉnh thức.

## 5. Report items

Headword count and verify line; headwords with >1 sense; senses with >1 candidate; the `reuse` line; every shared candidate and " / " → " và " rewrite; the most consequential splits and anything unclear.
