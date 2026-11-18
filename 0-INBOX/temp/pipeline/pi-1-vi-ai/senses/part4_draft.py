"""Part 4 helper: write decisions-part4.txt for the 619 headwords of agg-part4.tsv.
Each headword was reviewed by hand (Vietnamese values vs the approved Russian line, `words`/`show` for
every multi-value or multi-sense case; part4_ru_lookup.py prints both). EXPLICIT holds the hand-written
lines (splits, tags adapted to the family wording of parts 1-3, headwords missing from the Russian file).
FAMILY adapts the Russian 'rules and vows' of the sīlabbatupādāna family to the 'rules and rituals'
wording of the sīlabbataparāmāsa family (Vietnamese «giới hạnh và nghi thức» in both).
Every other headword was checked to be a one-meaning word whose Russian line has exactly ONE sense;
its tag is that Russian tag copied word for word.
The script stops if a headword not in EXPLICIT has no Russian line or a multi-sense Russian line."""
import os
import sys
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import senses_tool_vi as T  # noqa: E402

N = unicodedata.normalize
EXPLICIT = {
    # splits: two Vietnamese words for two different uses (Russian senses kept, verified with words/show)
    'vuṭṭhāna': "emergence from offences, rehabilitation, in āpattivuṭṭhāna (compound member): việc ra khỏi; "
                "emergence from meditative attainments, in samāpattivuṭṭhāna (compound member): việc xuất khỏi",
    'vuṭṭhānakusalatā': "skill in rehabilitation from offences (nominative sg.): sự thành thạo về việc ra khỏi; "
                        "skill in emerging from meditative attainments (nominative sg.): "
                        "sự thành thạo về việc xuất khỏi",
    # new split (coordinator rule): biết đủ = contentment in eating vs tự mãn = resting content (1-M2-140)
    'santuṭṭhitā': "contentment, satisfaction with little, in moderation in eating (nominative sg.): "
                   "sự biết đủ / biết đủ; "
                   "resting content, complacency, in 'asantuṭṭhitā kusalesu dhammesu' 'not resting content with "
                   "wholesome states' (nominative sg.): tự mãn",
    # one sense, tag adapted as for rūpaṃ in part 2 (phần vật chất = the matrix pair nāmañca rūpañca)
    'rūpañca': "and matter, material form, also 'the material' in nāmañca rūpañca, with ca (nominative sg.)",
    # parāmāsa family: 'misapprehension' wording of parts 1-3 instead of the Russian 'adherence'
    'parāmāsasaṃyojanaṃ': "the fetter of misapprehension, in sīlabbataparāmāsasaṃyojana (compound final)",
    'parāmāso kāyagantho': "the bodily tie of misapprehension, in sīlabbataparāmāso kāyagantho (nominative sg.)",
    # headwords missing from the Russian file
    'viharantaṃ': "dwelling, living on, in 'indriyaṃ asaṃvutaṃ viharantaṃ' 'living with the faculty "
                  "unrestrained' (accusative sg. present participle)",
    'atthi': "there is, exists, the positive part of natthi in the nihilist view (verb)",
    'ṭhānanti': "ground, occasion, in 'saṃvejaniyaṃ ṭhānaṃ' 'a ground for urgency', with the quotation "
                "marker (neuter sg.)",
    'ṭhānesu': "grounds, occasions, in 'saṃvejaniyesu ṭhānesu' 'in the grounds for urgency' (locative pl.)",
}
EXPLICIT = {N('NFC', k): N('NFC', v) for k, v in EXPLICIT.items()}
FAM_OLD, FAM_NEW = 'rules and vows', 'rules and rituals'

aggp, decp, _ = T.part_paths('4')
rows = T.read_agg(aggp)
ru = {}
with open(T.RU_SENSES, encoding='utf-8-sig') as f:
    for l in f:
        l = N('NFC', l.rstrip('\n'))
        i = l.find(': {')
        if i > 0 and l.endswith('}'):
            ru[l[:i]] = l[i + 3:-1]
out, errs, fam = [], [], []
for h in rows:
    if not rows[h]['vals']:
        continue
    if h in EXPLICIT:
        out.append(f'{h}: {{{EXPLICIT[h]}}}')
        continue
    if h not in ru:
        errs.append(f'{h}: no Russian line and no explicit decision')
        continue
    senses = ru[h].split('; ')
    if len(senses) != 1:
        errs.append(f'{h}: Russian line has {len(senses)} senses; needs an explicit decision')
        continue
    tag = senses[0].rsplit(': ', 1)[0]
    if 'sīlabbatupādān' in h.lower() or 'sīlabbataparāmās' in h.lower():
        if FAM_OLD not in tag:
            errs.append(f'{h}: family tag without {FAM_OLD!r}: {tag!r}')
            continue
        tag = tag.replace(FAM_OLD, FAM_NEW)
        fam.append(h)
    if 'adherence' in tag and 'parāmās' in h.lower():
        errs.append(f'{h}: parāmāsa tag still says adherence: {tag!r}')
    out.append(f'{h}: {{{tag}}}')
unused = [k for k in EXPLICIT if k not in rows]
if unused:
    errs.append(f'EXPLICIT keys not in agg-part4: {unused}')
if errs:
    print('\n'.join(errs))
    sys.exit(1)
with open(decp, 'w', encoding='utf-8', newline='\n') as f:
    f.write('# pi-1 Pāli→Vietnamese senses, part 4 (agg-part4.tsv, 619 headwords). Hand-reviewed tag table.\n'
            '# Tags copy the approved Russian pi-1 senses file word for word where the meaning is the same;\n'
            '# splits and combined tags follow decisions-sample.txt and decisions-part1..3.txt; the parāmāsa family\n'
            '# keeps "misapprehension", the sīlabbatupādāna family takes "rules and rituals" (giới hạnh và nghi thức).\n'
            '# Build: python -I -X utf8 senses_tool_vi.py build --part 4\n')
    f.write('\n'.join(out) + '\n')
print(f'wrote {len(out)} decision lines -> {decp}')
print(f'"rules and rituals" family tags adapted ({len(fam)}): {fam}')
