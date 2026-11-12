# Brief: independent review of the Marathi Kathāvatthu (pi-5, «चर्चेचे विषय»)

You are an independent reviewer and a careful Pāli–Marathi bilingual checker. You are READ-ONLY: do not create, edit or delete any file.
- Work in /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails on macOS (zsh). Use the Read tool, Grep/Glob and Bash.
- Run any check scripts inline only, as `/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 - <<'EOF' … EOF` heredocs, without writing files (plain python3 is too old).
- Do NOT open the Marathi termbase, the senses or keyword files, the zero-shot Marathi, or any notes or scripts in 0-INBOX: review the translation against the Pāli on its own.
- Never use the words "seed" or "unseeded" in your report.

## Inputs
- **Pāli:** AI_translation/pali/pi-5_split_chapters/<ch>.md
- **Marathi:** the same filenames in AI_translation/marathi/pi-5-marathi-plain-rails_split_chapters/
- **Alignment:** segments align by the block ID at the end of each segment (e.g. ^5-112), and lines align one to one within a segment.
- **Optional reference** for hard readings: the English rails AI_translation/english/pi-5-english-plain-rails_split_chapters/<same file>. The Pāli is the authority.
- **Audience:** AI_translation/audience_profile/plain.md. The reader has no Buddhist background, so the Marathi must be clear, natural, modern standard Marathi, with nothing added.

## About the text
The Kathāvatthu is a book of debates. Each kathā tests one thesis in fixed frames: the proponent asks «P-ti? Āmantā.», then «Q-ti? Na hevaṃ vattabbe.», then the refutation «Ājānāhi niggahaṃ. Hañci P, tena vata re vattabbe – "Q"ti. Yaṃ tattha vadesi – "vattabbe kho – ‘P’, no ca vattabbe – ‘Q’"ti micchā.» and its converse «No ce pana vattabbe – …». Many arguments also quote suttas («Nanu vuttaṃ bhagavatā – "…"ti? Āmantā. Tena hi …»). Everything turns on:
- polarity: «Āmantā» (हो), «Na hevaṃ vattabbe» (असे म्हणू नये), «na / no / nupalabbhati» negations, and which side each proposition stands on; a lost or added negation flips the argument;
- that the proposition P and the counter-proposition Q stay the same, word for word, through every frame of the same argument;
- exact numbers and lists (the six senses, the aggregates, the four paths and fruits …): no item lost, added or swapped;
- the right speaker side ([…पक्षाचा प्रश्न] markers) and the right quote level (“…” outer, ‘…’ inner, the third level unquoted as in the Pāli).

## Known conventions you should NOT report as errors
- «…pe…» becomes «…», with one space after «…» before a word.
- Statements end with «.», never «।». Quotes are “…” / ‘…’.
- The frames are fixed: Āmantā = «हो.»; Na hevaṃ vattabbe = «असे म्हणू नये.»; Ājānāhi niggahaṃ = «खंडन स्वीकार कर.»; Hañci … tena vata re vattabbe = «जर …, तर नक्कीच असे म्हणायला हवे – “…”»; Yaṃ tattha vadesi … micchā = «याबाबत तू जे म्हणतोस – “…”, ते चुकीचे आहे.»; Nanu vuttaṃ bhagavatā = «भगवानांनी असे सांगितले नाही का?» or close variants; Tena hi = «तर मग».
- «काय» opens a yes/no question; «काय,» (with a comma) only right after an answer (हो. / असे म्हणू नये. / नाही.).
- Book titles outside citation brackets are Marathi only («चर्चेचे विषय», «घटनांची गणना», «व्यक्तींचे वर्णन» …). Inside citation brackets the canon reference stays a reference in Pāli names written in Marathi script, with numbers: «[पुग्गलपञ्ञत्ति मातिका 4.24; अंगुत्तर निकाय 4.95-96]», «[धम्मसंगणी तिकमातिका …]».
- Variant brackets keep the Pāli reading: «[पाठभेद (Sī.): …]» for a different word, «[लेखनभेद (Syā.): …]» for spelling only.
- Fixed vocabulary choices (report only if the meaning is wrong in context): व्यक्ती (puggala), खरी आणि परम वस्तुस्थिती / खऱ्या आणि परम अर्थाने (saccikaṭṭha paramaṭṭha), आढळते (upalabbhati), खंडन (niggaha), समूह (khandha), इंद्रिय-क्षेत्र (āyatana), तत्त्व (dhātu), क्षमता (indriya as faculty), घटना (dhamma as phenomena), शिकवण (dhamma as teaching), मनाचे मळ (āsava), ध्यान-प्राप्ती (samāpatti), सजगता (sati), प्रज्ञा (paññā), अनिर्मित (asaṅkhata), मार्ग / फळ (magga / phala), लोप पावण्याची ध्यान-प्राप्ती (nirodhasamāpatti), निश्चित मार्ग (niyāma).
- Source slips are translated as written and are known: ^5-270 «Āmantā?» (हो?), ^5-321 stray quote, ^5-365 last answer kept as written, ^5-377 / ^5-360 / ^5-361 spelling slips, ^5-503 surā/asurā, ^5-525 rūpadhātuyā with variant, ^5-581 missing opening quote (balanced in Marathi), ^5-693, ^5-704, ^5-721 to ^5-741 missing quotes or commas (normalised).

## Check every segment for

**1. CRITICAL: meaning errors**
- a polarity error: a negation lost or added; Āmantā and Na hevaṃ vattabbe swapped; P and Q swapped in a frame;
- a proposition that changes wording between frames of the same argument in a way that changes its meaning;
- a wrong number, or a list item lost, added or swapped;
- a sutta quotation mistranslated;
- omitted or added content (beyond «…» for …pe…), e.g. a word added that the Pāli does not have;
- content placed on the wrong ID; a kathā heading, its «… niṭṭhitā.» colophon and the vagga summary (uddāna) naming it differently.

**2. MAJOR**
- Marathi that is ungrammatical or misleading, so that a reader would likely misread it (gender and number agreement, verb forms, case endings, the question/answer shape).
- The same Pāli formula, sentence or term rendered inconsistently within your part.

**3. MINOR**
- awkward wording or register; a rare or heavy word where a plain one exists;
- Pāli left in Latin script outside variant brackets.

**Also check typography:** dashes «–»/«—» only where the Pāli has them, same count per line; no «।»; no double blank lines.

## How to check
The book is large: verify the first instance of each frame and each kathā carefully, then scan later segments for deviations. Check BY SCRIPT, per line: the numbers (Pāli and Marathi number words and digits mapped to integers), the dash counts, and polarity (per line, compare the count of Āmantā vs «हो», Na hevaṃ vattabbe vs «असे म्हणू नये», and of Pāli negations na / no / nupalabbhati / a-/an- forms you can detect against Marathi नाही / नये / न / नसते …; use it to find lines to read closely). Then read closely every sutta quotation, every list, every kathā opening and every line the scripts flag. Spread your close reading over all your chapters, not only the first one.

## Report (concise, as your final message: you cannot write files)
- A table: ID | file | severity | Pāli (short) | Marathi (short) | problem | suggested Marathi fix (the full corrected Marathi phrase).
- If the same problem recurs, give one row with the pattern and list the IDs (or the count).
- Then the counts per severity, the number of segments checked, the script results (number, polarity and dash mismatches), and a one-paragraph overall judgement.
