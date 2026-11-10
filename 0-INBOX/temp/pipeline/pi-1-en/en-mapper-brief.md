# Brief: English→Pāli keyword mapping for pi-1 (Dhammasaṅgaṇī)

**Setup.**
- Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write tools for files, PowerShell for commands, `python -I -X utf8`, helper scripts written to files.
- Write ONLY your own mapped files, plus helper scripts named after your chapters, inside 0-INBOX\temp\pipeline\pi-1-en\mapper\. Do not touch 1-SOURCES\ or 4-SYSTEM\, and do not run git.

**Read first.**
- AI_translation\skills\keyword-equivalence-mapper.md (the skill you execute).
- The format to copy: AI_translation\english\pi-4-keywords-by-reference-pali-english-plain.md and pi-3-…-plain.md (the same step for earlier books; look at 30–40 lines).

**Per chapter <ch>:**
- **Keywords (English, extracted by script):** 0-INBOX\temp\pipeline\pi-1-en\mapper\<ch>.keywords.md, `[id] kw1, kw2, …`.
- **English translation:** AI_translation\english\pi-1-english-plain-zeroshot_split_chapters\<ch>.md (segments end with ^id).
- **Pāli source (where the equivalents come from):** AI_translation\pali\pi-1_split_chapters\<ch>.md, same ^ids.
- **Helpful:** the English was generated from the Pāli by builder scripts with fixed phrase tables (0-INBOX\temp\pipeline\pi-1-en\build_*.py, const_*.py, en-zeroshot-terms.md, notes-*.md). They show exactly which Pāli produced which English phrase.
- **Output:** mapper\<ch>.mapped.md. Same lines, same order, the same English keywords in the same order, each written `pāli=english` (Pāli on the LEFT, the English keyword unchanged on the right), as in the pi-3/pi-4 maps.

**Rules (as in the earlier English maps).**
- For each English keyword, find the Pāli word or phrase in THAT segment's Pāli that it translates, and write it as it appears there (the inflected form in the text, e.g. `kāyena=body`, `Katamo puggalo=kind of person`; a compound may be cut to the part the keyword covers). Keep the Pāli diacritics exactly.
- Keep the English keywords exactly as given (multiword, capitalised, odd fragments alike). Never add, drop, merge or reorder them.
- If the keyword has no Pāli counterpart in that segment (an English function word or added clarification, or it occurs only inside a variant bracket), write `(no direct equivalent)=kw`.
- Compare each segment for real; the same English word can come from different Pāli in different segments. Identical formulaic segments get identical mappings. A helper script with a mapping table plus per-segment overrides is fine, after you have actually read the segments; the builder tables make most of the formulaic parts exact.
- No ", " inside a Pāli value (it is the separator).

**Verify each chapter** (replace CH). It must print `bad []`:
```
python -I -X utf8 -c "import pathlib;d=pathlib.Path('0-INBOX/temp/pipeline/pi-1-en/mapper');ch='CH';a=[l.split('] ',1) for l in (d/f'{ch}.keywords.md').read_text(encoding='utf-8').splitlines()];b=[l.split('] ',1) for l in (d/f'{ch}.mapped.md').read_text(encoding='utf-8').splitlines()];assert [x[0] for x in a]==[x[0] for x in b];bad=[i for (i,x),(_,y) in zip(a,b) if [k.strip() for k in x.split(', ')]!=[k.rsplit('=',1)[1] for k in y.split(', ')]];print(ch,'lines',len(a),'bad',bad)"
```
Also check that every Pāli value (left side, except `(no direct equivalent)`) occurs in that segment's Pāli text (write a small script; report any that don't, e.g. a cut compound, and justify them).

**Final report (short):** per chapter the line count, the verifier result, the number of (no direct equivalent), the Pāli-presence check result, and any genuinely unclear mappings.
