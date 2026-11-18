"""Part 3 helper: write decisions-part3.txt for the 622 headwords of agg-part3.tsv.
Each headword was reviewed by hand (Vietnamese values vs the approved Russian line, `words`/`show` for
every multi-value or multi-sense case; part3_ru_lookup.py prints both). EXPLICIT holds the hand-written
lines (splits, combined tags). FAMILY adapts the Russian tag for the sīlabbataparāmāsa family to the
'misapprehension' wording fixed in parts 1-2 (Parāmāsa, parāmāso). Every other headword was checked to be
a one-meaning word whose Russian line has exactly ONE sense; its tag is that Russian tag copied word for word.
The script stops if a headword not in EXPLICIT has no Russian line or a multi-sense Russian line."""
import os
import sys
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import senses_tool_vi as T  # noqa: E402

N = unicodedata.normalize
EXPLICIT = {
    # splits (Russian senses kept, verified with words/show)
    'sineho': "affection, fond attachment, in the lists of craving and the taints (nominative sg.): sự luyến ái; "
              "moisture, the liquidity of the water element (nominative sg.): chất ẩm",
    'dhamme': "the Buddha's teaching, in doubt about the Teacher and the Teaching (locative sg.): Giáo Pháp; "
              "phenomena, states, as object in 'dhamme ārabbha' (accusative pl.): hiện tượng",
    'niyatā': "fixed, certain in result, as in micchattaniyata and sammattaniyata (nominative pl.): cố định; "
              "bound, restricted to each being, in the definition of the internal (nominative pl.): cố hữu",
    # new splits: two Vietnamese words for two different referents or uses (coordinator rule from part 2)
    'phalaṃ': "fruit of the path, fruition, as in arahattaphala (nominative/accusative sg.): thành quả; "
              "fruit of deeds, the result of good and bad actions, in 'kammānaṃ phalaṃ vipāko' "
              "(nominative sg.): quả",
    'para': "others, other people, as in parālābha 'others' gain' (compound member): người khác; "
            "other, in the deity name paranimmitavasavattī 'wielding power over others' creations' "
            "(compound member): Tha",
    # one Vietnamese value where the Russian has two senses: combined tag
    'sīla': "rules or morality, ethical conduct, in sīlabbata 'rules and vows' and as in sīlasaṃvara and "
            "sīlavisuddhi (compound member)",
    'sacca': "truth, what is true, in idaṃsaccābhinivesa 'adherence to only this is true' and in "
             "saccānulomika 'conforming to the truths' (compound member)",
}
EXPLICIT = {N('NFC', k): N('NFC', v) for k, v in EXPLICIT.items()}
FAM_OLD, FAM_NEW = 'adherence to rules and vows', 'misapprehension of rules and rituals'

aggp, decp, _ = T.part_paths('3')
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
    if 'sīlabbataparāmās' in h.lower():
        if FAM_OLD not in tag:
            errs.append(f'{h}: family tag without {FAM_OLD!r}: {tag!r}')
            continue
        tag = tag.replace(FAM_OLD, FAM_NEW)
        fam.append(h)
    out.append(f'{h}: {{{tag}}}')
unused = [k for k in EXPLICIT if k not in rows]
if unused:
    errs.append(f'EXPLICIT keys not in agg-part3: {unused}')
if errs:
    print('\n'.join(errs))
    sys.exit(1)
with open(decp, 'w', encoding='utf-8', newline='\n') as f:
    f.write('# pi-1 Pāli→Vietnamese senses, part 3 (agg-part3.tsv, 622 headwords). Hand-reviewed tag table.\n'
            '# Tags copy the approved Russian pi-1 senses file word for word where the meaning is the same;\n'
            '# splits and combined tags follow decisions-sample.txt / decisions-part1.txt / decisions-part2.txt;\n'
            '# the sīlabbataparāmāsa family keeps the parts 1-2 wording "misapprehension of rules and rituals".\n'
            '# Build: python -I -X utf8 senses_tool_vi.py build --part 3\n')
    f.write('\n'.join(out) + '\n')
print(f'wrote {len(out)} decision lines -> {decp}')
print(f'sīlabbataparāmāsa family tags adapted ({len(fam)}): {fam}')
