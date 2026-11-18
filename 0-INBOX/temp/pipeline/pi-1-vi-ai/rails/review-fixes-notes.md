# pi-1 Vietnamese rails: review fixes (findings r1-r4), 2026-11-18

Script: `review_fixes_vi.py` (backup `backup-pre-review/`, always reads from the backup; `--dry` supported).
Log: `review-fixes-log.tsv` (rule, file, segment, line, old, new). Verify log: `review_fixes_verify.log`.
Termbase adherence: `review_fixes_adherence_pre.md` (855 misses with the updated termbase) and
`review_fixes_adherence_post.md` (884); diff with `review_fixes_adh_diff.py`.

The rails builders were NOT rerun (that would drop these fixes). Before any rebuild, the builder constants
below need the same change. Line numbers are as of today.

| Rule | Change | Builder constant(s) to change |
|---|---|---|
| r1#1 | «không có gốc rễ cần dứt bỏ» -> «không có gốc rễ nào cần dứt bỏ»; neva … na …: «…thấy chân lý, cũng không có gốc rễ nào …» | `build_rails_sample_vi.py` R_SEE / R_DEV (l.102-103) and the PAIRS / PRED entries for the na / neva … pahātabbahetukā names; `build_rails_4-01_vi.py` PRED_X (l.758-759); `build_rails_3-01_vi.py` EKAKA list items |
| r1#2 / r4#4 | yathādiṭṭhissa ca padhānaṃ = «Và sự nỗ lực của người có quan điểm tương xứng như thế» | `build_rails_sample_vi.py` PAIRS 1-M2-138 (l.421); `build_rails_4-02_4-03_vi.py` l.694 takes it from there |
| r1#3 | «…, là trạng thái mà nhờ đó các bậc thánh mô tả người ấy – “…”» | `build_rails_2-01_2-02_vi.py` PIECES (l.348) |
| r1#4 | rūpañca «Phần vật chất» (1-M2-109) and ^1-1317 «phần vật chất là gì? … đó được gọi là phần vật chất» | `build_rails_sample_vi.py` PAIRS 1-M2-109 (l.376); `build_rails_4-02_4-03_vi.py` FIXED entry for «Tattha katamaṃ rūpaṃ? …» (see by_note l.885) |
| r2#1 | heading ^1-1-7-0 «Loại không xác định về mặt đạo đức là quả của nghiệp» | `build_rails_2-04_vi.py` heading map «#### Abyākatavipāko» (l.344) |
| r2#2 | ^1-565 «Các quả của nghiệp, thuộc loại không xác định về mặt đạo đức.» | `build_rails_2-05_vi.py` «Vipākā abyākatā.» (l.266) |
| r2#3 | Tasseva …: «. Còn khi một người <jhāna clause>, là quả của chính <nghiệp / tầng thiền> ấy đã được tạo và <tích lũy / tu tập>, thì vào lúc ấy …» | `build_rails_2-04_vi.py` TASSEVA (l.288-291) and clause(); `build_rails_2-05_vi.py` TASSEVA_P / TASSEVA_V (l.146-147) |
| r2#4 | ^1-555 «Điều mà ở những hiện tượng đã hiểu biết trọn vẹn ấy là sự hiểu biết trọn vẹn, …» | `build_rails_2-05_vi.py` ANNV_RE handler (l.85-88; ANNATAVI l.52) |
| r2#5 | asuropo «sự nói năng cộc cằn» (anasuropo keeps «sự không thô lỗ», locked termbase) | `build_rails_2-04_vi.py` DOSA_V (l.154); `build_rails_4-01_vi.py` / `4-02_4-03` reuse DOSA_V |
| r3#1 | ^1-584 «…; khi đã sinh khởi thì có thể được sáu loại thức nhận biết; …» | `build_rails_3-01_vi.py` EKAKA «uppannaṃ» + «chahi viññāṇehi viññeyyaṃ» (l.230) |
| r3#2 | ^1-590 «… mà thân có thể nhận biết: có loại …, có loại …; vật chất mà yếu tố ý …» | `build_rails_3-01_vi.py` the aṭṭhaka join (sukhasamphassaṃ / dukkhasamphassaṃ l.105-106) |
| r3#3 | drop «Điều mà là» in ch3 (elements; «Sự tích lũy …, đó là sự tăng trưởng …»; «Sự tăng trưởng …, đó là sự liên tục …») | `build_rails_3-02_3-03_vi.py` definitions at l.542-551 (they use REL = S.REL «Điều mà»); do NOT change S.REL itself (ch4/ch5 still use «Điều mà là») |
| r3#4 | «? <items> (không) do nghiệp đã được tạo –» | `build_rails_3-02_3-03_vi.py` the «(Na) kammassa katattā» answer builder (rest, l.174) |
| r3#5 | ādāsamaṇḍalassa «mặt gương» | `build_rails_3-02_3-03_vi.py` OBJ_WORDS (l.403) |
| r3#6 | vaṇṇanibhā «ánh màu» | `build_rails_3-02_3-03_vi.py` VN (l.388) |
| r4#1 | «… theo phương pháp chia bốn, hoặc N tầng thiền theo phương pháp chia năm …» | `build_rails_5_vi.py` jset() (l.128-131) |
| r4#2 | kenaci: «Những hiện tượng nào mà một loại thức nào đó có thể nhận biết, còn một loại thức nào đó không thể nhận biết?»; closing «Những hiện tượng này là những hiện tượng mà …»; ^1-1464 «… đều là những hiện tượng mà …» | `build_rails_4-01_vi.py` PRED_X (l.762-763) and kenaci_vi(); `build_rails_5_vi.py` l.566-567 |
| r4#3 | ṭhapetvā X; taṃsampayutto: «gắn liền với <X> ấy» («cảm giác ấy»); plural exclusions keep «chúng» | `build_rails_4-01_vi.py` WITH_THEM (l.69) where the excluded factor is singular; `build_rails_4-02_4-03_vi.py` L (l.835) |
| r4#5 | ^1-1051 «ở nơi bản thân của họ» | `build_rails_4-01_vi.py` INNER (l.284-289) |
| r4#6 | ^1-1350 «Một người từ bỏ lời nói thô cộc, …, không đưa đến định tâm, và nói lời không có lỗi, …» | `build_rails_4-02_4-03_vi.py` FULL (l.579) |
| r4#7 | ^1-1418 «thuộc cõi hình sắc hoặc thuộc cõi không hình sắc» (as ^1-1027) | `build_rails_5_vi.py` the mahaggatā answer |
| r4#8 | «A vừa là N vừa gắn liền với B» (B is an N) / «A vừa là N vừa có / gắn liền với N là B» | `build_rails_4-01_vi.py` REL_TO (l.408), vv (l.582); `build_rails_4-02_4-03_vi.py` l.365-381 |
| r4#9 | «Những <N> cùng sinh khởi theo nhóm hai hoặc ba –»; «Quan điểm và sự tham lam khi cùng sinh khởi –» | `build_rails_5_vi.py` l.214-219 and the diṭṭhi-ca-lobho-ca entry |
| r4#10 | cittahetukaṃ «có tâm làm nguyên nhân» | `build_rails_3-02_3-03_vi.py` CITTAJA / NA_CITTAJA (l.150-151); `build_rails_4-02_4-03_vi.py` and `build_rails_5_vi.py` reuse them |

## Termbase entries still carrying pre-fix wording (termbase not writable here)
These cause the new adherence misses (884 vs 855); none is a translation miss:
- upādāya vaṇṇanibhā, maṇisaṅkhamuttāveḷuriyassa vaṇṇanibhā, jātarūparajatassa vaṇṇanibhā («màu sắc và dáng vẻ …»), vaṇṇa «màu sắc» in vaṇṇanibhā (r3#6).
- lokuttara…jjhānā phrase entries with «và» (r4#1).
- Abyākatavipāko, Vipākā abyākatā (r2#1, r2#2).
- pahātabbahetukā «có gốc rễ cần dứt bỏ» vs «không có gốc rễ nào cần dứt bỏ» (r1#1).
- Yo «điều» at ^1-641/642/734/736/868/871 (r3#3), yathā «theo» (r1#2).
- rūpañca «phần vật chất» (48, pre-existing): ch5 «rūpañca, nibbānañca» keeps «vật chất và Niết-bàn» per the phrase entry «rūpañca nibbānañca»; only the matrix pair and ^1-1317 changed.
