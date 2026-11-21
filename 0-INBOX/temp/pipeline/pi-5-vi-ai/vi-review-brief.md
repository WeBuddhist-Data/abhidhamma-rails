# Brief: independent review of the Vietnamese Kathāvatthu (pi-5), plain rails translation

You are an independent reviewer and a careful Pāli–Vietnamese bilingual checker. You are READ-ONLY: do not edit any translation file.
- Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: use the Read tool; run python as `python -I -X utf8 -B`; write helper scripts with the Write tool at full paths under D:\Work\OpenPecha\abhidhamma-rails (never write any file from PowerShell), LF line endings.
- Put any helper scripts in 0-INBOX\temp\pipeline\pi-5-vi-ai\review\, named after your part (r1_*.py …). Never create files at the repo root, outside the repo or in a system temp folder. Never run git; never write "seed". No web.
- **Never write a file that contains Tịnh Sự text** (no dumps, no extracts, no aligned copies, no word lists from it): your scripts may read it and print to the console, nothing more. Your report must not quote it beyond a few words to identify a point.
- Do not open the termbase, the keyword maps, the word senses, the Vietnamese zero-shot, or any builder, notes or log in 0-INBOX\temp\pipeline\pi-5-vi-ai\ (rails\, termbase\, senses\, mapper-vi\, build_*, notes-*, agents-run.md, harmonise*, backup-pre-harmonise\, divergences*): the point is a reading that is not anchored on them.
- Grep only the specific files named here, never whole folders.
- You cannot write report files: return your report as text.

## Inputs
- **Pāli:** AI_translation\pali\pi-5_split_chapters\<ch>.md
- **Our Vietnamese (under review):** the same filenames in AI_translation\vietnamese\pi-5-vietnamese-plain-rails_split_chapters\
- **Alignment:** segments align by the block ID at the end of each segment (e.g. ^5-112); non-empty lines align one to one.
- **Reference human translation (Tịnh Sự):** 1-SOURCES\Translations\Vietnamese\vi-5-tinh_su.md, block-aligned to the same IDs. It is COPYRIGHTED: use it only to check meaning. Never copy its wording into a suggested fix; quote at most a few words of it to identify a point. Your suggested fixes must be in our own words and our own terms.
- **Optional references** for hard readings: the English pi-5 AI_translation\english\pi-5-english-plain.md and the Russian AI_translation\russian\pi-5-russian-plain-rails_split_chapters\<ch>.md (by block ID); the commentary 1-SOURCES\Commentaries\pi-kathavatthu-atthakatha.md. The Pāli is the authority.
- **The approved pi-1 … pi-4 Vietnamese** (AI_translation\vietnamese\pi-1/2/3/4-vietnamese-plain.md): passages pi-5 shares with them (lists, jhāna formulas, path / fruit phrases, paṭiccasamuppāda, the condition names, person types, sutta passages) should match unless a decision below says otherwise; report unexplained drift as MAJOR (consistency).
- **Style:** 0-INBOX\temp\pipeline\vietnamese-style.md. **Audience:** AI_translation\audience_profile\plain.md (no Buddhist background; clear, natural, modern Vietnamese, nothing added).

## About the text
The Kathāvatthu («Các vấn đề tranh luận») is a book of debates. Each kathā tests a thesis in question-and-answer form between our side (sakavāda) and an opponent (paravāda): «Có phải X không? Đúng vậy. / Không nên nói như thế.»; the rebuttal pentad (anuloma, paṭikamma, niggaha, upanayana, niggamana: «Nếu … thì … Điều bạn nói ở đây là sai …»); sutta quotations brought by either side («Chẳng phải Đức Thế Tôn đã nói … sao?», «Có bài kinh như vậy thật không? Đúng vậy.»); each kathā closes «Phần bàn về X đã hoàn tất.»; each chapter (vagga) closes with its name and a summary (uddāna); five groups of fifty kathās (paṇṇāsaka) close with their own summary. Everything turns on:
- polarity: na, no, a-/an-, natthi, «na vattabbaṃ»; Āmantā «Đúng vậy» vs Na hevaṃ vattabbe «Không nên nói như thế»; a question vs a statement; which side asks and which answers;
- the argument word: one Pāli word that the debate turns on must keep ONE Vietnamese word throughout the kathā (e.g. atthi «tồn tại» / natthi «không tồn tại» in the existence theses);
- complete lists and strings: nothing dropped, nothing added, order kept; …pe… = «…» and nothing expanded;
- the rebuttal pentad and the frames: the same Pāli frame reads the same everywhere.

## Translation policy and user decisions (not errors)
- **Source as written (user):** source slips are kept; only plain spelling slips and missing punctuation are rendered as meant (supplied quotes, commas). DO flag places where the Vietnamese ADDS or DROPS something the Pāli does not support (supplied subjects such as «người ta», «nó», «Ngài» are allowed only where Vietnamese needs a subject: flag any that change the meaning).
- **Approved terms:** book «Các vấn đề tranh luận»; kathā names «Bàn về …»; Āmantā «Đúng vậy.» (Āmantā? «Đúng vậy?»); Na hevaṃ vattabbe «Không nên nói như thế»; the frames and pentad of the approved sample (1-puggalakatha.md); saṃvara «sự thu thúc»; adhipati «yếu tố chủ đạo» (adhipatipaccaya «điều kiện chủ đạo»); hetupaccaya «điều kiện gốc rễ»; aggo «bậc hàng đầu»; (a)kusala kāya- / vacī- / manokamma «nghiệp (bất) thiện bằng thân / lời nói / ý»; feelings sukha / dukkha «dễ chịu» / «khó chịu», kāyika / cetasika dukkha «nơi thân» / «trong tâm», «khổ đau» / «hạnh phúc» for suffering in general and happiness; niyata «cố định»; tiṭṭheyya / tiṭṭhanti «kéo dài», tiṭṭhati «duy trì»; atthi «tồn tại» / natthi «không tồn tại» in existence theses (possessive atthi «có»); samanantara «kế cận liền ngay»; āsevanā «thực hành»; no «một» before «bậc A-la-hán» where the Pāli has no numeral; upaṭṭhāka «người thị giả»; atta «cá nhân»; pariyāpanna «nằm trong»; ruhiruppādaka «kẻ làm chảy máu»; punabbhava «sự hiện hữu mới»; names in Vietnamese form (Sê-ni-gia, Sô-ma, Diêm-ma, Tu-bạt-đà-la …).
- **Closes:** "Tassuddānaṃ –" after a vagga «Tóm tắt của chương này –»; the vagga close «Chương thứ N.»; Mahāpaṇṇāsako «Nhóm năm mươi lớn.»; Dutiyo … paṇṇāsako «Nhóm năm mươi thứ hai.» …; Tassāpi uddānaṃ «Tóm tắt của nhóm này nữa –».
- **Already listed for the user (assess briefly, give your view; do not re-report as new):** "Tassuddānaṃ –" after a fifty-group close rendered «Tóm tắt của nhóm này –» (^5-604, ^5-742, ch28, ch31); ch29 buddho tiṭṭhati / buddhā tiṭṭhanti «tồn tại»; kammaṃ karoti «làm nghiệp» vs «tạo nghiệp»; taṃ jīvaṃ taṃ sarīraṃ (sample vs pi-1 wording); bare vipāko «quả» beside dānaphala «quả của sự bố thí» (ch15); Handa hi «Bởi vì» (ch3 / ch10) vs handa «Này,» (ch16); dibbasota «tai thuộc cõi trời» vs dibbacakkhu «thiên nhãn»; uppādino / uppajjissanti both «sẽ sinh khởi» (ch7); Sakka «Sakka»; ch31 paṇṇāsakuddāna adds «năm mươi» for Mahā- / khuddaka-; «suốt một kiếp» («một» added); rūparāga / saddarāga wordplay (ch24).

## Part A: bilingual check of every segment
**1. CRITICAL: meaning errors** — a negation lost or added; Āmantā / Na hevaṃ swapped; a question rendered as a statement or the reverse where it changes the argument; the thesis word changed inside a kathā; a word, item or clause dropped or added; content on the wrong ID.
**2. MAJOR** — Vietnamese that is ungrammatical or misleading for a plain reader; a kathā name inconsistent between heading, closing line and uddāna; the same Pāli rendered inconsistently within your part, across the book, or against pi-1 … pi-4 where the Pāli is the same.
**3. MINOR** — awkward wording or register; repetition; Pāli left outside brackets.
**Typography:** "–" only where the Pāli has one; statements end with "."; questions with "?" and a Vietnamese question word; quotes “…” / ‘…’; no «….».

## Part B: comparison with the Tịnh Sự translation (meaning only)
For every segment of your part, compare on MEANING. Report only where it reveals something to check:
- a different reading that changes the meaning (polarity, which side speaks, a different sense of a word, a different construal of the thesis): check the Pāli (and commentary) and say which is right. Tịnh Sự is not the authority.
- content one has and the other lacks (beyond …pe… expansions): which is right.
- a passage where Tịnh Sự is clearly easier for a lay reader in structure: describe the structural point and propose a fix in our own words.
Do not report terminology differences where ours follows the decisions above or is another valid word.

## How to check
Read every segment. By script, compare per segment: polarity words (không, chưa, chẳng …) vs Pāli negations (na, no, natthi, a-/an- …); Āmantā / Na hevaṃ counts vs «Đúng vậy» / «Không nên nói như thế»; «?» counts; list-item counts. The debates repeat: once a frame is checked, check that its repeats match; spend the attention on the theses, the sutta quotations and the opponent's arguments.

## Report (concise, plain text, as your final message)
- Part A table: ID | file | severity | Pāli (short) | Vietnamese (short) | problem | suggested fix (our wording).
- Part B table: ID | file | kind (reading / content / clarity) | what differs (brief) | which is right and why | suggested fix to ours, or "none".
- Group repeats: where one problem recurs in many segments, give it once with the list of IDs.
- Counts per severity and kind, segments checked, and a one-paragraph overall judgement.
