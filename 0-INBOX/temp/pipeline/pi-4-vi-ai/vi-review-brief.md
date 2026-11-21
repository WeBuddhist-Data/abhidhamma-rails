# Brief: independent review of the Vietnamese Puggalapaññatti (pi-4), plain rails translation

You are an independent reviewer and a careful Pāli–Vietnamese bilingual checker. You are READ-ONLY: do not edit any translation file.
- Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: use the Read tool; run python as `python -I -X utf8`; write helper scripts with the Write tool at full paths under D:\Work\OpenPecha\abhidhamma-rails (never write any file from PowerShell).
- Put any helper scripts in 0-INBOX\temp\pipeline\pi-4-vi-ai\review\, named after your part (r1_*.py …). Never create files at the repo root, outside the repo or in a system temp folder. Never run git; never write "seed". No web.
- **Never write a file that contains Tịnh Sự text** (no dumps, no extracts, no aligned copies, no word lists from it): your scripts may read it and print to the console, nothing more.
- Do not open the termbase, the keyword maps, the word senses, the Vietnamese zero-shot, or any builder or notes in 0-INBOX\temp\pipeline\pi-4-vi-ai\ (rails\, termbase\, senses\, mapper-vi\, build_*, notes-*, agents-run.md): the point is a reading that is not anchored on them.
- Grep only the specific files named here, never whole folders.
- You cannot write report files: return your report as text.

## Inputs
- **Pāli:** AI_translation\pali\pi-4_split_chapters\<ch>.md
- **Our Vietnamese (under review):** the same filenames in AI_translation\vietnamese\pi-4-vietnamese-plain-rails_split_chapters\
- **Alignment:** segments align by the block ID at the end of each segment (e.g. ^4-112); non-empty lines align one to one.
- **Reference human translation (Tịnh Sự):** 1-SOURCES\Translations\Vietnamese\vi-4-tinh_su.md, block-aligned to the same IDs. It is COPYRIGHTED: use it only to check meaning. Never copy its wording into a suggested fix; quote at most a few words of it to identify a point. Your suggested fixes must be in our own words and our own terms.
- **Optional references** for hard readings: the English pi-4 rails AI_translation\english\pi-4-english-plain.md and the Russian AI_translation\russian\pi-4-russian-plain-rails_split_chapters\<ch>.md (by block ID); the commentaries 1-SOURCES\Commentaries\pi-puggalapannatti-atthakatha.md, pi-puggalapannatti-mulatiika.md, pi-puggalapannatti-anutiika.md. The Pāli is the authority.
- **The approved pi-1, pi-2 and pi-3 Vietnamese** (AI_translation\vietnamese\pi-1/2/3-vietnamese-plain.md): passages pi-4 shares with them (lists, jhāna and vimokkha formulas, path / fruit phrases, sīla strings, the Khuddakavatthu definitions) should match unless a decision below says otherwise; report unexplained drift as MAJOR (consistency).
- **Style:** 0-INBOX\temp\pipeline\vietnamese-style.md. **Audience:** AI_translation\audience_profile\plain.md (no Buddhist background; clear, natural, modern Vietnamese, nothing added).

## About the text
The Puggalapaññatti («Định danh các hạng người») first lists the six designations and a matrix of person types grouped by one … ten (ch1), then defines each type (ch2-11): «Thế nào là X? Ở đời này, có người … – người này được gọi là “X”.» Groups of persons are often illustrated by similes (clouds, mice, mangoes, pots, water, warriors …). Everything turns on:
- the person type: each name must be the same in the matrix, the question and the quoted name, and must render the Pāli faithfully;
- negations (na, no, a-/an-, neva … na), the "X but not Y" contrasts of the four- and five-fold groups, and which member of a pair or simile is which;
- complete lists and strings: nothing dropped, nothing added, order kept;
- the similes: each half applied to the right person.

## Translation policy and user decisions (not errors)
- **Source as written (user):** source slips are kept; only plain spelling slips and missing punctuation are rendered as meant. Known (assess briefly): ^4-176 «puratthimena narassa» rendered as written «ở phía đông của một người» (the aṭṭhakathā glosses nagarassa 'of the town': DO assess and give both readings for the user); ^4-142 samādiṭṭhi (as meant); ^4-189 a single «na» over three verbs; ^4-166 vaṇṇopi reading; ^4-202 line 6 «āgantā itthattaṃ» without «āgāmī hoti»; ^4-191 4th case lacks uppannā; ^4-109, ^4-97, ^4-100, ^4-108; ^4-M-10 (17) punctuation. DO flag places where the Vietnamese ADDS or DROPS something the Pāli does not support.
- **Terminology decisions:** book «Định danh các hạng người»; paññatti «sự định danh»; puggala «người», counted «hạng người»; the definition frame above; Kathañca puggalo X hoti? «Người như thế nào là X?», Evaṃ … «Như vậy là X.»; persons «… là những ai?», things «… là gì?»; samannāgata «được trang bị» (qualities) / «mang» (bad states); «vị ấy» for a monk, «người ấy» otherwise; abhininnāmeti «dẫn tâm»; cross-book alignments jīvita «sự sống», saṭho «người gian trá», ñāti «người thân», samanantarā «liền sau», sampavaṅkatā «sự nghiêng về phía», icchā «sự mong muốn», aggo «hàng đầu», gatiṃ «cõi tái sinh»; aṭṭhakathā «Chú giải»; purisa «đàn ông» (address «Này ông»).
- Matrix names that begin «có người» (atthi / ekacco in the matrix) drop «có» in definitions whose Pāli lacks that word (coordinator rule).

## Part A: bilingual check of every segment
**1. CRITICAL: meaning errors** — a negation lost or added; a person type, pair member or simile half swapped or wrongly applied; a wrong number; a word, item or clause dropped or added; content on the wrong ID.
**2. MAJOR** — Vietnamese that is ungrammatical or misleading for a plain reader; a person name inconsistent between matrix, question and quoted name; the same Pāli rendered inconsistently within your part, across the book, or against pi-1 / pi-2 / pi-3 where the Pāli is the same.
**3. MINOR** — awkward wording or register; repetition; Pāli left outside brackets.
**Typography:** "–" only where the Pāli has one; statements end with "."; questions with "?" and a Vietnamese question word; quotes “…” / ‘…’; no «….».

## Part B: comparison with the Tịnh Sự translation (meaning only)
For every segment of your part, compare on MEANING. Report only where it reveals something to check:
- a different reading that changes the meaning (polarity, which person, which simile half, a different sense of a word): check the Pāli (and commentary) and say which is right. Tịnh Sự is not the authority.
- content one has and the other lacks (beyond …pe… expansions): which is right.
- a passage where Tịnh Sự is clearly easier for a lay reader in structure: describe the structural point and propose a fix in our own words.
Do not report terminology differences where ours follows the decisions above or is another valid word.

## How to check
Read every segment. By script, compare per segment: polarity words (không, chưa, chẳng …) vs Pāli negations; list-item counts; the person name in matrix / question / quote (exact match). Read the similes and the definitions closely.

## Report (concise, plain text, as your final message)
- Part A table: ID | file | severity | Pāli (short) | Vietnamese (short) | problem | suggested fix (our wording).
- Part B table: ID | file | kind (reading / content / clarity) | what differs (brief) | which is right and why | suggested fix to ours, or "none".
- Counts per severity and kind, segments checked, and a one-paragraph overall judgement.
