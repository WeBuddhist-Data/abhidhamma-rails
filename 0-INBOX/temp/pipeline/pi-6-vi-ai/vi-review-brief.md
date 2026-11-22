# Brief: independent review of the Vietnamese Yamaka (pi-6), plain rails translation

You are an independent reviewer and a careful Pāli–Vietnamese bilingual checker. You are READ-ONLY: do not edit any translation file.
- Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: use the Read tool; run python as `python -I -X utf8 -B`; write helper scripts with the Write tool at full paths under D:\Work\OpenPecha\abhidhamma-rails (never write any file from PowerShell, not even a scratch file), LF line endings.
- Put any helper scripts in 0-INBOX\temp\pipeline\pi-6-vi-ai\review\, named after your part (r1_*.py …). Never create files at the repo root, outside the repo or in a system temp folder. Never run git; never write "seed". No web.
- **Never write a file that contains Tịnh Sự text** (no dumps, no extracts, no aligned copies, no word lists from it): your scripts may read it and print to the console, nothing more. Your report must not quote it beyond a few words to identify a point.
- Do not open the termbase, the keyword maps, the word senses, the Vietnamese zero-shot, or any builder, notes or log in 0-INBOX\temp\pipeline\pi-6-vi-ai\ (rails\, termbase\, senses\, mapper-vi\, build_*, notes-*, agents-run.md, harmonise*, backup-pre-harmonise\, divergences*): the point is a reading that is not anchored on them.
- Grep only the specific files named here, never whole folders.
- You cannot write report files: return your report as text.

## Inputs
- **Pāli:** AI_translation\pali\pi-6_split_chapters\<ch>.md
- **Our Vietnamese (under review):** the same filenames in AI_translation\vietnamese\pi-6-vietnamese-plain-rails_split_chapters\
- **Alignment:** segments align by the block ID at the end of each segment (e.g. ^6-2-61); non-empty lines align one to one.
- **Reference human translation (Tịnh Sự):** 1-SOURCES\Translations\Vietnamese\vi-6-tinh_su.md, block-aligned to the same IDs. It is COPYRIGHTED: use it only to check meaning. Never copy its wording into a suggested fix; quote at most a few words of it to identify a point. Your suggested fixes must be in our own words and our own terms.
- **Optional references** for hard readings: the English pi-6 AI_translation\english\pi-6-english-plain.md (by block ID); the commentary 1-SOURCES\Commentaries\pi-yamaka-atthakatha.md. The Pāli is the authority.
- **The approved pi-1 … pi-5 Vietnamese** (AI_translation\vietnamese\pi-1/2/3/4/5-vietnamese-plain.md): lists pi-6 shares with them (khandha, āyatana, dhātu, sacca, indriya, anusaya names; person types; planes; jhānas; path / fruit phrases) should match unless a decision below says otherwise; report unexplained drift as MAJOR (consistency).
- **Style:** 0-INBOX\temp\pipeline\vietnamese-style.md. **Audience:** AI_translation\audience_profile\plain.md (no Buddhist background; clear, natural, modern Vietnamese, nothing added).

## About the text
The Yamaka («Các cặp câu hỏi») asks every question in a pair: (a) «Ở người nào mà A …, thì ở người ấy có phải B … không?» / (b) «Còn ở người nào mà B …, thì ở người ấy có phải A … không?», and answers «Đúng vậy.», «Không.», «Không có.», or a partial answer that names the persons, planes or moments for which it holds and does not hold («Ở <người>, A …, nhưng ở người ấy không có B …»; «A …, B cũng …»). Ten yamakas (gốc rễ, khối, lĩnh vực nhận biết, yếu tố, sự thật, tạo tác, khuynh hướng tiềm ẩn, tâm, hiện tượng, năng lực), each in sections (paṇṇatti: naming questions; pavatti: arising / ceasing in present, past, future and mixed tenses; pariññā; anusaya sections). Everything turns on:
- polarity: na, no, a-/an-, natthi, «no ca» (= "but not"), "neither … nor"; a separate na vs a fused negative; a denied negative after no ca (= positive);
- tense and aspect: uppajjati «sinh khởi» / uppajjittha «đã sinh khởi» (negative «chưa từng sinh khởi») / uppajjissati «sẽ sinh khởi»; uppanna «ở trạng thái đã sinh khởi»; uppajjamāna «đang sinh khởi»; the mixed-tense pairs must keep each clause's own tense;
- the answer heads: which persons, planes, moments; nothing dropped or added; order kept;
- complete lists; …pe… = «…» and nothing expanded; the same Pāli frame reads the same everywhere.

## Translation policy and user decisions (not errors)
- **Source as written (user):** source slips are kept; only plain spelling slips and missing punctuation are rendered as meant. Lines where the Pāli itself looks inconsistent were translated as written and are already listed for review (^6-7-243, ^6-9-192, ^6-6-121, ^6-10-357, ^6-10-361): assess them briefly and say whether you agree. DO flag places where the Vietnamese ADDS or DROPS something the Pāli does not support.
- **Approved terms and frames:** book «Các cặp câu hỏi»; yamaka titles «Các cặp câu hỏi về …»; labels (a) (b) (c) (d) (đ) (e) (g) (h); the frames of the approved sample (1-mulayamaka.md); mūla «gốc rễ» / mūlamūla «cội rễ»; hetu in the ten-term series «nguyên nhân» (sahetuka / ahetuka «có / không có gốc rễ»); paṭiloma «chiều ngược» / paccanīka «chiều nghịch»; uppajjati «sinh khởi» / upapajjati «tái sinh»; parijānāti «hiểu biết trọn vẹn», pajahati «dứt bỏ», bhāveti «tu tập», sacchikaroti «tự mình chứng nghiệm»; pahīna «đã được dứt bỏ» / appahīna «chưa được dứt bỏ»; after no ca a denied negative «vẫn V» (past «đã từng V»; pahīna «đã được dứt bỏ»); "neither" «không có A, cũng không có B»; kassaci «ở một số chúng sinh»; itthīnaṃ / purisānaṃ upapajjantānaṃ «… tái sinh làm người nữ / người nam»; «Phần tai còn lại không phải là năng lực»; kāyika / cetasika dukkha «sự khó chịu nơi thân / trong tâm»; bare dukkhaṃ «khổ đau» (Sacca) / «sự khó chịu» (Indriya); dhātu headings «Mục hỏi / trả lời theo các cõi»; beings «chúng sinh trong cõi X», Itaresaṃ «người khác» («chúng sinh khác trong cõi X» before a plane); sakkāya «tự ngã»; Aṭṭhamako «Người thứ tám»; tadekaṭṭha «những gì cùng hiện diện với nó» (as a modifier «…, vốn cùng hiện diện với nó»); na vattabbo «không nên nói là …»; bhaṅgā «phải phân chia»; the «hiểu theo nghĩa …» frame (piyarūpa, diṭṭhisaññā, dibbacakkhu …); ñāṇasampayutta «gắn liền với hiểu biết»; eteneva bhāvena «trong chính trạng thái ấy»; bhava «kiếp sống» (kappa «kiếp»); pavatte «trong đời sống»; anaññātaññassāmīti «sự biết được điều chưa từng biết»; samāpannānaṃ «người đang nhập»; sānusayo «có»; the anantarā phrases «… ngay sau tâm này» / «vào khoảnh khắc … của tâm mà ngay sau đó …».
- **Already listed for the user (assess briefly, give your view; do not re-report as new):** the run join «…, và …» where an inner list keeps its «và» (67 places); cutassa «đã chết đi khỏi»; heṭṭhā «xuống phía dưới»; katici «một số» / dassetvā «trải qua» («sau khi trải qua một số kiếp sống»); aññindriya «năng lực hiểu biết trọn vẹn» beside parijānāti; questions the Pāli ends with "." rendered «?» (^6-2-36, ^6-5-130, ^6-7-335, ^6-10-455).

## Part A: bilingual check of every segment
**1. CRITICAL: meaning errors** — a negation lost or added; a tense or aspect changed; an answer («Đúng vậy» / «Không» / «Không có» / a partial answer) not matching the Pāli; a person, plane, moment or member dropped, added or swapped; content on the wrong ID.
**2. MAJOR** — Vietnamese that is ungrammatical or misleading for a plain reader (e.g. a list that reads as "not both" where the Pāli says "neither"); the same Pāli rendered inconsistently within your part, across the book, or against pi-1 … pi-5 where the Pāli is the same.
**3. MINOR** — awkward wording or register; repetition; heavy heads that could be eased without changing a term.
**Typography:** "–" only where the Pāli has one; statements end with "."; questions with "?" and a Vietnamese question word; no «….».

## Part B: comparison with the Tịnh Sự translation (meaning only)
For every segment of your part, compare on MEANING. Report only where it reveals something to check:
- a different reading that changes the meaning (polarity, tense, which persons / planes, a different sense of a word): check the Pāli (and commentary) and say which is right. Tịnh Sự is not the authority.
- content one has and the other lacks (beyond …pe… expansions): which is right.
- a passage where Tịnh Sự is clearly easier for a lay reader in structure: describe the structural point and propose a fix in our own words.
Do not report terminology differences where ours follows the decisions above or is another valid word.

## How to check
The Yamaka repeats one frame thousands of times: check it by script. Per line, compare the Pāli's negations (na, no, natthi, a-/an-, nappa-, nānu- …) with the Vietnamese (không, chưa, chẳng, «không có», and the «vẫn» / «đã từng» of a denied negative); tense markers (-ittha / -issati / -māna / -nna vs «đã / chưa từng / sẽ / đang / ở trạng thái»); «?» counts; Āmantā / No / Natthi vs «Đúng vậy / Không / Không có»; the number of person and place items in each answer head; list-item counts. Then read the headings, the editorial notes in brackets, the first occurrence of every frame and a sample of each repeat by eye.

## Report (concise, plain text, as your final message)
- Part A table: ID | file | severity | Pāli (short) | Vietnamese (short) | problem | suggested fix (our wording).
- Part B table: ID | file | kind (reading / content / clarity) | what differs (brief) | which is right and why | suggested fix to ours, or "none".
- Group repeats: where one problem recurs in many segments, give it once with the list of IDs.
- Counts per severity and kind, segments checked, and a one-paragraph overall judgement.
