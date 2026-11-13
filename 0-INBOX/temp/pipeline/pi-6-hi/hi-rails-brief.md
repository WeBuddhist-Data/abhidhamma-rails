# Brief: RAILS Hindi translation, plain audience (pi-6, Yamaka)

## Setup
- Work in D:\Work\OpenPecha\abhidhamma-rails.
- Windows: use the Read/Write tools for files and PowerShell for commands; run python as `python -I -X utf8`; write helper scripts to files (inline `python -c` with regexes breaks in PowerShell).
- Other agents may translate other files in parallel. Write ONLY your own chapter files in the output folder, plus helper scripts and notes named after your files in 0-INBOX\temp\pipeline\pi-6-hi\rails\. Never create files at the repo root or in a system temp folder. Do not touch 1-SOURCES\ or 4-SYSTEM\, and do not run git.
- Do not use the words "seed" or "unseeded" anywhere.

## Read first
- AI_translation\skills\rails-verse-translator.md. Follow it.
- 0-INBOX\temp\pipeline\hindi-style.md: register, typography, dash rule, structure.
- **Approved pi-6 frames (binding for sentence shape):**
  - 0-INBOX\temp\pipeline\pi-6-hi\hi-zeroshot-terms.md: the book title «प्रश्नों के जोड़े», the ten chapter headings «X पर प्रश्नों के जोड़े», all section headings (खंड, विधि, सूची, व्याख्या, सकारात्मक/नकारात्मक/विपरीत, «सकारात्मक: व्यक्ति» etc.), the closing lines, the question and answer frames, the being/place/moment phrases and the process-verb table. The user approved these; copy them verbatim. Where one of its WORDS differs from the termbase, the termbase wins.
  - 0-INBOX\temp\pipeline\pi-6-hi\harmonise-notes.md, the "Decisions" table only (columns Rule/Decision; ignore the builder column): sense-organ beings «आँख वाले / आँख से रहित» joined with « और »; «चार या पाँच समूहों वाले अस्तित्व»; sota = «दिव्य कान और तृष्णा की धारा, कान हैं»; Natthi = «ऐसा कोई नहीं है।»; «X से मरने वालों में»; «X में अंतिम जन्म लेने वालों में»; «सभी के मन के … होने के क्षण में»; every being/place chunk keeps «में» and the last chunk is joined with « और »; the pariññā/pajahana/bhāvanā questions «(क) जो व्यक्ति …, क्या वह …?» (past «जिस व्यक्ति ने …, क्या उसने …?»); bare raso = «स्वाद»; the note formulas (यस्सक «व्यक्ति वाला भाग» …, «का विस्तार करना चाहिए», «चक्र पूरा करना चाहिए», «संक्षिप्त किया गया है», «बिना भ्रम के»).
- Other approved answer forms: Āmantā = «हाँ।»; No = «नहीं।». "no ca … nuppajjati" (and every "no ca … na V") is rendered as a positive: «पर उनमें Y उत्पन्न होता है». In the term-checking (padasodhana/paṇṇatti) pairs, bare words stay bare (rūpaṃ «रूप», saṅkhārā «रचनाएँ», cakkhu «आँख») while the khandha/āyatana/dhātu/indriya names take the full term. hetu = «हेतु» only in the ten-names list; elsewhere a root is मूल.
- Translate FRESH from the Pāli, consulting the locked termbase term by term.
- Do NOT open the pi-6 zero-shot Hindi (AI_translation\hindi\pi-6-hindi-plain-zeroshot_split_chapters\, pi-6-hindi-plain-zeroshot.md), the build_*_hi.py / common_*_hi.py builders, the notes-*.md files, or the pi-6 Hindi keyword map.
- **Models of house style:** the approved rails Hindi of pi-2 (AI_translation\hindi\pi-2-hindi-plain-rails_split_chapters\, line-aligned with AI_translation\pali\pi-2_split_chapters\) and pi-1 (pi-1-hindi-plain-rails_split_chapters\). They hold the aggregate, sense-base, element, truth, faculty, dependent-origination and latent-tendency names and the kusala/akusala/abyākata frames. Where the Pāli is the same, reuse their wording, EXCEPT where the pi-6 termbase deliberately differs (below): then the pi-6 termbase wins. pi-3/4/5 rails Hindi are models of house style only.

## Inputs
- **Source:** AI_translation\pali\pi-6_split_chapters\<f>.md
- **Locked termbase (authoritative, approved by the user 2026-11-12):** AI_translation\hindi\pi-6-pali-hindi-termbase-plain.md, in the form `pali: {english tag: हिंदी; …}`.
  - Look up each Pāli word; pick the sense by its tag. Phrases (the being phrases, places, moments) often have their own entries; a compound without an entry is built from its members' entries.
  - Inflect grammatically (number, gender, oblique case, verb agreement), but never swap in a synonym. Terms are in dictionary form.
  - If no sense fits, use the closest sibling entry and REPORT it.
- **Deliberate pi-6 choices that differ from pi-1/2/3/4/5 (approved, binding):** the spheres as places «इंद्रिय-सुखों का लोक», «सूक्ष्म भौतिक लोक», «अभौतिक लोक» (and their beings «… के प्राणी»), not «… से संबंधित»; catutthajjhāna = «ध्यान की चौथी अवस्था» (likewise the other jhānas as attested in the termbase); indriya = «क्षमता», cakkhundriya = «आँख की क्षमता» (not «इंद्रिय»); kusalahetū = «हितकर हेतु»; uddeso = «सूची»; natthi = «ऐसा कोई नहीं»; taṇhāsota = «तृष्णा की धारा»; uppanna = «उत्पन्न हो चुका»; sarāga = «राग-युक्त»; okāsa = «स्थान»; puggala = «व्यक्ति». The full list is 0-INBOX\temp\pipeline\pi-6-hi\termbase\cross-book-differences.md.
- Binding conventions carried over from the pi-1/pi-2 rails review:
  - The termbase's "no comma inside a term" is a file-format rule, not punctuation. Hindi sentences take normal commas.
  - Core: dhamma = परिघटना (the Teaching = शिक्षा); kusala/akusala = हितकर/हानिकर; abyākata = नैतिक रूप से अनिर्धारित; khandha = समूह; mātikā = मूल सूची; nāma = मानसिक पक्ष.
- **Sentence formulas (authoritative for sentence shape):** 0-INBOX\temp\pipeline\pi-6-hi\rails\hi-rails-formulas.md. The sample agent creates it; it is read-only for everyone else. Any NEW recurring formula goes in your notes file rails\notes-<files>.md.
- **Audience:** AI_translation\audience_profile\plain.md
- **Helper:** the Yamaka is almost entirely formulaic (question pairs, person/place/both frames in six tenses, positive and negative). Use a builder script with fixed formula strings so identical Pāli gets identical Hindi, but only after reading the segments; every output line must be read for sense.

## The sample (scope)
- AI_translation\hindi\pi-6-hindi-plain-rails_split_chapters\preamble.md (from AI_translation\pali\pi-6_split_chapters\preamble.md).
- 1-mulayamaka.md, complete.
- 2-01-khandhayamaka.md from the start through the end of «(1) Paccuppannavāro» of the uppādavāra (the Paṇṇattivāra in full, then the present-tense section with all six person/place frames; Pāli lines 1-638, ending with ^6-2-55, just before «(2) Atītavāro ^6-2-13-0»), written as sample-1\2-01-sample.md with the matching Pāli in sample-1\2-01-pali-sample.md, both in 0-INBOX\temp\pipeline\pi-6-hi\rails\.
- The sample agent writes rails\hi-rails-formulas.md (every recurring string of the sample, plus the frames of the later tenses and the nirodha/uppādanirodha sections as "(not yet in the sample)" lines) and rails\build_rails_sample.py holding the same strings as Python constants.
- After the user approves the sample, it is the model for everything: other agents import build_rails_sample.py read-only (`sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-hi\rails"); import build_rails_sample as S`; never edit or run it) and copy hi-rails-formulas.md verbatim.

## Output
AI_translation\hindi\pi-6-hindi-plain-rails_split_chapters\<f>.md, one file per Pāli file. Long files may be built in parts and joined, but the final file must be complete.

## Rules
- **Block IDs:** exact, at the end of the last line of each segment, in the same order.
- **Headings:** keep their #-level.
- **Segments:** each has the source's number of non-empty lines. One blank line between segments; no double blank lines; no CR characters.
- **DASH RULE (user):** "–" only where the Pāli has "–" or "—", at the same spot, with the same count on every line. Never add a dash, and never use ":-".
- **Punctuation:** "…pe…" becomes "…". Questions end «?», statements «।». The quotative -ti is dropped. Quotes are “…” / ‘…’.
- **Brackets:** «[वर्तनी-भेद (Ka.): <Pāli>]» for spelling-only variants, «[पाठभेद (…): <Pāli>]» otherwise; (Ka)/(Kha)/(Ga)/(Gha)/(Ṅa)/(Ca) → (क)/(ख)/(ग)/(घ)/(ङ)/(च). Digits in the Pāli stay as digits.
- **Formulas:** identical Pāli gets identical Hindi. Where the Pāli of two segments differs only by a term, a tense, a polarity, a variant bracket or a numeral, the Hindi differs only there.
- **Readability for a plain reader:** long being/place chains and abbreviated answers must still read as Hindi sentences. Where a literal string reads badly, recast the sentence while keeping every term.

## Verify each file (all must pass)
```
python -I 0-INBOX\temp\pipeline\check_chapter_ids.py AI_translation\pali\pi-6_split_chapters AI_translation\hindi\pi-6-hindi-plain-rails_split_chapters <f>.md
python -I -X utf8 0-INBOX\temp\pipeline\pi-1-en\dashcheck.py AI_translation\pali\pi-6_split_chapters\<f>.md AI_translation\hindi\pi-6-hindi-plain-rails_split_chapters\<f>.md
python -I -X utf8 0-INBOX\temp\pipeline\pi-1-hi\verify_hi.py AI_translation\pali\pi-6_split_chapters\<f>.md AI_translation\hindi\pi-6-hindi-plain-rails_split_chapters\<f>.md
```
(For the partial 2-01 sample, run dashcheck and verify_hi on sample-1\2-01-pali-sample.md against sample-1\2-01-sample.md.)
Also confirm no double blank lines and no Latin-script words outside variant brackets. Then run termbase adherence (it checks only the segments present in the folder):
```
python -I -X utf8 0-INBOX\temp\pipeline\hindi_termbase_adherence.py AI_translation\pali\pi-6-keywords-by-reference-pali-plain.md AI_translation\hindi\pi-6-pali-hindi-termbase-plain.md AI_translation\hindi\pi-6-hindi-plain-rails_split_chapters
```
Fix genuine misses. Inflection and split phrases cause false misses, so read the misses with judgement.

## Final report (short)
- Per file: checks passed and segment count; adherence result.
- New formulas.
- Termbase misfits (term, segment, why it does not fit, what you wrote).
- Unsure Pāli or source slips.
