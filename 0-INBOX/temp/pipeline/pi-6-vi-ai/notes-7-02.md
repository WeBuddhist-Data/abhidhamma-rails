# notes-7-02: Anusayavāra, paṭiloma (nānuseti), 7-02-anusayayamaka.md

Builder: build_7-02_vi.py (imports build_sample_vi and build_7-01_vi; importing writes nothing).
Format: Pāli = tiếng Việt. [7-01] = frame-setter constant used verbatim; [7-01 proposed] = 7-01 proposal, now used; [new] = settled here.
The builder also re-translates all 253 lines of 7-01 and asserts they equal the finished 7-01 file byte for byte,
and checks identical Pāli sentences across 7-01 and 7-02 give identical Vietnamese.

## Reused from 7-01 (verbatim)
Tendencies and tl() lists (A ca B ca = A và B; A, B và C; A…pe… B = A… B) [7-01]
nānuseti / nānusenti = không nằm sẵn; no ca … nānuseti / nānusenti = … vẫn nằm sẵn [7-01 proposed]
(Ka) yassa A nānuseti tassa B nānusetīti? = (a) Ở người nào mà A không nằm sẵn, thì ở người ấy có phải B không nằm sẵn không? [7-01]
yattha … tattha … / yassa yattha … tassa tattha … ; (Kha) … vā pana … = Còn … [7-01]
A nānuseti, no ca tassa B nānuseti = A không nằm sẵn, nhưng ở người ấy B vẫn nằm sẵn [7-01 BUT_C]
A ca nānuseti B ca nānuseti = A không nằm sẵn, đồng thời B cũng không nằm sẵn [7-01 BOTH_C]
Arahato = Ở bậc A-la-hán [7-01 proposed]
apariyāpanne = nơi những gì không nằm trong các cõi tồn tại [7-01 proposed]
sabbattha = ở mọi nơi; <person> sabbattha <clause>. = <person>, ở mọi nơi, <clause>. [7-01 proposed]
Anusayavāra (heading) / Anusayavāro. = Mục về khuynh hướng tiềm ẩn / Mục về khuynh hướng tiềm ẩn. [7-01 proposed]
Anusayavāre paṭilomaṃ. = Chiều ngược trong mục về khuynh hướng tiềm ẩn. [7-01 proposed VARE_DIR]
(Gha) paṭilomapuggalo / (Ṅa) paṭilomaokāso / (Ca) paṭilomapuggalokāsā = (d) Chiều ngược theo người / (đ) Chiều ngược theo nơi chốn / (e) Chiều ngược theo người và nơi chốn [terms; labels from build_sample_vi.LABEL, Vietnamese alphabet order (a)(b)(c)(d)(đ)(e)(g)(h), coordinator update]
(Ekamūlakaṃ) … (Chakkamūlakaṃ) = (Phần dựa trên một mục) … (Phần dựa trên bộ sáu) [7-01]

## New: «…pe…» shortenings (same as notes-7-04 where they overlap)
<statement>…pe…. / <statement> …pe…. = <statement without its period>… [new; «….» never written; = 7-04]
<person> sabbattha…pe…. = <person>, ở mọi nơi… (Arahato sabbattha…pe…. = Ở bậc A-la-hán, ở mọi nơi…; Dvinnaṃ puggalānaṃ sabbattha…pe…. = Ở hai hạng người, ở mọi nơi…) [new]
Āmantā …pe…. = Đúng vậy… [new; = 7-04]
(Kha) yattha vā pana…pe…? = (b) Còn ở nơi nào… không? [new; sample «…?» = «… không?»; «mà» dropped with the omitted clause]

## Source notes (translated as written)
^6-7-43 «nānusenti…pe….» vs ^6-7-63 «nānusenti …pe….»: spacing only, same rendering («…» attached).
^6-7-54 «(Kha) yattha vā pana…pe…?»: the whole (Kha) question is shortened in the Pāli; kept short.
No spelling slips found in 7-02.

## 7-04 frames
Checked against the coordinator's "From 7-04": 7-02 has no nominative person subjects and no niranusayo;
«Āmantā …pe….» = «Đúng vậy…» and «<statement>…pe….» = «<statement>…» are identical to 7-04.

## Tool note
With the new labels there is no «(f)» in 7-02; verify_rails_vi.py prints OK.
