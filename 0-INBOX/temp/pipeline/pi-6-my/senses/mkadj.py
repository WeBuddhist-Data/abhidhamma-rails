"""Write the MR_ADJUST block (literal entries) for gen_decisions_my.py from the hand table below; checks that every
headword is in agg-part1.tsv and takes a Marathi tag (no binding line). usage: mkadj.py out.txt"""
import importlib.util, pathlib, sys
HERE = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('g', HERE / 'gen_decisions_my.py'); g = importlib.util.module_from_spec(spec)
spec.loader.exec_module(g)
rows = g.read_agg(HERE / 'agg-part1.tsv')
order = list(rows)
bind = [g.read_senses(p, True) for p in g.BIND_FILES.values()]
mr = g.read_senses(g.MR_SENSES, False)
R_FAM = 'the Marathi tag names the root member only; the Burmese value is the whole compound'
R_SYN = 'the Marathi tag is that of kusala alone; the Burmese value is the hetuvāra synonym'
R_NEG = 'the Marathi tag is the positive lemma gloss; the Burmese value is the negated verb'
R_BEING = 'the Marathi tag names the plane; the Burmese value is the beings of that plane (R5)'
R_CYC = 'the Marathi tag names the faculty or plane only; the Burmese value is the cycle label «…ကို အခြေခံသော»'
R_OWN = 'the Marathi tag describes another member or a general category; adjusted to what the Burmese value says'
T = []
CASE = {'ā': '(nominative pl.)', 'āti': '(nominative pl., quoted with iti)', 'āni': '(neuter pl.)',
        'aṃ': '(neuter sg.)', 'añceva': '(neuter sg., with ceva)'}
fam = {'kusala': 'a root that is skilful', 'akusala': 'a root that is unskilful',
       'abyākata': 'a root that is neither skilful nor unskilful', 'nāma': 'a root belonging to the mental side'}
for x, r in fam.items():
    for end in ('ā', 'āti', 'āni'):
        T.append((f'{x}mūlamūl{end}', f'the root of {r} {CASE[end]}', R_FAM))
    for end in ('ā', 'āti', 'aṃ', 'añceva'):
        T.append((f'{x}mūlak{end}', f'based on {r} {CASE[end]}', R_FAM))
        T.append((f'{x}mūlamūlak{end}', f'based on the root of {r} {CASE[end]}', R_FAM))
    T.append((f'{x}mūlasahajātā dhammā', f'states arisen together with {r} (nominative pl.)', R_FAM))
    T.append((f'{x}mūlasahajātā', f'arisen together with {r} (nominative pl.)', R_FAM))
for end in ('ā', 'āti', 'aṃ', 'añceva', 'āni'):
    T.append((f'ekamūlamūl{end}', f'having one root of a root in common {CASE[end]}', R_FAM))
    T.append((f'ekamūlamūlak{end}', f'based on one root of a root in common {CASE[end]}', R_FAM))
for end in ('ā', 'āti', 'āni'):
    T.append((f'aññamaññamūlamūl{end}', f'each serving as the root of a root for the other {CASE[end]}', R_FAM))
    T.append((f'aññamaññamūlamūlak{end}', f'each stemming from the other as the root of a root {CASE[end]}', R_FAM))
T += [
    ('kusalahetūti', "the wholesome roots, here 'having the skilful as cause', the second of ten synonyms for a root "
     '(nominative pl., quoted with iti)', R_SYN + ' (= kusalahetū)'),
    ('kusalanidānā', 'having a skilful source, the third of ten synonyms for a root (nominative pl.)', R_SYN),
    ('kusalasamuṭṭhānā', 'having a skilful origin, the sixth of ten synonyms for a root (nominative pl.)', R_SYN),
    ('kusalārammaṇā', 'having a skilful object, the eighth of ten synonyms for a root (nominative pl.)', R_SYN),
    ('kusalasamudayā', 'having a skilful arising, the tenth of ten synonyms for a root (nominative pl.)', R_SYN),
    ('nuppajjati', 'does not come into being (negated, 3rd sg. present)', R_NEG),
    ('nuppajjatīti', 'does not come into being (negated, present, quoted with iti)', R_NEG),
    ('nuppajjittha', 'did not come into being (negated, past)', R_NEG),
    ('nuppajjitthāti', 'did not come into being (negated, past, quoted with iti)', R_NEG),
    ('nuppajjissati', 'will not come into being (negated, future)', R_NEG),
    ('nuppajjissatīti', 'will not come into being (negated, future, quoted with iti)', R_NEG),
    ('nappajahati', 'does not give up (negated, 3rd sg. present)', R_NEG),
    ('nappajahanti', 'do not give up (negated, 3rd pl. present)', R_NEG),
    ('nappajahatīti', 'does not give up (negated, present, quoted with iti)', R_NEG),
    ('nappajahissati', 'will not give up (negated, 3rd sg. future)', R_NEG),
    ('nappajahissanti', 'will not give up (negated, 3rd pl. future)', R_NEG),
    ('nappajahissatīti', 'will not give up (negated, future, quoted with iti)', R_NEG),
    ('nānuseti', 'does not lie dormant (negated, 3rd sg. present)', R_NEG),
    ('nānusetīti', 'does not lie dormant (negated, present, quoted with iti)', R_NEG),
    ('nānusenti', 'do not lie dormant (negated, 3rd pl. present)', R_NEG),
    ('nānusentīti', 'do not lie dormant (negated, 3rd pl. present, quoted with iti)', R_NEG),
    ('arūpānaṃ', 'of beings in the immaterial plane (genitive pl.)', R_BEING),
    ('suddhāvāsānaṃ', 'of beings in the Pure Abodes, the highest fine-material planes of non-returners (genitive pl.)',
     R_BEING),
    ('pañcavokārānaṃ', 'of beings in the existence with all five aggregates (genitive pl.)', R_BEING),
    ('rūpāvacarānaṃ', 'of beings in the fine-material plane (genitive pl.)', R_BEING),
    ('arūpāvacarānaṃ', 'of beings in the immaterial plane (genitive pl.)', R_BEING),
    ('āpāyikānaṃ', 'of beings in the states of loss, the planes of unhappy rebirth (genitive pl.)', R_BEING),
    ('cakkhundriyamūlakaṃ', 'based on the eye faculty, a cycle tag (neuter sg.)', R_CYC),
    ('ghānindriyamūlakaṃ', 'based on the nose faculty, a cycle tag (neuter sg.)', R_CYC),
    ('itthindriyamūlakaṃ', 'based on the faculty of femaleness, a cycle tag (neuter sg.)', R_CYC),
    ('purisindriyamūlakaṃ', 'based on the faculty of maleness, a cycle tag (neuter sg.)', R_CYC),
    ('jīvitindriyamūlakaṃ', 'based on the life faculty, a cycle tag (neuter sg.)', R_CYC),
    ('somanassindriyamūlakaṃ', 'based on the faculty of glad mental feeling, a cycle tag (neuter sg.)', R_CYC),
    ('upekkhindriyamūlakaṃ', 'based on the faculty of neutral feeling, a cycle tag (neuter sg.)', R_CYC),
    ('saddhindriyamūlakaṃ', 'based on the faculty of trust, a cycle tag (neuter sg.)', R_CYC),
    ('paññindriyamūlakaṃ', 'based on the faculty of wisdom, a cycle tag (neuter sg.)', R_CYC),
    ('domanassindriyamūlakaṃ', 'based on the faculty of unhappy mental feeling, a cycle tag (neuter sg.)', R_CYC),
    ('anaññātaññassāmītindriyamūlakaṃ', "based on the faculty 'I shall know the not yet known', a cycle tag "
     '(neuter sg.)', R_CYC),
    ('aññindriyamūlakaṃ', 'based on the faculty of final knowledge, a cycle tag (neuter sg.)', R_CYC),
    ('kāmadhātumūlakaṃ', 'based on the sense-sphere plane, a cycle tag (neuter sg.)', R_CYC),
    ('rūpadhātumūlakaṃ', 'based on the fine-material plane, a cycle tag (neuter sg.)', R_CYC),
    ('arūpadhātumūlakaṃ', 'based on the immaterial plane, a cycle tag (neuter sg.)', R_CYC),
    ('nakāmadhātumūlakaṃ', 'based on what is not the sense-sphere plane, a cycle tag (neuter sg.)', R_CYC),
    ('narūpadhātumūlakaṃ', 'based on what is not the fine-material plane, a cycle tag (neuter sg.)', R_CYC),
    ('naarūpadhātumūlakaṃ', 'based on what is not the immaterial plane, a cycle tag (neuter sg.)', R_CYC),
    ('nakāmanaarūpadhātumūlakaṃ', 'based on what is neither the sense-sphere nor the immaterial plane, a cycle tag '
     '(neuter sg.)', R_CYC),
    ('narūpanaarūpadhātumūlakaṃ', 'based on what is neither the fine-material nor the immaterial plane, a cycle tag '
     '(neuter sg.)', R_CYC),
    ('nakāmanarūpadhātumūlakaṃ', 'based on what is neither the sense-sphere nor the fine-material plane, a cycle tag '
     '(neuter sg.)', R_CYC),
    ('sacakkhukānaṃ', 'of those having the eye (genitive pl.)', R_OWN),
    ('acakkhukānaṃ', 'of those lacking the eye (genitive pl.)', R_OWN),
    ('sacakkhukā', 'those having the eye (nominative pl.)', R_OWN),
    ('sasotakānaṃ', 'of those having the ear (genitive pl.)', R_OWN),
    ('asotakānaṃ', 'of those lacking the ear (genitive pl.)', R_OWN),
    ('taṇhāvippayuttacitte', 'in a mind dissociated from craving (locative)', R_OWN),
    ('cittake', "the mind section, in the names of the cited sections 'yassa cittake …' (locative)", R_OWN),
    ('pacchimakusalacittassa', 'of the last wholesome mind (genitive)', R_OWN),
    ('avitakkaavicāraṃ', 'without applied and without sustained thinking (neuter sg.)', R_OWN),
    ('avitakkaavicārapacchimacittasamaṅgīnaṃ', 'of those possessed of a last mind without applied and sustained '
     'thinking (genitive pl.)', R_OWN),
    ('savitakkasavicārabhūmiyaṃ', 'in the level with applied and sustained thinking (locative)', R_OWN),
    ('avitakkaavicārabhūmiyaṃ', 'in the level without applied and sustained thinking (locative)', R_OWN),
    ('avitakkaavicārapacchimacittassa', 'of the last mind without applied and sustained thinking (genitive)', R_OWN),
    ('savitakkasavicārapacchimacittassa', 'of the last mind with applied and sustained thinking (genitive)', R_OWN),
    ('pacchimacittasamaṅgīnaṃ', 'of those possessed of the last mind before death (genitive pl.)', R_OWN),
    ('pacchimacittasamaṅgīna', 'of those possessed of the last mind before death (genitive pl., misspelt for '
     'pacchimacittasamaṅgīnaṃ)', R_OWN),
    ('upekkhāsampayuttapacchimacittasamaṅgīnaṃ', 'of those possessed of a last mind accompanied by neutral feeling '
     '(genitive pl.)', R_OWN),
    ('somanassasampayuttapacchimacittasamaṅgīnaṃ', 'of those possessed of a last mind accompanied by glad mental '
     'feeling (genitive pl.)', R_OWN),
    ('upekkhāsampayuttapacchimacittaṃ', 'a last mind accompanied by neutral feeling (nominative sg.)', R_OWN),
    ('somanassasampayuttapacchimacittaṃ', 'a last mind accompanied by glad mental feeling (nominative sg.)', R_OWN),
    ('nirodhasamāpannānaṃ', 'of those who have entered the attainment of cessation (genitive pl.)', R_OWN),
    ('nirodhasamāpannānanti', 'of those who have entered the attainment of cessation (genitive pl., quoted with iti)',
     R_OWN),
    ('dhātuvisajjanāvāro', 'heading: the section of answers on the planes', R_OWN),
    ('upapajjissati', 'will come into being (3rd sg. future), misspelt in the source for uppajjissati '
     '(map-harmonise §A 6)', R_OWN),
    ('uppajjamānanti', 'arising, what is in the course of arising (present participle, quoted with iti)', R_OWN),
    ('uppajjamānañca', 'arising, what is in the course of arising (present participle, with ca)', R_OWN),
    ('nirujjhamānanti', 'ceasing, what is in the course of ceasing (present participle, quoted with iti)', R_OWN),
    ('nirujjhamānañca', 'ceasing, what is in the course of ceasing (present participle, with ca)', R_OWN),
    ('sānusayavāro', 'heading: the section on those who have a tendency', R_OWN),
    ('sānusayavāra', 'heading: the section on those who have a tendency (stem)', R_OWN),
    ('sānusayavāre', 'in the section on those who have a tendency (locative)', R_OWN),
    ('anusayavāro', 'heading: the section on the tendencies', R_OWN),
    ('anusayavāra', 'heading: the section on the tendencies (stem)', R_OWN),
    ('anusayavāre', 'in the section on the tendencies (locative)', R_OWN),
    ('suddhadhātuvāro', 'heading: the section on the elements alone', R_OWN),
    ('suddhasaṅkhāravāro', 'heading: the section on the formations alone', R_OWN),
    ('saccayamakaṃ', 'title of the chapter of pairs on the truths', R_OWN),
    ('saṅkhārayamakaṃ', 'title of the chapter of pairs on the formations', R_OWN),
    ('saṅkhārayamakepi', 'in the chapter of pairs on the formations too (locative, with pi)', R_OWN),
    ('anusayayamakaṃ', 'title of the chapter of pairs on the tendencies', R_OWN),
    ('yassakasadisaṃ', "like the 'of whom' section, in an abbreviation note", R_OWN),
    ('yatthakasadisaṃ', "like the 'where' section, in an abbreviation note", R_OWN),
    ('yassayatthakasadisaṃ', "like the 'of whom, where' section, in an abbreviation note", R_OWN),
    ('abhisametāvīnaṃ', 'of those who have seen the truths directly (genitive pl.)', R_OWN),
    ('anabhisametāvīnaṃ', 'of those who have not yet seen the truths directly (genitive pl.)', R_OWN),
]
pos = {h: i for i, h in enumerate(order)}
bad, sample, full = [], [], []
seen = set()
for hw, tag, why in T:
    if hw in seen: bad.append(f'dup {hw}'); continue
    seen.add(hw)
    if hw not in rows: continue                       # a family form not in the book
    if any(g.lookup(b, hw) for b in bind): bad.append(f'binding {hw}'); continue
    k = g.lookup(mr, hw)
    if not k or len(mr[k]) != 1: bad.append(f'not one Marathi tag {hw}'); continue
    old = mr[k][0]
    line = f'    {hw!r}: ({tag!r},\n        {why + "; Marathi tag: " + old!r}),'
    (sample if pos[hw] < 80 else full).append((pos[hw], line))
if bad: sys.exit('\n'.join(bad))
out = ['    # ---- sample ----'] + [l for _, l in sorted(sample)] + ['    # ---- full run ----'] + [l for _, l in sorted(full)]
pathlib.Path(sys.argv[1]).write_text('\n'.join(out) + '\n', encoding='utf-8')
print(len(sample), len(full))
