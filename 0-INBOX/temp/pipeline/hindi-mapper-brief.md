# Brief: Pāli→Hindi keyword mapping (pi-3, pi-4, pi-5)

**Setup.**
- Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: use the Read/Write tools for files and PowerShell for commands; run python as `python -I -X utf8`.
- Other agents map other chapters in parallel. Write ONLY your own mapped files, plus helper scripts named after your chapters inside your book's scratch folder.

**Read first.**
- AI_translation\skills\keyword-equivalence-mapper.md (the skill you execute).
- 0-INBOX\temp\pipeline\hindi-style.md (the Hindi conventions and core terms).

**Per chapter <ch> (book pi-N, scratch 0-INBOX\temp\pipeline\pi-N-hi\):**
- **Keywords:** mapper-hi\<ch>.keywords.md, in the form `[id] kw1, kw2, ...` (Pāli).
- **Hindi translation:** AI_translation\hindi\pi-N-hindi-plain-zeroshot_split_chapters\<ch>.md. Segments end with ^id.
- **Pāli source, for context:** AI_translation\pali\pi-N_split_chapters\<ch>.md.
- **Output:** mapper-hi\<ch>.mapped.md. Same lines, same order, the same keywords in the same order, each written `pali=हिंदी`.
- **Conventions reference:** the user-approved Russian mapping of the same chapter, 0-INBOX\temp\pipeline\pi-3\mapper-ru\, pi-4\mapper-ru\ or pi-5-ru\mapper-ru\ (<ch>.mapped.md). Use it to see how fragments, multiword keywords and no-equivalent cases were handled. The Hindi itself must come from the Hindi translation.

**Rules.** These are the same rules the user approved for Russian, adapted to Hindi.
- **Find the Hindi in that segment.** For each keyword, find the word or phrase in THAT segment's Hindi that carries its meaning.
- **Give it in DICTIONARY form:**
  - Nouns in the direct case. Use the singular, or keep the plural if the concept is plural. Oblique forms like समूहों or परिघटनाओं become समूह or परिघटना.
  - Adjectives and participles in the masculine direct singular (जुड़ा, अलग, शामिल), unless the concept is plural.
  - Verbs in the infinitive (-ना), or as the participle the text uses.
  - Strip postpositions and case markers (को, से, में, का/की/के, ने) unless they are part of the term itself (e.g. «धारा में प्रवेश कर चुका»).
- **Fragments** that lost a negative prefix map to the positive part.
- **Keep keywords exactly as given:** multiword, capitalised and odd fragments alike. Never add, drop, merge or reorder them.
- **No direct equivalent:** if there is none in that segment (for example, the word appears only inside a variant bracket kept in Pāli, or a particle has no Hindi word), write `kw=(no direct equivalent)`.
- **Compare each segment for real.** The same Pāli word may map differently by context. Identical formulaic segments get identical mappings. A helper script with a mapping table plus per-segment overrides is fine, but only after you have actually read each segment.
- **No ", " inside a Hindi value**, because that is the separator. Drop the comma or use " / ".

**Verify each chapter** (replace N and CH). The command must print `bad []`:
```
python -I -X utf8 -c "import pathlib;d=pathlib.Path('0-INBOX/temp/pipeline/pi-N-hi/mapper-hi');ch='CH';a=[l.split('] ',1) for l in (d/f'{ch}.keywords.md').read_text(encoding='utf-8').splitlines()];b=[l.split('] ',1) for l in (d/f'{ch}.mapped.md').read_text(encoding='utf-8').splitlines()];assert [x[0] for x in a]==[x[0] for x in b];bad=[i for (i,x),(_,y) in zip(a,b) if [k.strip() for k in x.split(', ')]!=[k.split('=',1)[0] for k in y.split(', ')]];print(ch,'lines',len(a),'bad',bad)"
```

**Final report (short):**
- For each chapter: the line count, the verifier result and the number of (no direct equivalent).
- Any mappings that are genuinely unclear.
