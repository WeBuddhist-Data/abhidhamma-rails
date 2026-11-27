"""Write the MR_ADJUST block for gen_decisions_my.py (pi-7) from the hand table below: the Marathi pi-7 tags that carry
a Marathi mapping note ('mapped as …', 'also its negated form', 'mapped in several wordings', 'mapped joined with the
plain noun') which does not describe the Burmese value. Checks that every headword is in agg-part1.tsv, has no binding
line and takes one Marathi tag. usage: mkadj.py out.txt"""
import importlib.util, pathlib, sys
HERE = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('g', HERE / 'gen_decisions_my.py'); g = importlib.util.module_from_spec(spec)
spec.loader.exec_module(g)
rows = g.read_agg(HERE / 'agg-part1.tsv')
bind = [g.read_senses(p, True) for p in g.BIND_FILES.values()]
mr = g.read_senses(g.MR_SENSES, False)
R = 'the Marathi tag carries a note on the Marathi mapping that the Burmese value does not show; adjusted to the Burmese'
T = [
    ('nabhāvanāya', 'not by development, the negated instrumental in the triad and dyad items (instrumental)'),
    ('Nadassanena', 'not by seeing the truths, the negated instrumental in the dyad and the items without roots to be '
                    'abandoned by seeing (instrumental)'),
    ('nevācayagāmināpacayagāmī', 'leading neither to accumulation nor to dismantling (masculine sg.)'),
    ('Nevācayagāmināpacayagāmiṃ', 'leading neither to accumulation nor to dismantling (neuter sg.)'),
    ('nevācayagāmināpacayagāmissa', 'of what leads neither to accumulation nor to dismantling (genitive sg.)'),
    ('nevasekkhanāsekkho', 'belonging neither to one in training nor to one beyond training (masculine sg.)'),
    ('Nevasekkhanāsekkhaṃ', 'belonging neither to one in training nor to one beyond training (neuter sg.)'),
    ('nevasekkhanāsekkhañca', 'and belonging neither to one in training nor to one beyond training (neuter sg.)'),
    ('nevasekkhanāsekkhassa', 'of what belongs neither to one in training nor to one beyond training (genitive sg.)'),
    ('Āsavañca', 'and a mental taint, item of the taint dyad (accusative sg. with -ñca)'),
    ('Saññojanaṃ', 'fetter, item of the fetter dyad, the dyad term itself a fetter (accusative sg.)'),
    ('saññojano', 'fetter, item of the fetter dyad, the dyad term itself a fetter (nominative sg.)'),
    ('Ganthaṃ', 'tie, knot, item of the tie dyad, the dyad term itself a tie (accusative sg.)'),
    ('Ganthañca', 'and a tie, knot, item of the tie dyad (accusative sg. with -ñca)'),
    ('nīvaraṇo', 'hindrance, item of the hindrance dyad, the dyad term itself a hindrance (nominative sg.)'),
    ('Nīvaraṇañceva', 'both a hindrance, item of the hindrance dyad (neuter sg. with -ñceva)'),
    ('Parāmāsañca', 'and wrong grasping, item of the wrong-grasping dyad (accusative sg. with -ñca)'),
    ('upādāno', 'clinging, item of the clinging dyad, the dyad term itself a clinging (masculine sg.)'),
    ('Upādānañca', 'and clinging, item of the clinging dyad, the dyad term itself a clinging '
                   '(nominative/accusative sg. with -ñca)'),
    ('Kilesaṃ', 'defilement, item of the defilement dyad, the dyad term itself a defilement (accusative sg.)'),
]
out = []
for hw, tag in T:
    assert hw in rows, hw
    assert not any(g.lookup(b, hw) for b in bind), hw
    k = g.lookup(mr, hw)
    assert k and len(mr[k]) == 1, hw
    out.append(f'    {hw!r}: ({tag!r},\n        {R + "; Marathi tag: " + mr[k][0]!r}),')
open(sys.argv[1], 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print(len(out))
