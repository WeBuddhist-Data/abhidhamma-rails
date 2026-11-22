# pi-6 Vietnamese zero-shot: harmonise pass (2026-11-22), decisions and remaining divergences

Script: harmonise_vi.py (exact strings, scoped to one file and one segment or the whole file, asserted counts; rules run in order; reads backup-pre-harmonise/, so it is re-runnable; dashes, ellipses, block IDs, heading levels and variant brackets asserted unchanged on every changed line; the sample is never written and is asserted byte-identical with its backup). Log: harmonise-log.tsv (107 entries). Divergence finder: find_divergences_vi.py (divergences-pre.md = before, divergences.md = after). Helpers (pi-6 files only): vi_common.py, probe_vi.py, probe_heads_vi.py, probe_heads2_vi.py, probe_ye_ca_vi.py, probe_members_vi.py, probe_open_vi.py. Adapted from the pi-5 tools (pi-5 files untouched). Builders not rerun.

Precedence used: (1) the approved sample (build_sample_vi.py / 1-mulayamaka.md, vi-zeroshot-terms.md), (2) pi-1-5 wording (pi-1 first), (3) zeroshot-coordinator-rules.md, (4) the frame-setter's form, (5) the majority form.

## Lines changed
3-01 1, 3-04 11, 3-05 7, 3-06 22, 5-01 5, 5-02 7, 5-03 5, 6-01 23, 6-02 15, 8 3, 9-01 4, 9-02 4 (total 107). Unchanged: preamble, 1-mulayamaka (sample, byte-identical with the backup), 2-01, 2-02, 3-02, 3-03, 4, 7-01 … 7-11, 9-03, 10-01 … 10-13.

## Checks (after the pass)
All 44 files: check_chapter_ids OK, dashcheck 0 dash-line mismatches / 0 extra em-dashes, pi-1-vi-ai\verify_rails_vi.py OK; NFC; no CR; no «—», «:-», «….», «là là», «được được», «chánh niệm», «(f)». Sample (preamble.md, 1-mulayamaka.md) byte-identical with backup-pre-harmonise/. Repo root: no new file (the three empty build_4_vi.py, build_5_vi.py, build_15_vi.py there date from 2026-11-21).

## Named points
- **asammohantena** (editorial notes, one each in 3-01, 5-02, 5-03, 6-02) = «mà không mê lầm» (pi-1 sammoha «sự mê lầm» ^1-390; 5-02 ^6-5-153 and 5-03 ^6-5-164 already). Changed: 3-01 ^6-3-12 «…từng thuật ngữ một, không để nhầm lẫn)» → «…từng thuật ngữ một mà không mê lầm)»; 6-02 ^6-6-158 «phân tích một cách không nhầm lẫn,» → «phân tích mà không mê lầm,». Neither sentence needs «một cách»: the phrase follows the verb directly, as in 5-02 / 5-03.
- **Two-part citta kinds** = «tâm <A part> và <B part>» (coordinator rule; 5-01, 5-02, 10-03, 10-04 already): 9-01 ^6-9-39, ^6-9-43 and 9-02 ^6-9-105, ^6-9-109 (4 lines each) «tâm vừa không gắn liền với các hiện tượng thiện vừa không gắn liền với các hiện tượng bất thiện» (and the reverse order) → «tâm không gắn liền với các hiện tượng thiện và không gắn liền với các hiện tượng bất thiện». No other «tâm vừa …» for a two-part citta kind is left (the remaining «vừa … vừa …» are the sample's Añceva Bñca BOTH frame, which stays).
- **Answer heads, one «ở» per run of persons**: no change needed. The finder (probe_heads_vi.py, probe_heads2_vi.py) finds no head anywhere in which a person group repeats «ở» after another person group. The 11 lines in 6-02 with «…, ở chúng sinh Vô Tưởng» (^6-6-96, 97, 116, 126 ×2, 127 ×2, 145, 146, 156, 157) are all "Pacchimacittassa bhaṅgakkhaṇe asaññasattānaṃ": «Vào khoảnh khắc tan rã của tâm cuối cùng, ở chúng sinh Vô Tưởng». The «ở» comes after a time phrase, so by the brief's own rule the person group keeps its «ở». The identical Pāli in 10-11 (×4) has the same form, as do 9-01, 9-02, 5-02 and 8 after «vào khoảnh khắc …». Changing 6-02 would split identical Pāli from 10-11. 6-02 ^6-6-106 «…, khi tâm thứ hai đang diễn ra, ở chúng sinh Vô Tưởng» also follows a time phrase (dutiye citte vattamāne). 10-06's head6() already gives one «ở» to a run of persons (the only repeats are after «vào tâm mà ngay sau đó … sẽ sinh khởi», a time phrase, identical with 10-07 and 10-12).
- **«Pacchimabhavikānaṃ saghānakānaṃ / itthīnaṃ / purisānaṃ upapajjantānaṃ» = one group**: no change needed. 10-10 already has it as one group in all 4 lines (^6-10-388 ×4: «Ở những người thuộc kiếp sống cuối cùng đang tái sinh là người nam …»), byte-identical with 10-09 and 10-11. 10-10 has no saghānaka line; the split reported in agents-run.md is not in the file.
- **«ye ca somanassena / upekkhāya <plane>ṃ upapajjitvā parinibbāyissanti»**: no change needed. The only Pāli with a plane is 10-06 ^6-10-309 (2 lines, "ye ca somanassena rūpāvacaraṃ"), both «những người nào sau khi tái sinh vào cõi hình sắc mà có niềm vui đi kèm sẽ nhập Niết-bàn trọn vẹn»: plane first, then «mà» + attribute, the 3-02 frame («tái sinh vào cõi dục lạc mà không có mắt», the earlier frame-setter). 10-05 has no line with this Pāli. Its attribute-first lines («sau khi tái sinh có mắt và có niềm vui đi kèm») render "sacakkhukā somanassena" (two attributes, no plane), which 10-06 renders the same way.
- **Cut questions «…pe…?» / «…?»** = the sample's «… không?» (^6-1-98, vi-zeroshot-terms.md; 7-02 ^6-7-54 already): «…?» → «… không?» in 3-04 11, 3-05 7, 3-06 22, 5-01 5, 5-02 7, 5-03 5, 6-01 23, 6-02 14, 8 3 (97 lines, one per line, each aligned with a Pāli question cut by …pe… / … and ending in «?»). Cut lines ending "…pe…." (no «?», e.g. 3-05 ^6-3-166, ^6-3-171, ^6-3-173) keep «…» as in the sample's «Ye keci … Y…pe…» frame. 3-01's «?…pe…» = «? …» (question complete before the cut) is untouched.
- **sabbattha**: both kept, by context. «ở mọi nơi» = in every plane (7-02 36, 7-04 37, 7-06 46, 7-08 46 lines, anusaya answers «<person>, ở mọi nơi, …»). «ở mọi chỗ» = in every case or section of the text (editorial notes 3-01 ^6-3-13, ^6-3-40, 3-04 ^6-3-124, 5-01 ^6-5-40, 6-01 ^6-6-31: «yatthakaṃ … sabbattha sadisaṃ»).

## Divergence groups before / after (find_divergences_vi.py)
Before: (a1) 0, (a2) 0, (a3) 1, (s2) line skeletons 6, (s3) sentence skeletons 3, (h) answer heads 0, (b) 0, (e) 4.
After: (a1) 0, (a2) 0, (a3) 0, (s2) 6, (s3) 3, (h) 0, (b) 0, (e) 4.
Skeleton masks: khandha, āyatana, dhātu (4 only), sacca, saṅkhāra, indriya, anusaya names, the kusala / akusala / abyākata dhammā and the sa- / a-cakkhuka attributes, masked as X on both sides. 4,412 line skeletons and 738 answer heads were compared (431 heads across more than one chapter).
- (a3) resolved: "(Kha) yattha vā pana…pe…?" (5-01 ×2, 6-01 ×2 «(b) Còn ở nơi nào…?» vs 7-02 «… không?»), settled by the cut-question rule.
- Remaining (s2) / (s3), 9 groups, all one point: bare dukkhaṃ in the paṇṇatti naming questions (Ka) dukkhaṃ X / na dukkhaṃ na X: 5-01 «khổ đau» (the truth of suffering, dukkhasacca, pi-2) vs 10-01 «sự khó chịu» (bodily pain, the dukkhindriya member, pi-2 ^2-221). The Pāli word is the same but the sense differs with the yamaka. Kept: not a divergence.
- Remaining (e), 4 cases: 2-01 ^6-2-36, 5-02 ^6-5-130, 10-13 ^6-10-455 (×2). The Pāli question ends in «.» and the Vietnamese ends in «?». The chapter agents rendered these as meant and listed them in agents-run.md / notes. Kept (brief point 6).

## Builder constants that would need the same change (builders not rerun)
- build_3-01_vi.py l.146 note «…dựa trên từng thuật ngữ một, không để nhầm lẫn)»; build_6-02_vi.py l.108 ASAMMOHA = «một cách không nhầm lẫn».
- build_9-01_vi.py l.186 VIPPAYUTTA2 = «tâm vừa không gắn liền với {a} vừa không gắn liền với {b}» (9-02 imports it).
- Cut questions «…?»: build_8_vi.py EXACT_LINE "Yassa vā pana…pe…? Āmantā …pe…." (l.468) and the two «…?» lines (l.455, l.459); build_6-01_vi.py frag_question (l.254); build_3-04_vi.py cut_q; build_3-06_vi.py cut questions (l.86 ff.); build_3-05_vi.py (from build_8); build_5-01_vi.py PE_Q handling; build_5-02_vi.py; build_5-03_vi.py yo_pe_question (l.96); build_6-02_vi.py (from build_6-01). In each, PE + "?" becomes PE + " không?" (build_7-02_vi.py Q_PE_KHA is the model).

## Not decided here: for the user (termbase stop)
Forms in use now, and where (probe_open_vi.py):
- sakkāya standalone «tự ngã» (sabbasakkāyapariyāpanna …): 7-01 (3 lines).
- dhātu as plane: headings dhātupucchāvāro / dhātuvisajjanāvāro «Mục hỏi theo các yếu tố» / «Mục trả lời theo các yếu tố» (7-10 ×1, 7-11 ×2), while the body renders kāma- / rūpa- / arūpadhātu as «cõi dục lạc / cõi hình sắc / cõi không hình sắc» (7-01 … 7-11).
- Aṭṭhamako «Người thứ tám»: 7-05, 7-06, 7-07, 7-08, 10-13.
- tadekaṭṭhaṃ «<X> vốn cùng hiện diện với nó» («những gì cùng hiện diện với nó»): 7-05, 7-07 (8 lines each).
- after no ca + negative verb: «vẫn dứt bỏ» (7-06 125, 10-13 6), «vẫn hiểu biết trọn vẹn» (2-02, 3-06, 5-03 2 each, 7-07 61, 7-08 64, 10-13 8).
- «không có A và B» for "neither" (no ca A ca B ca sānusayo): 7-03 (37 lines), 7-07 (the pariññā equivalent); may read as "not both".
- na vattabbo «không nên nói là “…” hay “…”» (pi-1 / pi-2 «nên nói»): 7-09 91, 7-10 94.
- kassaci «ở một số người» (pi-2 «ở một số chúng sinh»): 7-11 (187).
- bhaṅgā «phải phân chia» (alt. «phải phân tích»): 7-10, 7-11 (81 each).
- uppajjittha «đã sinh khởi» (8 agent preferred «đã từng»); negative «chưa từng sinh khởi», after no ca «đã từng sinh khởi»: all pavatti chapters (2-01, 2-02, 3-01 … 3-06, 5-01 … 5-03, 6-01, 6-02, 8, 9-01 … 9-03, 10-05, 10-08, 10-12).
- uppanna «ở trạng thái đã sinh khởi»: 8 (230).
- piyarūpa / diṭṭhisaññā / dibbacakkhu … «hiểu theo nghĩa …»: 3-01 4, 4 4, 10-01 23 (2-01 the same frame).
- «Tai còn lại không phải là năng lực» (could read "the other ear"): 10-01 1, 10-02 2.
- itthīnaṃ / purisānaṃ upapajjantānaṃ «đang tái sinh là người nữ / là người nam» (alt. «tái sinh làm người nữ»): 10-02, 10-03, 10-04, 10-08 … 10-11.
- ñāṇasampayuttānaṃ «gắn liền với hiểu biết» (alt. «có hiểu biết đi kèm»): 10-02, 10-03, 10-04, 10-08, 10-09.
- eteneva bhāvena katici bhave «sau khi trải qua một số kiếp sống trong chính trạng thái ấy»: 10-05, 10-06, 10-07, 10-09 … 10-12.
- bhava «kiếp sống» (pi-1 … 5 «kiếp» = aeon): the same chapters.
- 6-01's «Vào tâm mà ngay sau đó <tâm cuối cùng …> sẽ sinh khởi» (reads stiffly): 6-01 21, 6-02 40, 10-05 6, 10-06 12, 10-07 6, 10-12 7. The different Pāli with uppādakkhaṇe is «vào khoảnh khắc sinh khởi của tâm mà ngay sau đó …» (10-09 6, 10-10 3, 10-11 3).
- pavatte «trong đời sống» (coordinator rule): 5-01 … 5-03, 9-01, 9-02, 10-02 … 10-04, 10-08 … 10-11.
- kāyikaṃ dukkhaṃ «khổ đau nơi thân» vs pi-1 «sự khó chịu nơi thân»: 5-01 (4 lines).
- anaññātaññassāmīti bare «sự biết được điều chưa từng biết»: 10-01 19, 10-02 10.
