Map the Pāli keywords of one pi-6 (Yamaka) chapter to the Vietnamese zero-shot. Your chapter is named in the message (N = its number prefix, e.g. 10-03).

Read and follow exactly: D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai\vi-mapper-brief.md and mapper-vi\map-coordinator-rules.md in the same folder (first-rendering rule; fused vs separate negatives; the placeholder keyword; Itaresaṃ / plane-being position rules).

Frame-setters (load with importlib from mapper-vi\):
- map_10-02_vi.py: value1002 (chains 10-01 FACULTIES / faculty_value, value303 → 3-02 / 3-01 / 2-01), ATTR10 / BEINGS_ATTR (attribute beings: itthīnaṃ «người nữ», somanassena «có niềm vui đi kèm», ñāṇasampayuttānaṃ …), citta10, moment10, mulaka10.
- map_2-01_vi.verb_value for every uppajjati / nirujjhati tense keyword; map_2-02_vi.parinna_value and PARINNA tables for the pariññāvāra; map_5-03_vi pajahati tenses; map_8_vi aspect forms and «tâm cuối cùng …»; map_6-01_vi ANANTARA-type phrases («ngay sau») if they occur.
- Earlier Indriya map chapters (map_10-0N_vi.py) that already exist: follow them for identical Pāli and Vietnamese; others run at the same time.
Pacchima citta kinds (e.g. somanassasampayuttapacchimacittaṃ) are not parsed by citta10: take the word order from the segment, as 8 / 6-01 do, and list them in your notes.

Read notes-map-10-01.md, notes-map-10-02.md and the mapped files. Run `python -I -X utf8 -B 0-INBOX\temp\pipeline\pi-6-vi-ai\mapper-vi\verb_audit_vi.py <part>` (0 differences) and check_parts_vi.py before reporting. Write files only with the Write tool at their full paths; nothing at the repo root, no temp files, no helper files beyond your three (<part>.mapped.md, map_<N>_vi.py, notes-map-<N>.md). Return your report as text.
