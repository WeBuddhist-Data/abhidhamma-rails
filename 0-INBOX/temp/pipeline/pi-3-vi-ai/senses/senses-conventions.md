# pi-3 (Dhātukathā) Pāli→Vietnamese senses: conventions from the sample (for parts 1–3)

The sample was agg-sample.tsv (94 headwords: the first 90 rows of part 1 plus the next 4 multi-value rows, last «sukha»). Settled 2026-11-20, awaiting user review. The brief (..\vi-senses-brief.md, with its FORBIDDEN list) and the skill (AI_translation\skills\word-sense-grouper.md) govern. Base: ..\..\pi-2-vi-ai\senses\senses-conventions.md and ..\..\pi-1-vi-ai\senses\senses-conventions.md; everything there still holds (merge rules for «sự», classifiers, tense words, «có»; shared candidates; tag pattern **short English gloss[, distinguishing context] (grammar)**). This file records only what pi-3 adds or changes.

## 1. Workflow and tool (READ-ONLY for parts 1–3: call it, do not edit it)

Files per part K (all in this folder): `decisions-partK.txt` (your hand-written tag table) → `partK-senses.md` (output). Part 1 contains the 94 sample headwords: copy their lines from decisions-sample.txt unchanged.

```
python -I -X utf8 senses_tool_vi.py todo   --part K        # headwords still without a decision line
python -I -X utf8 senses_tool_vi.py prior  --part K        # each todo headword: agg row + [pi-2 vi] + [pi-1 vi] + [pi-3 ru] (+ [pi-3 en] hint) lines (start here)
python -I -X utf8 senses_tool_vi.py prior  <hw> [<hw> ...] # same for named headwords
python -I -X utf8 senses_tool_vi.py words  <hw> [<value>]  # per Vietnamese value, the Pāli tokens with the stem in its segments
python -I -X utf8 senses_tool_vi.py show   <hw> [<value>] [<max segs>] [<width>]   # ids + Pāli/Vietnamese line pairs
python -I -X utf8 senses_tool_vi.py build  --part K        # builds partK-senses.md, then verifies
python -I -X utf8 senses_tool_vi.py verify --part K
python -I -X utf8 senses_tool_vi.py reuse  --part K        # lines reusing a pi-1 / pi-2 Vietnamese tag verbatim (for the report)
```

- In PowerShell an empty argument is dropped: write `-` for "any value" (`show rūpa - 0` lists every id with its value; max segs 0 = ids only). pi-3 paragraphs are long: pass a width (`show sukha "hạnh phúc" 4 200`).
- `words` lists tokens co-occurring in the segment, not the token the keyword came from (the method paragraphs list many items): confirm a split with `show`.
- Decision lines as in pi-1 / pi-2 (`hw: {tag}` or `hw: {tag1: v1 / v2; tag2: v3 / *}`), one per headword, any order.
- Slash-alternative keywords (`āyatanāni / pādā`, `kāma / āyatanehi`, `vitakkehi / vicārehi`, `kāma / āyatana`): the value «a / b» is rewritten «a và b» by the tool; write the tag-only form. Tag: `merged list keyword, <what a is> and <what b is> (grammar)`. The sample had 1 such rewrite.

## 2. Tags: which source

1. **[pi-2 vi] first, then [pi-1 vi]**: copy the approved Vietnamese tag verbatim when pi-3 has the same headword in the same sense with the same Vietnamese value (a «sự» / «điều» / classifier variant counts as the same value: bodhi «giác ngộ» = pi-2 «sự giác ngộ»). Their **splits** are binding too: a pair of values that pi-1 / pi-2 keep in ONE sense stays one sense here (upekkhā «sự bình thản / bình thản», saññā «tri giác / có tri giác», saṅkhāra «tạo tác / sự tạo tác», hetukā «có gốc rễ / lấy … làm gốc rễ»), even where the pi-3 map chose the value by context (crosscheck-values.tsv). Add a sense only for a value pi-1 / pi-2 do not have (ādi «mục khác» / «bắt đầu bằng»; expected: arūpa «phi vật chất»).
2. Where pi-1 and pi-2 differ, take the one whose value set matches pi-3 best (phasso: pi-1, because the pi-2 tag also covers «loại tiếp xúc»; sammā Hoàn Toàn, dukkha pain: pi-1).
3. **Adapt only the example compound or the grammar label** when the prior example does not occur in pi-3 or would point to the wrong sense (pi-2 sukha 'sukhasahagata body-consciousness' is «hạnh phúc» here; rūpa 'Rūpadukaṃ', 'rūpataṇhā', 'Dhammahadaya'; cittaṃ 'paṭhamaṃ cittaṃ'; saṅkhāra 'padhānasaṅkhāra'; sammā 'path factors'). Keep the gloss words of the prior tag.
4. **[pi-3 ru] word for word** when pi-1 / pi-2 Vietnamese have no line, the line is for another meaning (vippayogo pi-2 «xa lìa», saṅgaho pi-1 «phân loại», saṅgaha pi-2 «tổng hợp», āyatanena pi-2 «ngành», maccu pi-2 «sự tử vong» if the value differs), or the pi-1 / pi-2 tag's grammar label is wrong for the whole pi-3 family (§4: sampayutta / vippayutta, the counted units).
5. New tags only for artefact keywords (`āyatanehi N-hi`, slash alternatives) and where one Vietnamese value covers two Russian senses (cittaṃ: combined tag).
- Forbidden in a tag: ": ", "; ", braces, Vietnamese letters, a bare English hint (`verify` checks all of them).

## 3. One sense or several: pi-3 decisions

Split (checked with `words` / `show`):
- **sukha** «dễ chịu» = sukhindriya (and Sukhāya vedanāya) vs «hạnh phúc» = sukhasahagata of the joy triad (pi-1 / pi-2 user split; pi-2 tag examples adapted). Expected: sukhāya = «dễ chịu» (pi-1 / pi-2 tag).
- **dukkha** «khó chịu» = dukkhindriya, adukkhamasukha, dukkhena of the grief series (pi-1 tag) vs «khổ đau» = dukkhasacca (pi-2 tag).
- **rūpa** «vật chất» (rūpakkhandha) vs «hình sắc» visible form (rūpāyatana, rūpadhātu of the element list, 3-23/27/32/35) vs «hình sắc» fine-material sphere (rūpabhava, rūpāvacara): shared candidate, as pi-1 / pi-2. The brief's "vật chất vs hình sắc (plane)" misses the visible-form ids; `show rūpa "hình sắc" 16 200` shows both.
- **ādi** «mục khác» (Khandhādi, Saccādi, Paṭiccasamuppādādi: "and the rest") vs «bắt đầu bằng» (Phassādisattakaṃ: "beginning with").
- **dhamma** «đối tượng của ý» (dhammāyatana, dhammadhātu) vs «hiện tượng» (Dhammasaṅgaṇī).
- **sammā** «đúng đắn» (sammappadhāna) vs «Hoàn Toàn» (sammāsambuddha).
- Expected in parts 2–3: arūpa «không hình sắc» (immaterial sphere: pi-2 Arūpa tag) vs «phi vật chất» (immaterial aggregates of the summary verse, 3-352: [pi-3 ru] second tag).

Merge (one sense):
- «điều X» (the matrix / heading noun) with «X» (the predicate): sampayuttaṃ, vippayuttaṃ, asaṅgahitaṃ, and the stems sampayutta / vippayutta / asaṅgahita (only «điều …» there).
- nominaliser / «có»: upekkhā sự bình thản / bình thản (upekkhāsahagata / upekkhindriya; pi-2 tag covers "neutral feeling or mental balance"); saññā tri giác / có tri giác (saññābhava, asaññābhava: combined tag naming 'percipient'); saṅkhāra tạo tác / sự tạo tác (saṅkhārakkhandha / saṅkhārapaccayā); hetukā có gốc rễ / lấy … làm gốc rễ (maggahetukā; pi-1 / pi-2 tag).
- one value for two Russian senses → combined tag: cittaṃ «tâm» (listed topic and 'no cittaṃ' of the summary verses).
- Gapped vs contiguous values of one phrase («hiện tượng … có gốc rễ» / «hiện tượng có gốc rễ», «tâm … được gộp vào» / «tâm được gộp vào», «có tính va chạm … được gộp vào»): one sense, as pi-2.

## 4. Recurring pi-3 headword families: the tags

Reuse these for every form; change only the grammar label (and the numeral).

| Family | Sense tag (source) | Vietnamese |
|---|---|---|
| saṅgaho / asaṅgaho / sampayogo / vippayogo (method nouns) | `the method of comprising within a category (nominative noun)`, `the method of non-comprising (nominative noun)`, `the method of non-conjunction (nominative noun)`; sampayogo: the ru line (ru) | sự gộp vào / sự không gộp vào / sự (không) gắn liền |
| saṅgaha / asaṅgaha / vippayoga (heading members) | `comprising, as heading compound member`, `non-comprising, as heading compound member`, `non-conjunction, as heading compound member` (ru); saṅgaho asaṅgaho `name of the first method, comprising and not comprising`, saṅgahāsaṅgaha `name of the first method in the headings (compound)` (ru) | same |
| asaṅgahita- (predicate and matrix noun) | `not comprised within a category (neuter sg. participle)`; asaṅgahito `(masculine sg. participle)`, asaṅgahitā `(pl. participle)`, asaṅgahitāni `(neuter pl. participle)`; stem asaṅgahita `not comprised (stem in heading compounds)` (ru); saṅgahita forms: the ru line | (điều) không được gộp vào / (điều) được gộp vào |
| sampayutta- / vippayutta- | `conjoined as co-arising mental states (neuter sg. participle)` / `not conjoined, standing apart (neuter sg. participle)`; -o masculine sg., -ā pl., -ehi instrumental pl. participle; stems `conjoined, stem in heading compounds` / `not conjoined, stem in heading compounds` (ru). Not the pi-1 / pi-2 `conjoined with, compound final …`: in pi-3 these are free predicates and method terms, not compound finals | (điều) gắn liền / (điều) không gắn liền |
| X saṅgahitā / X vippayuttā dhammā (subject + predicate keywords) | the ru line (e.g. `comprised in an element (pl. phrase)`); pi-1 vi line where the value matches (vippayuttā dhammā `phenomena dissociated from, ending the dyad answers (nominative pl.)`) | «X (…) được gộp vào» |
| counted units | khandhehi `the five aggregates as counted units (instrumental or ablative pl.)`, āyatanehi `the twelve sense bases as counted units (…)`, dhātūhi `the eighteen elements as counted units (…)`; khandhena `a single aggregate as counted unit (instrumental or ablative sg.)`, āyatanena `a single sense base …`, dhātuyā `a single element …` (ru; the pi-2 dhātuyā / āyatanena tags name other uses). Headings and lists keep the vi tags: Khandho, khandhā, Āyatanaṃ, āyatanāni, dhātu, dhātuyo, Saccaṃ, Indriyaṃ (pi-2 / pi-1) | khối / lĩnh vực nhận biết / yếu tố |
| count words | numeral stems: `N, the number (cardinal numeral)` (pi-2 vi: ekādasa, dvādasa; aṭṭhārasa `eighteen, the number of the elements (numeral)`), else the ru line (bāvīsati `the number 22, counting the faculties`, Tevīsa `the number 23 (cardinal)`); N-hi `the number N (instrumental pl.)`; N-hi dhātūhi `phrase counting N of the elements (instrumental pl.)`; N-hāyatanehi `compound counting N of the sense bases (instrumental pl.)`, dvādasahāyatanehi `compound counting all twelve sense bases (instrumental pl.)` (ru) | the numeral (+ noun) |
| āyatanehi N-hi (artefact) | `sense bases, then the numeral N of the element count, as in 'ekādasahāyatanehi ekādasahi dhātūhi' (instrumental pl. phrase)` (new; the ru "phrase counting N sense bases" misreads it) | lĩnh vực nhận biết N |
| -ena / -ehi / -āya reference words («đối với X», frame dropped) | the headword's own vi / ru tag with the instrumental label: phassena `sense impression (instrumental sg.)`, Cakkhāyatanena `the eye sense base (instrumental sg.)`, Sanidassanehi `that can be seen (instrumental pl. adjective)`, X-ehi dhammehi `… states (instrumental pl. phrase)` (ru); dukkhena = the dukkha pain sense; saṅkhārena «sự tạo tác» = ru (not pi-1 sasaṅkhārena «sự thúc đẩy») | X |
| method ordinals | heading stems pañcama … cuddasama: `ordinal Nth, in method headings` (ru); closing -mo: the pi-2 vi tag where present (pañcamo `fifth, ordinal (masculine nominative sg.)`, chaṭṭho `sixth, ordinal (…)`), else the same pattern `Nth, ordinal (masculine nominative sg.)`; Navamassa `ordinal 9th (genitive, of the ninth method)` (ru) | thứ N |
| verse words (uddāna of methods 5, 6, 9, 13 …: 3-227, 3-305, 3-352, 3-408, 3-447, 3-455) | the ru line verbatim (bhavā `modes or planes of being (nominative pl., summary verses)`, maccu, su, buddho, sahabhu, saṅgahaṃ gatā, pare, antare, labbhati, duke, niddese); vi tag only where the value matches (Rūpaṃ «vật chất» = pi-2 rūpaṃ first sense; ārammaṇaṃ «có đối tượng» = pi-1 / pi-2 tag; jīvitaṃ, pumaṃ as their pi-1 / pi-2 lines) | the map values |
| book frame and headings | abhidhamma, Abhidhammapiṭake, Uddeso, mātikā, niddeso, nayo (pi-2 / pi-1 vi); kathā, Dhātukathā, dhātukathāya, naya, nayamukha, abbhantara, bāhira, Bāhiramātikā, lakkhaṇa, visabhāgo, bhāga, sabbā (ru); dhammasaṅgaṇī: pi-1 gloss with the pi-3 role (`… named as the matrix of this book (nominative sg.)`) | the map values |
| the 16 list items (3-2) and their -ena forms | pi-2 / pi-1 vi tags (jhānāni, khandhā, manasikāro, bodhi, phasso, paṭicca, padhānā, aṅgā, indriyāni, vedanā, cetanā, sati, ariyo, maggo, iddhi, balāni, saccāni, appamaññāyo); upaṭṭhānā, samuppādo: ru | the map values |

## 5. Report items

Headword count and verify line; headwords with >1 sense; senses with >1 candidate; the `reuse` line; every shared candidate and " / " → " và " rewrite; the splits and merges against the crosscheck list; anything unclear.
