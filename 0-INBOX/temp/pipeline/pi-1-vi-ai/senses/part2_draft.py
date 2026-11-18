"""Part 2 helper: write decisions-part2.txt for the 622 headwords of agg-part2.tsv.
Each headword was reviewed by hand (Vietnamese values vs the approved Russian line, `words`/`show` for
every multi-value or multi-sense case; part2_ru_lookup.py prints both). EXPLICIT holds the hand-written
lines (splits, combined tags, headwords missing from the Russian file, tags adapted to the Vietnamese
values). Every other headword was checked to be a one-meaning word whose Russian line has exactly ONE
sense; its tag is that Russian tag copied word for word.
The script stops if a headword not in EXPLICIT has no Russian line or a multi-sense Russian line."""
import os
import sys
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import senses_tool_vi as T  # noqa: E402

N = unicodedata.normalize
EXPLICIT = {
    # one Vietnamese sense, tag adapted (Russian tag covers only one of the uses)
    'patho': "path, way, a synonym of view, also the forked way in dvedhāpatho 'crossroads' (nominative sg.)",
    'dukkhaṃ': "pain, painful feeling of mind or body, as a factor and in the feeling definitions (neuter sg.)",
    'parāmāso': "misapprehension, wrong grasping by views, also in sīlabbataparāmāso 'misapprehension of rules "
                "and rituals' (nominative sg.)",
    'samuddo': "ocean, sea, a name for the sense organ in the eye-base definition, also in taṇhāsamuddo "
               "'ocean of craving' (nominative sg.)",
    # headwords missing from the Russian file
    'avasesa': "remainder, what is left over, in anavasesappahānāya 'for abandoning without remainder' "
               "(compound member)",
    'vidhena': "in … ways, the second member of duvidhena, tividhena and the other numbered classifications "
               "(compound final, instrumental)",
    # splits (Russian senses kept, verified with words/show)
    'thambhitattaṃ': "rigidity, stiffness of mind, in the doubt list (neuter sg.): trạng thái cứng đờ; "
                     "distension, the state of being supported, said of the air element (neuter sg.): "
                     "trạng thái căng cứng",
    'rūpaṃ': "matter, material form, also 'the material' in nāmarūpa (nominative/accusative sg.): "
             "vật chất / phần vật chất; visible form, the object of the eye, in 'cakkhunā rūpaṃ disvā' "
             "(accusative sg.): hình sắc",
    'hetukaṃ': "having roots, rooted (compound final, neuter sg.): có gốc rễ; "
               "caused by, in cittahetuka 'caused by mind' (compound final): có … làm gốc rễ",
    'vaṇṇa': "colour, visible hue (compound member, as in vaṇṇanibhā): màu sắc; "
             "praise, reputation, in vaṇṇamacchariya 'stinginess about praise' (compound member): lời khen",
    'dhātūnaṃ': "of things, material objects, in 'dhātūnaṃ sannighātasaddo' (genitive pl.): vật; "
                "of the elements, in the definition of skill in attention (genitive pl.): yếu tố",
    'phala': "fruits of plants, in the lists of smells and tastes (compound member): trái cây; "
             "fruit of the path, in phalasamaṅgī 'one possessing the fruit' (compound member): thành quả",
    'khandha': "stems, plant stalks, in the list of tastes (compound member): thân cây; "
               "aggregates, in khandhadhātuāyatana (compound member): khối",
    'saṅkha': "conch shell, among the gems in maṇisaṅkhamuttāveḷuriya (compound member): vỏ ốc; "
              "conch horn, the blown instrument in saṅkhasadda 'sound of conches' (compound member): tù và",
    'kāyassa':"of the physical body, in bodily intimation and moderation in food (genitive sg.): thân; "
               "of the mental body, the group of mental factors, as in kāyapassaddhi (genitive sg.): thân tinh thần",
    'bhedo': "breaking forth of speech, articulation, in vacībhedo (compound final): sự phát thành; "
             "breaking up, dissolution, in the impermanence list (nominative sg.): sự tan rã",
}
EXPLICIT = {N('NFC', k): N('NFC', v) for k, v in EXPLICIT.items()}

aggp, decp, _ = T.part_paths('2')
rows = T.read_agg(aggp)
ru = {}
with open(T.RU_SENSES, encoding='utf-8-sig') as f:
    for l in f:
        l = N('NFC', l.rstrip('\n'))
        i = l.find(': {')
        if i > 0 and l.endswith('}'):
            ru[l[:i]] = l[i + 3:-1]
out, errs = [], []
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
    out.append(f'{h}: {{{senses[0].rsplit(": ", 1)[0]}}}')
unused = [k for k in EXPLICIT if k not in rows]
if unused:
    errs.append(f'EXPLICIT keys not in agg-part2: {unused}')
if errs:
    print('\n'.join(errs))
    sys.exit(1)
with open(decp, 'w', encoding='utf-8', newline='\n') as f:
    f.write('# pi-1 Pāli→Vietnamese senses, part 2 (agg-part2.tsv, 622 headwords). Hand-reviewed tag table.\n'
            '# Tags copy the approved Russian pi-1 senses file word for word where the meaning is the same;\n'
            '# splits and combined tags follow decisions-sample.txt / decisions-part1.txt (kāya, dukkha, parāmāsa).\n'
            '# Build: python -I -X utf8 senses_tool_vi.py build --part 2\n')
    f.write('\n'.join(out) + '\n')
print(f'wrote {len(out)} decision lines -> {decp}')
