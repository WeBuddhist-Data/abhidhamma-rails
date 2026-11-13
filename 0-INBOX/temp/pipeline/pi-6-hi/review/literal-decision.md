# pi-6 Hindi: translate the Pāli as written (user decision, 2026-11-13)

The user decided: no emendations unless the source data (tipitaka.org) is updated. The Hindi now follows the Pāli as written, like the English rails. This supersedes the U1 emendations of apply_review_fixes_pi6.py.

Source check (source-check\): ^6-6-121 "na nirujjhittha" is in our source, the CST extracted data, VRI's GitHub XML and the SuttaCentral Mahāsaṅgīti edition; ^6-6-132 lacks "na" in our source, the CST data and VRI's XML, while the Mahāsaṅgīti edition reads "na nirujjhatīti".

Reverted to literal by revert_to_literal_pi6.py (literal-log.tsv, backups in backup-pre-literal\):
- ^6-6-121 (6-02): «शरीर की रचना समाप्त नहीं हुई थी और वाणी की रचना समाप्त होगी।»
- ^6-6-132 (6-02): «… क्या उसमें मन की रचना समाप्त होती है?»
- ^6-7-243 (7-07): «… क्या वहाँ अहंकार की सुप्त प्रवृत्ति को पूरी तरह समझा जाता है?»
- ^6-10-240 (10-05): «… क्या वहाँ आँख की क्षमता उत्पन्न हुई थी?» (tattha for tassa)
- ^6-9-192 (9-03): «हितकर परिघटनाएँ» (note removed)
- ^6-10-357 (10-08): «कान की क्षमता» (note removed)
- ^6-10-361 (10-08): tenses as written (notes removed)

Kept as rendered (spelling or agreement slips, not meaning): upapajj-/uppajj- confusions (^6-3-212, ^6-10-206, ^6-10-309, ^6-10-398), nirujjhattha, nirujjhiti, vadanā, ariyāpanne, anusanti, kāmārāga-, vītakkantaṃ, nappajjahittha, bhavissanti for bhāvessanti (^6-10-452), singular/plural verb slips (^6-10-140, ^6-10-385, ^6-10-454, ^6-10-459, ^6-10-468), missing or stray ca, punctuation. Source labels and headings were already kept as written.
