# Brief: RAILS Hindi translation, plain audience (pi-2, Vibhaṅga)

## Setup
- Work in D:\Work\OpenPecha\abhidhamma-rails.
- Windows: use the Read/Write tools for files and PowerShell for commands; run python as `python -I -X utf8`; write helper scripts to files (inline `python -c` with regexes breaks in PowerShell).
- Other agents may translate other chapters in parallel. Write ONLY your own chapter files in the output folder, plus helper scripts and notes named after your chapters in 0-INBOX\temp\pipeline\pi-2-hi\rails\. Never create files at the repo root. Do not touch 1-SOURCES\ or 4-SYSTEM\, and do not run git.
- Do not use the words "seed" or "unseeded" anywhere.

## Read first
- AI_translation\skills\rails-verse-translator.md. Follow it.
- 0-INBOX\temp\pipeline\hindi-style.md: register, typography, dash rule, structure.
- 0-INBOX\temp\pipeline\pi-2-hi\hi-zeroshot-terms.md: ONLY its book title («विस्तृत विश्लेषण»), the 18 chapter headings («X का विश्लेषण»), the section headings (उपदेशों के अनुसार विश्लेषण / अभिधम्म के अनुसार विश्लेषण / प्रश्नोत्तर), the closing lines and the Niddesa heading form «… की व्याख्या». The user approved these titles; copy them verbatim. Ignore its other terms where they conflict with the termbase: the termbase wins.
- Translate FRESH from the Pāli, consulting the locked termbase term by term.
- Do NOT open the pi-2 zero-shot Hindi (AI_translation\hindi\pi-2-hindi-plain-zeroshot_split_chapters\, pi-2-hindi-plain-zeroshot.md), the build_*_hi.py builders, or the pi-2 Hindi keyword map.
- **pi-1 rails Hindi is the main model** (final, reviewed by the user): AI_translation\hindi\pi-1-hindi-plain-rails_split_chapters\ (lines align one to one with AI_translation\pali\pi-1_split_chapters\). The Vibhaṅga repeats many pi-1 formulas (matrix triads/dyads in the Abhidhammabhājanīya and Pañhāpucchaka sections, mind-state lists, factor synonym strings, jhāna formulas, question/answer frames). Where the Pāli is identical to pi-1, reuse the pi-1 rails wording, except where the pi-2 termbase deliberately differs (see below): then the pi-2 termbase wins. Grep the Pāli in pi-1, read the same line in the Hindi.
- Other finished Hindi rails books (AI_translation\hindi\pi-3-hindi-plain.md, pi-4-hindi-plain.md, pi-5-hindi-plain.md) are models of house style only. Where they disagree with the pi-2 termbase, the pi-2 termbase wins.

## Inputs
- **Source:** AI_translation\pali\pi-2_split_chapters\<ch>.md
- **Locked termbase (authoritative, approved by the user 2026-11-12):** AI_translation\hindi\pi-2-pali-hindi-termbase-plain.md, in the form `pali: {english tag: हिंदी; …}`.
  - Look up each Pāli word; pick the sense by its tag. Compounds and phrases often have their own entries; a compound without an entry is built from its members' entries.
  - Inflect grammatically (number, gender, oblique case, verb agreement), but never swap in a synonym. Terms are in dictionary form.
  - If no sense fits, use the closest sibling entry and REPORT it.
- **Deliberate pi-2 choices that differ from pi-1/3/4/5 (approved, binding):** parakkama = पराक्रम (kept apart from padhāna = प्रयत्न and vāyāma = प्रयास; parakkamati stays «प्रयत्न करना»); paṭipadā = «प्रगति का ढंग»; dukkha/sukha in compounds = दुःख/सुख; rūpa as a sphere = «सूक्ष्म भौतिक लोक», arūpa = «अभौतिक लोक»; bhāveti = «अभ्यास करना», āsevati = «निरंतर सेवन करना», bahulīkaroti = «बार-बार करना»; samannāgata = «युक्त»; samāpatti = «ध्यान-अवस्था»; duccarita = «शरीर/वाणी/मन का दुराचरण»; kilesa = «मन के क्लेश»; acetasika = «मन का सहचर न होने वाला»; vipāka = «कर्म-फल रूपी». The full list is 0-INBOX\temp\pipeline\pi-2-hi\termbase\cross-book-differences.md.
- Binding conventions carried over from the pi-1 rails review:
  - The termbase's "no comma inside a term" is a file-format rule, not punctuation. Hindi sentences take normal commas: «न X, न Y», «X, पर Y», and commas in lists.
  - vipāka after हितकर/हानिकर = «हितकर कर्म के फल रूपी …», «हानिकर कर्म के फल रूपी …».
  - Core: dhamma = परिघटना (the Teaching = शिक्षा); kusala/akusala = हितकर/हानिकर; abyākata = नैतिक रूप से अनिर्धारित; khandha = समूह; mātikā = मूल सूची; sammappadhāna = सही प्रयत्न; vīriya = उत्साह; vāyāma = प्रयास.
- **Sentence formulas (authoritative for sentence shape):** 0-INBOX\temp\pipeline\pi-2-hi\rails\hi-rails-formulas.md. The sample agent creates it; it is read-only for everyone else. Any NEW recurring formula goes in your notes file rails\notes-<chapters>.md.
- **Audience:** AI_translation\audience_profile\plain.md
- **Helper:** a builder script with fixed formula strings guarantees identical Hindi for identical Pāli. The Vibhaṅga is highly repetitive (the aggregate formulas, the past/future/present, own/others', coarse/subtle, inferior/superior, far/near strings, the matrix question/answer frames), so use one.

## The approved sample (user-approved 2026-11-12): read it first, it is the model for everything
- AI_translation\hindi\pi-2-hindi-plain-rails_split_chapters\preamble.md (done; do not rewrite it).
- 0-INBOX\temp\pipeline\pi-2-hi\rails\sample-1\1-sample.md: chapter 1 through ^2-33 (line-aligned with sample-1\1-pali-sample.md).
- 0-INBOX\temp\pipeline\pi-2-hi\rails\hi-rails-formulas.md: every string in it is binding, copy it verbatim (including the "(not yet in the sample)" lines). 0-INBOX\temp\pipeline\pi-2-hi\rails\build_rails_sample.py holds the same strings as Python constants; import it instead of retyping them (`sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-hi\rails"); import build_rails_sample as S`; import only, never edit or run it).
- Words without a termbase entry, as fixed in the sample (reuse them): niyaka «उन्हीं का/की»; āsanne «निकट», anāsanne «निकट नहीं», upakaṭṭhe «समीप», anupakaṭṭhe «समीप नहीं», avidūre «दूर नहीं», asantike «पास नहीं»; hīnasammata / paṇītasammata «आम तौर पर हीन / उत्तम माना गया»; samuppanna «भली-भाँति उत्पन्न»; sukhasamphassa / dukkhasamphassa «सुख-संपर्क वाला / दुःख-संपर्क वाला»; santike «पास».
- **Matrix (mātikā) triads and dyads** in the Abhidhammabhājanīya and Pañhāpucchaka sections: use the item names of the approved pi-1 rails AI_translation\hindi\pi-1-hindi-plain-rails_split_chapters\1-matika.md and pi-1's rails question/answer frames (Katame dhammā X? / ime dhammā X; siyā …; na vattabbā …), except where a pi-2 termbase choice differs (then inflect the pi-2 term into the same frame). One shape per frame across the book.

## Output
AI_translation\hindi\pi-2-hindi-plain-rails_split_chapters\<ch>.md. Long chapters may be built in parts and joined, but the final file must be complete.

## Rules
- **Block IDs:** exact, at the end of the last line of each segment, in the same order (including the odd ^2-U… IDs).
- **Headings:** keep their #-level.
- **Segments:** each has the source's number of non-empty lines. One blank line between segments; no double blank lines; no CR characters.
- **DASH RULE (user):** "–" only where the Pāli has "–" or "—", at the same spot, with the same count on every line. Never add a dash, and never use ":-".
- **Punctuation:** "…pe…" becomes "…". Statements end with «।». Quotes are “…” / ‘…’.
- **Brackets:** «[वर्तनी-भेद (Sī., Syā.): <Pāli>]» for spelling-only variants, «[पाठभेद (…): <Pāli>]» otherwise; (Ka)/(Kha)/(Ga) → (क)/(ख)/(ग). Digits in the Pāli stay as digits.
- **Formulas:** identical Pāli gets identical Hindi. Where the Pāli of two segments differs only by a variant bracket or a numeral, the Hindi differs only there.
- **Readability for a plain reader:** the long -pe- runs and abbreviated lists must still read as Hindi sentences. Where a literal string reads badly, recast the sentence while keeping every term.

## Verify each chapter (all must pass)
```
python -I 0-INBOX\temp\pipeline\check_chapter_ids.py AI_translation\pali\pi-2_split_chapters AI_translation\hindi\pi-2-hindi-plain-rails_split_chapters <ch>.md
python -I -X utf8 0-INBOX\temp\pipeline\pi-1-en\dashcheck.py AI_translation\pali\pi-2_split_chapters\<ch>.md AI_translation\hindi\pi-2-hindi-plain-rails_split_chapters\<ch>.md
python -I -X utf8 0-INBOX\temp\pipeline\pi-1-hi\verify_hi.py AI_translation\pali\pi-2_split_chapters\<ch>.md AI_translation\hindi\pi-2-hindi-plain-rails_split_chapters\<ch>.md
```
Also confirm no double blank lines and no Latin-script words outside variant brackets. Then run termbase adherence (it checks only the segments present in the folder):
```
python -I -X utf8 0-INBOX\temp\pipeline\hindi_termbase_adherence.py AI_translation\pali\pi-2-keywords-by-reference-pali-plain.md AI_translation\hindi\pi-2-pali-hindi-termbase-plain.md AI_translation\hindi\pi-2-hindi-plain-rails_split_chapters
```
Fix genuine misses. Inflection and split phrases cause false misses, so read the misses with judgement.

## Final report (short)
- Per chapter: checks passed and segment count; adherence result.
- New formulas.
- Termbase misfits (term, segment, why it does not fit, what you wrote).
- Unsure Pāli or source slips.
