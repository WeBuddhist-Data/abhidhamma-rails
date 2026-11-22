# pi-6 keyword map: coordinator rules (binding for every map agent)

The coordinator adds rules here while map agents run. Re-read before you build and before you report.

## User decisions (2026-11-22, map sample approved as proposed)
- kusalaṃ / akusalaṃ / abyākataṃ / nāmaṃ: the form of their first occurrence in the segment (predicate «thiện», subject «hiện tượng bất thiện» …).
- kusalā dhammā inside the pair questions: the discontinuous «hiện tượng … thiện»; where the text has «hiện tượng thiện» together (headings), that.
- yassa / tassa = «người nào» / «người ấy» (no «ở»); yattha / tattha = «ở nơi nào» / «ở nơi ấy».
- hetu inside the hetuvāra series «nguyên nhân» (kusalahetū «nguyên nhân thiện»).

## Frame-setters for this run
- Each yamaka's first chapter (2-01, 3-01, 4, 5-01, 6-01, 7-01, 8, 9-01, 10-01) sets the member values of its yamaka; later chapters of that yamaka import its map_<N>_vi.py.
- Shared frames across yamakas (uppajjati / nirujjhati and tenses, the beings and planes, the person / place relatives, pariññā verbs): 2-01 first; 7-01 for anuseti / pajahati / parijānāti; 8 for the aspect forms (uppajjamāna, uppanna, niruddha …). If a value you need is already in a finished chapter's map, use it.

## Shared values fixed by the coordinator
(added here as agents report)
- The keyword files contain a literal keyword `(no direct equivalent)` (about 90 times in 24 files: the extraction's placeholder for a Pāli word it could not name). Keep it as a keyword and map it `(no direct equivalent)=(no direct equivalent)` (7-01, 3-01). Never guess a Pāli word for it, never drop it; it counts as NDE in the report.
- Frame tables to import: map_2-01_vi (frames201: verbs, planes, beings, persons), map_3-01_vi (BASES, BARE, ATTR, SENSE, PLANE_LOC with kāmāvacara / rūpāvacara / arūpāvacara, BEINGS_GEN, value3), map_7-01_vi (value701), map_10-01_vi (FACULTIES, faculty_value, value10).
- suddhāvāsānaṃ = «chúng sinh trong cõi Tịnh Cư» where the text has it (3-01, 2-01), not the sample proposal «cõi Tịnh Cư».
- puggalassa / puggalānaṃ = «hạng người» where the text has «hạng người» (7-01).
- A negative verb that appears twice in a segment, once plain («không nằm sẵn») and once denied after no ca («vẫn nằm sẵn»): map the first rendering in the segment («không …»), as 7-02 does (first-rendering rule). Same for the FUSED negatives nappajahati, nānuseti, niranusayo, appahīno, nuppajjati (the negation is part of the keyword, so «không» is in the value). Clarified 2026-11-22: where the Pāli has a SEPARATE «na» before the verb (na parijānāti, na uppajjati …), the keyword is the positive verb and its value is the positive verb («hiểu biết trọn vẹn»), as 2-01 / 2-02 / 7-07 / 7-08 do; the «không» belongs to the na.
- uppajjati / nirujjhati and their tenses: always through map_2-01_vi.verb_value (the polarity of the verb's first rendering in the segment; a bare verb and its -ti question form count as one verb). So «sẽ sinh khởi» in one segment and «sẽ … sinh khởi» (from «sẽ không sinh khởi») in another are both correct; 8's 257 tense keywords were checked identical with verb_value. Do not hand-pick per clause.
- Planes in the accusative / ablative (rūpāvacaraṃ, kāmāvacarā …) = «cõi …» (the «vào» / «khỏi» is frame); genitive beings (-ānaṃ) = «chúng sinh trong cõi X», but «cõi X» when the text does not repeat «chúng sinh trong» (a plane-being that directly follows another one); asaññasattānaṃ keeps «chúng sinh» (3-02; map_3-02_vi has the position rule: use it).
- A plane-being right after Itaresaṃ («Ở những chúng sinh khác trong cõi gồm năm khối»): Itaresaṃ = «chúng sinh khác», the plane-being = «cõi X»; Itaresaṃ alone = «người khác» (2-01, 3-03). map_3-02_vi.value302 alone misses this: āyatana / dhātu chapters import map_3-03_vi.value303.
- pajahati tenses (5-03, map_5-03_vi): pajahittha «đã dứt bỏ» / na «chưa từng dứt bỏ»; pajahissati «sẽ dứt bỏ» / na «sẽ không dứt bỏ»; after no ca «vẫn sẽ dứt bỏ» (first-occurrence polarity, the parijānāti templates of 2-02). bhāveti and sacchikaroti in 9-03 / 10-13 follow the same templates.
- pahīno / appahīno (and -ti / -ā forms): use map_7-09_vi.pahina_value (polarity from the keyword's OWN stem's first Pāli occurrence), not 7-01's VERBS lookup, which would give appahīno the rendering of pahīno. pahīno «đã được dứt bỏ», appahīno «chưa được dứt bỏ».
- Indriya pacchima citta kinds: «tâm cuối cùng <kind>» as the text (map_10-07_vi.pacchima10); «dassetvā … upapajjitvā»: the one «sau khi» belongs to dassetvā, so upapajjitvā = «tái sinh» there (10-07 ^6-10-328 / 329), «sau khi tái sinh» elsewhere.
- X-ānusayañca (and other -ñca / -ñceva forms of a member) = the member's value; the chain can raise KeyError on them, so use map_7-05_vi.tendency_ca (anusaya chapters) or strip -ñca / -ñceva before the lookup (7-05).
- paṭilomapuggalo / paṭilomaokāso / paṭilomapuggalokāsā = «chiều ngược theo người / theo nơi chốn / theo người và nơi chốn» (7-02).
