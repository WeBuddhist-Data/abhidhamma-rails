# Brief: Pāli→Marathi keyword mapping (pi-3)

**Setup.**
- Work in /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails. macOS (zsh): use the Read/Write tools for files and run Python as `python3 -I -X utf8`; write helper scripts to files, not inline `-c` with regexes.
- Other agents map other chapters in parallel. Write ONLY your own mapped files, plus helper scripts named after your chapters, inside 0-INBOX/temp/pipeline/pi-3-mr/mapper-mr/. Never use the system temp directory. Don't commit.

**Read first.**
- AI_translation/skills/keyword-equivalence-mapper.md (the skill you execute).
- 0-INBOX/temp/pipeline/marathi-style.md (the Marathi conventions and core terms).
- 0-INBOX/temp/pipeline/pi-3-mr/harmonise-notes.md, especially the final "Pāli = Marathi" table and the "User decisions" section: these are the forms the translation uses.
- **The user-approved sample (binding conventions):** 0-INBOX/temp/pipeline/pi-3-mr/mapper-mr/map_sample.py and its outputs preamble.mapped.md, 1-uddeso.mapped.md, 2-pathamanayo.sample.mapped.md, plus map-sample-table.md. Reuse its table: import or copy `T`, `SENSE`, `VIN` and the helper logic into your own script, and keep every value it gives for the same keyword in the same kind of segment.

**Per chapter <ch> (scratch 0-INBOX/temp/pipeline/pi-3-mr/mapper-mr/):**
- **Keywords:** <ch>.keywords.md, in the form `[id] kw1, kw2, ...` (Pāli).
- **Marathi translation (the CURRENT, harmonised text):** AI_translation/marathi/pi-3-marathi-plain-zeroshot_split_chapters/<ch>.md. Segments end with ^id.
- **Pāli source, for context:** AI_translation/pali/pi-3_split_chapters/<ch>.md.
- **Output:** <ch>.mapped.md. Same lines, same order, the same keywords in the same order, each written `pali=मराठी`.
- **Conventions reference for hard cases:** the user-approved Hindi mapping of the same book, AI_translation/hindi/pi-3-keywords-by-reference-pali-hindi-plain.md. Use it to see how fragments, multiword keywords and no-equivalent cases were handled. The Marathi itself must come from the Marathi translation.
- Chapter 2 only: the lines for ^3-2-0 to ^3-36 (2-pathamanayo.sample.mapped.md) are approved; reuse them byte-for-byte and map the rest.

**Rules.** These are the rules the user approved with the sample.
- **Find the Marathi in that segment.** For each keyword, find the word or phrase in THAT segment's Marathi that carries its meaning.
- **Give it in DICTIONARY form:**
  - Nouns in the direct case, singular for a bare keyword (khandhehi = समूह, dhātūhi = तत्त्व, āyatanāni = इंद्रिय-क्षेत्र, saccāni = सत्य). A keyword with a numeral keeps the plural the text uses (ekādasahi dhātūhi = अकरा तत्त्वे, ekādasahāyatanehi = अकरा इंद्रिय-क्षेत्रे).
  - Oblique forms go back to direct: समूहांच्या → समूह; डोळ्याच्या इंद्रिय-क्षेत्रासोबत → डोळ्याचे इंद्रिय-क्षेत्र; घटनांपासून → घटना; मनाच्या चेतनेचे तत्त्वा- → मनाच्या चेतनेचे तत्त्व. A genitive that is part of the term stays (भौतिक रूपाचा समूह, डोळ्याचे तत्त्व).
  - Adjectives and participles in the masculine direct singular (जोडलेला, वेगळा, भिन्न प्रकारचा); invariable ones as they are (समाविष्ट, बाहेर, अंशतः). Verbal nouns of the method names in -णे (समाविष्ट असणे, वेगळे असणे).
  - Item names that the translation gives as a relative phrase + घटना keep that phrase in the direct case (e.g. «मुळांसह असलेल्या घटना», «मनाच्या मळांचा विषय होणाऱ्या घटना»), exactly as in harmonise-notes.md.
  - Strip postpositions and case endings (-चा/-ची/-चे/-च्या, -ला, -ने, -त/-यांत, -शी, -पासून, -सोबत, -मध्ये, यांच्या बाहेर) unless they are part of the term itself (e.g. «अनिर्मिताला वगळून», «प्रवाहात प्रवेश केलेला»).
- **Discontinuous keywords** (e.g. "viññāṇa saṅgahito", "āyatanaṃ saṅgahitā") join the parts with " … ": «चेतना … समाविष्ट». Cross-item bigrams like "āyatanehi ekādasahi" map to the matching stretch of text: «इंद्रिय-क्षेत्र आणि अकरा».
- **Context decides the sense**, as in the sample: rūpa in khandha context = भौतिक रूप, in āyatana/dhātu context = दृश्य रूप; dhamma as an object of mind = मनाचे विषय, as phenomena = घटना; sammā in sammappadhāna = योग्य, in the homage = पूर्णपणे.
- **Fragments** that lost a negative prefix map to the positive part.
- **Keep keywords exactly as given:** multiword, capitalised and odd fragments alike. Never add, drop, merge or reorder them.
- **No direct equivalent:** if there is none in that segment (for example, the word appears only inside a variant bracket kept in Pāli, or a particle has no Marathi word), write `kw=(no direct equivalent)`.
- **Compare each segment for real.** The same Pāli word may map differently by context. Identical formulaic segments get identical mappings. A helper script with a mapping table plus per-segment overrides is the expected method, but only after you have actually read each segment.
- **No ", " inside a Marathi value**, because that is the separator. Drop the comma or use " / ".

**Verify each chapter.** All must pass:
1. Keyword preservation, which must print `bad []`:
```
python3 -I -X utf8 -c "import pathlib;d=pathlib.Path('0-INBOX/temp/pipeline/pi-3-mr/mapper-mr');ch='CH';a=[l.split('] ',1) for l in (d/f'{ch}.keywords.md').read_text(encoding='utf-8').splitlines()];b=[l.split('] ',1) for l in (d/f'{ch}.mapped.md').read_text(encoding='utf-8').splitlines()];assert [x[0] for x in a]==[x[0] for x in b];bad=[i for (i,x),(_,y) in zip(a,b) if [k.strip() for k in x.split(', ')]!=[k.split('=',1)[0] for k in y.split(', ')]];print(ch,'lines',len(a),'bad',bad)"
```
2. Presence: every word of every value (minus its last one or two letters, to allow for case endings) occurs in that segment's Marathi, the same check map_sample.py runs. List and justify any exceptions (such as जीभ → जिभे-).
3. No ", " inside any value.

**Final report (short):**
- For each chapter: the line count, the verifier results and the number of (no direct equivalent).
- Any mappings that are genuinely unclear.
