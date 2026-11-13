# Brief: RAILS Hindi translation, plain audience (pi-7, Paṭṭhāna)

## Setup
- Work in D:\Work\OpenPecha\abhidhamma-rails.
- Windows: use the Read/Write tools for files (write scripts with the Write tool, never via a shell redirect) and PowerShell for commands; run python as `python -I -B -X utf8`.
- Other agents may translate other files in parallel. Write ONLY your own files in the output folder, plus helper scripts and notes named after your files in 0-INBOX\temp\pipeline\pi-7-hi\rails\. Never create files at the repo root or in a system temp folder. Do not touch 1-SOURCES\ or 4-SYSTEM\, and do not run git.
- Do not use the words "seed" or "unseeded" anywhere. You cannot write report files for me: return your report as text.

## Read first
- AI_translation\skills\rails-verse-translator.md. Follow it.
- 0-INBOX\temp\pipeline\hindi-style.md: register, typography, dash rule, structure.
- **Approved pi-7 frames (binding for sentence shape):**
  - 0-INBOX\temp\pipeline\pi-7-hi\hi-zeroshot-terms.md: the book title «कारण-संबंध», the division and section headings, the 24 condition names in every case form, the paṭicca / sahajāta / paccaya / nissaya / saṃsaṭṭha / sampayutta frames, the pañhāvāra frame, the Siyā question frame («क्या … उत्पन्न हो सकती है?», user-approved even where the Pāli ends with "."), the counting frames. Copy them verbatim. Where one of its WORDS differs from the termbase, the termbase wins.
  - 0-INBOX\temp\pipeline\pi-7-hi\harmonise-notes.md: the triad and dyad names and the forms the harmonise pass fixed (Paccanīyuddhāro, labels, moment words, ghaṭanā, closing lines «… समाप्त।»).
- Translate FRESH from the Pāli, consulting the locked termbase term by term.
- Do NOT open the pi-7 zero-shot Hindi (AI_translation\hindi\pi-7-hindi-plain-zeroshot_split_chapters\, pi-7-hindi-plain-zeroshot.md), the build_*_hi.py builders, the notes-*.md files, or the pi-7 Hindi keyword map.
- **Models of house style:** the approved rails Hindi of pi-1 (AI_translation\hindi\pi-1-hindi-plain-rails_split_chapters\, especially 1-matika.md for the triad and dyad items), pi-2 and pi-6 (same folders pattern; line-aligned with AI_translation\pali\pi-N_split_chapters\). Where the Pāli is the same, reuse their wording, EXCEPT where the pi-7 termbase deliberately differs: then the pi-7 termbase wins.

## Inputs
- **Source:** AI_translation\pali\pi-7_split_chapters\<f>.md
- **Locked termbase (authoritative, approved by the user 2026-11-13):** AI_translation\hindi\pi-7-pali-hindi-termbase-plain.md, in the form `pali: {english tag: हिंदी; …}`.
  - Look up each Pāli word; pick the sense by its tag. Compounds and phrases often have their own entries; a compound without an entry is built from its members' entries.
  - Inflect grammatically (number, gender, oblique case, verb agreement), but never swap in a synonym. Terms are in dictionary form.
  - If no sense fits, use the closest sibling entry and REPORT it.
- **Deliberate pi-7 choices (approved, binding):** paccaya = «कारण» and the 24 conditions «X-कारण» (hetu «मूल-कारण» … avigata «अविलीनता-कारण»); positive ablative «X-कारण से», negative ablative «X-कारण के बिना», negative noun «X-कारण का अभाव», count locative «X-कारण में»; pañhāvāra «… के लिए X-कारण के रूप में कारण होती है»; paṭicca «… पर निर्भर होकर»; vipāka (adjective) = «कर्म-फल रूपी» everywhere; uppanna «उत्पन्न हो चुका»; niṭṭhita «समाप्त»; triad and dyad names «X वाला तीन/दो का वर्गीकरण». The full list of differences from earlier books is 0-INBOX\temp\pipeline\pi-7-hi\termbase\cross-book-differences.md.
- Core: dhamma = परिघटना; kusala/akusala = हितकर/हानिकर; abyākata = नैतिक रूप से अनिर्धारित; khandha = समूह; mātikā = मूल सूची. The termbase's "no comma inside a term" is a file-format rule, not punctuation: Hindi sentences take normal commas.
- **Sentence formulas (authoritative for sentence shape):** 0-INBOX\temp\pipeline\pi-7-hi\rails\hi-rails-formulas.md. The sample agent creates it; it is read-only for everyone else. Any NEW recurring formula goes in your notes file rails\notes-<files>.md.
- **Audience:** AI_translation\audience_profile\plain.md
- **Helper:** the Paṭṭhāna is almost entirely formulaic. Use a builder script with fixed formula strings so identical Pāli gets identical Hindi, but only after reading the segments; read your output for sense.
- **Source slips: translate the Pāli exactly as written** (user rule: no emendations unless the source data is updated). Only pure spelling slips are rendered as the word meant; agreement slips stay grammatical Hindi. List slips in your report; never fix them.

## The sample (scope)
- AI_translation\hindi\pi-7-hindi-plain-rails_split_chapters\preamble.md and 1-00-paccaya.md (complete).
- 1-01-kusalattika.md non-empty lines 1–190 (the dependent section, positive and negative) and 1235–1262 (the start of the question section), written as sample-1\1-01-a-sample.md / 1-01-a-pali-sample.md (lines 1–190) and sample-1\1-01-b-sample.md / 1-01-b-pali-sample.md (lines 1235–1262) in 0-INBOX\temp\pipeline\pi-7-hi\rails\ (Pāli copied exactly).
- The sample agent writes rails\hi-rails-formulas.md (every recurring string of the sample, plus the frames of the later sections and divisions as "(not yet in the sample)" lines) and rails\build_rails_sample.py holding the same strings as Python constants (importable without side effects: guard the build under `if __name__ == "__main__":`).
- After the user approves the sample, it is the model for everything: other agents import build_rails_sample.py read-only and copy hi-rails-formulas.md verbatim.

## Output
AI_translation\hindi\pi-7-hindi-plain-rails_split_chapters\<f>.md, one file per Pāli file.

## Rules
- **Block IDs:** exact, at the end of the last line of each segment, in the same order.
- **Headings:** keep their #-level and *…* italics.
- **Segments:** each has the source's number of non-empty lines. One blank line between segments; no double blank lines; no CR characters.
- **DASH RULE (user):** "–" only where the Pāli has "–" or "—", at the same spot, with the same count on every line. Never add a dash, and never use ":-".
- **Punctuation:** "…pe…" becomes "…". Statements end with «।», questions «?». Quotes are “…” / ‘…’.
- **Brackets:** Pāli {…} variants become «[वर्तनी-भेद (…): <Pāli>]» for spelling-only variants, «[पाठभेद (…): <Pāli>]» otherwise; untagged {…} notes «[पाठभेद: <Pāli>]»; never translate bracket contents. (Ka)/(Kha)… → (क)/(ख)…. Digits and count markers like "(3)" stay.
- **Formulas:** identical Pāli gets identical Hindi. Where the Pāli of two segments differs only by an item, a condition, a number or a variant bracket, the Hindi differs only there.

## Verify each file (all must pass)
```
python -I 0-INBOX\temp\pipeline\check_chapter_ids.py AI_translation\pali\pi-7_split_chapters AI_translation\hindi\pi-7-hindi-plain-rails_split_chapters <f>.md
python -I -X utf8 0-INBOX\temp\pipeline\pi-1-en\dashcheck.py AI_translation\pali\pi-7_split_chapters\<f>.md AI_translation\hindi\pi-7-hindi-plain-rails_split_chapters\<f>.md
python -I -X utf8 0-INBOX\temp\pipeline\pi-1-hi\verify_hi.py AI_translation\pali\pi-7_split_chapters\<f>.md AI_translation\hindi\pi-7-hindi-plain-rails_split_chapters\<f>.md
```
verify_hi may flag only the expected kinds: bracket counts where the Pāli uses {…}, and "?" on Siyā lines. Also confirm no double blank lines and no Latin-script words outside variant brackets. Then run termbase adherence (it checks only the segments present in the folder):
```
python -I -X utf8 0-INBOX\temp\pipeline\hindi_termbase_adherence.py AI_translation\pali\pi-7-keywords-by-reference-pali-plain.md AI_translation\hindi\pi-7-pali-hindi-termbase-plain.md AI_translation\hindi\pi-7-hindi-plain-rails_split_chapters
```
Fix genuine misses. Inflection and split phrases cause false misses, so read the misses with judgement.

## Final report (short)
- Per file: checks passed and segment count; adherence result.
- New formulas.
- Termbase misfits (term, segment, why it does not fit, what you wrote).
- Source slips (translated as written) and unsure Pāli.
