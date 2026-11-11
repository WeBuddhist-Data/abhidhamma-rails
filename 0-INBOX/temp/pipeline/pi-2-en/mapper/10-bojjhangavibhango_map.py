import pathlib
d = pathlib.Path(__file__).parent
ch = '10-bojjhangavibhango'
NDE = '(no direct equivalent)'

# the seven factors, as named in the list formula
SEVEN = {
 'awakening': 'sambojjhaṅgo', 'awakening factor': 'sambojjhaṅgo', 'Awakening Factors': 'bojjhaṅgā',
 'awakening factors': 'bojjhaṅgā', 'concentration': 'samādhi', 'equanimity': 'upekkhā', 'factor': 'sambojjhaṅgo',
 'factor of concentration': 'samādhisambojjhaṅgo', 'factor of energy': 'vīriyasambojjhaṅgo',
 'factor of equanimity': 'upekkhāsambojjhaṅgo', 'factor of investigation': 'dhammavicayasambojjhaṅgo',
 'factor of joy': 'pītisambojjhaṅgo', 'factor of mindfulness': 'satisambojjhaṅgo',
 'factor of tranquillity': 'passaddhisambojjhaṅgo', 'factors': 'bojjhaṅgā', 'investigation': 'vicaya',
 'investigation of things': 'dhammavicaya', 'joy': 'pīti', 'mindfulness': 'sati', 'things': 'dhamma',
 'tranquillity': 'passaddhi',
}
SHORT = {k: SEVEN[k] for k in ('awakening', 'awakening factor', 'Awakening Factors', 'awakening factors',
         'equanimity', 'factor', 'factor of equanimity', 'factor of mindfulness', 'factors', 'mindfulness')}

# supramundane jhāna formula (2-473, 2-476, 2-478, 2-481)
JHANA = {
 'abandoning': 'pahānāya', 'abandoning of views': 'diṭṭhigatānaṃ pahānāya', 'absorption': 'jhānaṃ',
 'beyond': 'lokuttaraṃ', 'develops': 'bhāveti', 'develops the meditative': 'jhānaṃ bhāveti',
 'difficult': 'dukkhapaṭipadaṃ', 'difficult practice': 'dukkhapaṭipadaṃ', 'direct': 'ābhiññaṃ',
 'direct knowledge': 'ābhiññaṃ', 'dismantling': 'apacaya', 'dwells': 'viharati', 'enters': 'upasampajja',
 'enters and dwells': 'upasampajja viharati', 'knowledge': 'ābhiññaṃ', 'leading to dismantling': 'apacayagāmiṃ',
 'meditative': 'jhānaṃ', 'meditative absorption': 'jhānaṃ', 'Meditative absorption': 'jhānaṃ', 'monk': 'bhikkhu',
 'occasion': 'samaye', 'pleasures': 'kāmehi', 'practice': 'paṭipadaṃ',
 'practice and slow': 'dukkhapaṭipadaṃ dandhābhiññaṃ', 'reaching': 'pattiyā', 'secluded': 'vivicceva',
 'secluded from sense': 'vivicceva kāmehi', 'sense': 'kāmehi', 'sense pleasures': 'kāmehi',
 'slow': 'dandhābhiññaṃ', 'slow direct': 'dandhābhiññaṃ', 'slow direct knowledge': 'dandhābhiññaṃ',
 'stage': 'bhūmiyā', 'therein': 'Tattha', 'views': 'diṭṭhigatānaṃ',
}
# definitions of the factors in the Abhidhamma classification
DEF = {
 'associated': 'sampayuttā', 'equanimous': 'upekkhanā', 'mind': 'cittassa', 'neutrality': 'majjhattatā',
 'path': 'magga', 'path factor': 'maggaṅgaṃ', 'recollection': 'anussati', 'remaining': 'Avasesā',
 'remaining things': 'Avasesā dhammā', 'right': 'sammā', 'things': 'dhammā', 'watching': 'ajjhupekkhanā',
}
# "the remaining things are associated with the awakening factor of X" (compound cut before -sampayuttā)
ASSOC = {
 'factor of concentration': 'samādhisambojjhaṅga', 'factor of energy': 'vīriyasambojjhaṅga',
 'factor of investigation': 'dhammavicayasambojjhaṅga', 'factor of joy': 'pītisambojjhaṅga',
 'factor of tranquillity': 'passaddhisambojjhaṅga',
}
# "on that occasion there is contact ... wholesome; as its result ..."
RESULT = {
 'contact': 'phasso', 'developed': 'bhāvitattā', 'done': 'katattā', 'emptiness': 'suññataṃ',
 'non-distraction': 'avikkhepo', 'things are wholesome': 'dhammā kusalā', 'wholesome': 'kusalā',
 'wholesome meditative': 'kusalassa jhānassa', 'wholesome meditative absorption': 'kusalassa jhānassa',
}
QA = {'answers': NDE, 'questions': 'Pañhā', 'Questions and Answers': 'Pañhāpucchakaṃ', 'section': NDE,
      'Section of Questions': 'Pañhāpucchakaṃ'}

def mg(*ds, **kw):
    r = {}
    for x in ds: r.update(x)
    r.update(kw)
    return r

M = {}
M['2-10-0'] = {'analysis': 'vibhaṅgo', 'awakening': 'Bojjhaṅga', 'Awakening Factors': 'Bojjhaṅga',
               'awakening factors': 'Bojjhaṅga', 'factors': 'Bojjhaṅga'}
M['2-10-1-0'] = {'classification': 'bhājanīyaṃ', 'discourses': 'Suttanta'}
for s in ('2-466', '2-468', '2-470', '2-472', '2-482'):
    M[s] = mg(SEVEN)
M['2-467'] = mg(SEVEN, {
 'arises': 'uppajjati', 'becomes': 'passambhati', 'body': 'kāyopi', 'care': 'nepakkena',
 'concentrated': 'samāhitaṃ', 'done': 'cirakatampi', 'dwelling': 'viharanto', 'endowed': 'samannāgato',
 'enters': 'āpajjati', 'examines': 'pavicarati', 'happy': 'sukhino', 'highest': 'paramena',
 'initiated': 'āraddhaṃ', 'inquiry': 'parivīmaṃsamāpajjati', 'investigates': 'pavicinati',
 'joyful': 'Pītimanassa', 'mind': 'cittaṃ', 'mindful': 'satimā', 'monk': 'bhikkhu', 'recalls': 'anussaritā',
 'remembers': 'saritā', 'slackening': 'asallīnaṃ', 'teaching': 'dhammaṃ', 'therein': 'Tattha',
 'tranquil': 'passambhati', 'unworldly': 'nirāmisā', 'watches': 'ajjhupekkhitā', 'wisdom': 'paññāya'})
M['2-469'] = mg(SEVEN, {
 'awakening': 'sambodhāya', 'bodily': 'kāyikaṃ', 'body': 'kāya', 'concentration': 'samādhi',
 'direct': 'abhiññāya', 'direct knowledge': 'abhiññāya', 'examination': 'vicāro', 'external': 'bahiddhā',
 'external things': 'bahiddhā dhammesu', 'internal': 'ajjhattaṃ', 'internal things': 'ajjhattaṃ dhammesu',
 'investigation': 'pavicayo', 'itself': 'tadapi', 'knowledge': 'abhiññāya', 'leads': 'saṃvattati',
 'leads to direct': 'abhiññāya / saṃvattati', 'mental': 'cetasikaṃ', 'mind': 'citta', 'regard': NDE,
 'therein': 'Tattha', 'things': 'dhammesu', 'thought': 'vitakko'})
M['2-471'] = mg(SEVEN, {
 'cessation': 'nirodha', 'classification': 'bhājanīyaṃ', 'develops': 'bhāveti',
 'develops the awakening': 'sambojjhaṅgaṃ bhāveti', 'discourses': 'Suttanta', 'dispassion': 'virāga',
 'finished': NDE, 'monk': 'bhikkhu', 'monk develops': 'bhikkhu / bhāveti', 'release': 'vossagga',
 'ripening': 'pariṇāmiṃ', 'seclusion': 'viveka', 'therein': 'Tattha',
 # "he develops the awakening factor of X" (accusative)
 'factor of concentration': 'samādhisambojjhaṅgaṃ', 'factor of energy': 'vīriyasambojjhaṅgaṃ',
 'factor of equanimity': 'upekkhāsambojjhaṅgaṃ', 'factor of investigation': 'dhammavicayasambojjhaṅgaṃ',
 'factor of joy': 'pītisambojjhaṅgaṃ', 'factor of tranquillity': 'passaddhisambojjhaṅgaṃ'})
M['2-10-2-0'] = {'abhidhamma': 'Abhidhamma', 'classification': 'bhājanīyaṃ'}
M['2-473'] = mg(JHANA, SHORT)
M['2-473']['awakening'] = 'bojjhaṅgā'
M['2-474'] = mg(SEVEN, DEF, {
 'aggregate': 'khandhassa', 'aggregate of consciousness': 'viññāṇakkhandhassa',
 'Aggregate of Consciousness': 'viññāṇakkhandhassa', 'aggregate of feeling': 'vedanākkhandhassa',
 'aggregate of mental': 'saṅkhārakkhandhassa', 'Aggregate of Mental': 'saṅkhārakkhandhassa',
 'Aggregate of Perception': 'saññākkhandhassa', 'aggregate of perception': 'saññākkhandhassa',
 'becoming': 'passambhanā', 'calmed': 'paṭippassambhitattaṃ', 'calming': 'paṭippassambhanā',
 'consciousness': 'viññāṇa', 'delight': 'pamodanā', 'effort': 'vāyāmo', 'elation': 'odagyaṃ', 'feeling': 'vedanā',
 'felicity': 'vitti', 'formations': 'saṅkhāra', 'gladness': 'pāmojjaṃ', 'initiation': 'ārambho',
 'initiation of energy': 'vīriyārambho', 'investigation': 'vicayo', 'investigation of things': 'dhammavicayo',
 'mental': 'cetasiko', 'Mental Formations': 'saṅkhāra', 'mental formations': 'saṅkhāra',
 'mental initiation': 'cetasiko vīriyārambho', 'merriment': 'pahāso', 'mirth': 'hāso',
 'non-delusion': 'amoho', 'perception': 'saññā', 'rejoicing': 'āmodanā', 'satisfaction': 'attamanatā',
 'steadiness': 'ṭhiti', 'therein': 'Tattha', 'tranquil': 'passambhanā', 'understanding': 'pajānanā',
 'view': 'diṭṭhi', 'wisdom': 'paññā'})
for s in ('2-475', '2-477', '2-480'):
    M[s] = mg(SHORT)
M['2-476'] = mg(SEVEN, JHANA, DEF, ASSOC)
M['2-478'] = mg(JHANA, SHORT, RESULT)
M['2-478']['awakening'] = 'bojjhaṅgā'
M['2-478']['things'] = 'dhammā'
M['2-479'] = mg(SHORT, DEF, therein='Tattha')
M['2-481'] = mg(SEVEN, JHANA, DEF, ASSOC, RESULT, {
 'abhidhamma': 'Abhidhamma', 'classification': 'bhājanīyaṃ', 'finished': NDE})
M['2-10-3-0'] = mg(QA)
M['2-483'] = {
 'awakening': 'bojjhaṅgānaṃ', 'Awakening Factors': 'bojjhaṅgānaṃ', 'awakening factors': 'bojjhaṅgānaṃ',
 'conflict': 'saraṇā', 'factors': 'bojjhaṅgānaṃ', 'free': 'araṇā', 'involve': 'saraṇā', 'neutral': 'abyākatā',
 'unwholesome': 'akusalā', 'wholesome': 'kusalā'}
M['2-10-3-1-0'] = {'triads': 'Tikaṃ'}
M['2-484'] = {
 'abandoned': 'pahātabbā', 'able': 'upādāniyā', 'accompanied': 'sahagato',
 'accompanied by equanimity': 'upekkhāsahagato', 'accompanied by happiness': 'sukhasahagato',
 'accompanied by joy': 'pītisahagato', 'accumulation': 'ācaya', 'arise': 'uppādino', 'arisen': 'uppannā',
 'associated': 'sampayutto', 'awakening': 'sambojjhaṅgo', 'awakening factor': 'sambojjhaṅgo',
 'Awakening Factors': 'bojjhaṅgā', 'awakening factors': 'bojjhaṅgā', 'belong': NDE, 'beyond': 'asekkhā',
 'birth': NDE, 'cause': 'hetukā', 'causes': 'hetukā', 'clung': 'upādāniyā', 'connected': 'saṃkilesikā',
 'connected with defilement': 'saṃkilesikā', 'defilement': 'saṃkilesikā', 'describable': 'vattabbā',
 'dismantling': 'apacaya', 'dominant': 'ādhipatino', 'dominant factor': 'ādhipatino', 'due to arise': 'uppādino',
 'equanimity': 'upekkhā', 'examination': 'vicārā', 'external': 'bahiddhā', 'external objects': 'Bahiddhārammaṇā',
 'factor': 'sambojjhaṅgo', 'factor of joy': 'Pītisambojjhaṅgo', 'factors': 'bojjhaṅgā', 'feeling': 'vedanāya',
 'fixed': 'niyatā', 'future object': 'anāgatārammaṇā', 'happiness': 'sukha', 'having': NDE,
 'internal': 'ajjhattā', 'internal and external': 'ajjhattabahiddhā', 'invisible': 'Anidassana',
 'invisible and offer': 'Anidassanaappaṭighā', 'joy': 'pīti', 'leading to dismantling': 'apacayagāmino',
 'measureless': 'Appamāṇā', 'measureless objects': 'Appamāṇārammaṇā', 'meditative': 'bhāvanāya',
 'meditative development': 'bhāvanāya', 'neither-painful-nor-pleasant': 'adukkhamasukhāya', 'neutral': 'abyākatā',
 'object': 'ārammaṇā', 'objects': 'ārammaṇā', 'past object': 'atītārammaṇā', 'path': 'magga',
 'pleasant': 'sukhāya', 'pleasant feeling': 'sukhāya vedanāya', 'present object': 'paccuppannārammaṇā',
 'refined': 'Paṇītā', 'resistance': 'appaṭighā', 'rightness': 'sammatta', 'seeing': 'dassanena',
 'subject to result': 'vipākadhammadhammā', 'things': 'dhammā', 'things subject': 'vipākadhammadhammā',
 'thought': 'vitakka', 'training': 'sekkhā', 'undefiled': 'Asaṃkiliṭṭha', 'unfixed': 'aniyatā',
 'wholesome': 'kusalā'}
M['2-10-3-2-0'] = {'pairs': 'Dukaṃ'}
M['2-485'] = mg(QA, {
 'abandoned': 'pahātabbā', 'accompanied': 'sahagato', 'accompanied by equanimity': 'upekkhāsahagato',
 'accompanied by happiness': 'sukhasahagato', 'accompanied by joy': 'pītisahagato', 'along': 'ānuparivattino',
 'analysis': 'vibhaṅgo', 'arise': 'sahabhuno', 'associated': 'sampayuttā', 'awakening': 'sambojjhaṅgo',
 'awakening factor': 'sambojjhaṅgo', 'Awakening Factors': 'Bojjhaṅga', 'awakening factors': 'bojjhaṅgā',
 'belong': NDE, 'beyond': 'Lokuttarā', 'birth': NDE, 'cannot': 'na', 'causes': 'hetukā', 'clinging': 'upādānā',
 'conditioned': 'Saṅkhatā', 'conflict': 'Araṇā', 'conjoined': 'saṃsaṭṭha', 'defilements': 'kilesā',
 'derived': 'upādā', 'describable': 'vattabbā', 'dissociated': 'vippayuttā', 'equanimity': 'upekkhā',
 'examination': 'vicārā', 'external': 'Bāhirā', 'factor': 'sambojjhaṅgo',
 'factor of investigation': 'Dhammavicayasambojjhaṅgo', 'factor of joy': 'Pītisambojjhaṅgo', 'factors': 'bojjhaṅgā',
 'fetters': 'saṃyojanā', 'fine-material': 'rūpāvacarā', 'fine-material sphere': 'rūpāvacarā', 'finished': 'niṭṭhito',
 'fixed': 'niyatā', 'floods': 'oghā', 'follow': 'ānuparivattino', 'free': 'Araṇā', 'grasping': 'parāmāsā',
 'happiness': 'sukha', 'having': 'sahetukā', 'hindrances': 'nīvaraṇā', 'immaterial': 'Arūpā',
 'immaterial sphere': 'arūpāvacarā', 'investigation': 'vicaya', 'investigation of things': 'Dhammavicaya',
 'invisible': 'Anidassanā', 'joy': 'pīti', 'known': 'viññeyyā', 'means': 'Kenaci', 'meditative': 'bhāvanāya',
 'meditative development': 'bhāvanāya', 'mental': 'Cetasikā', 'mental factors': 'Cetasikā', 'mental taints': 'āsavā',
 'mind': 'Citta', 'minds': 'cittā', 'non-root': 'na hetū', 'objects': 'sārammaṇā', 'originated': 'samuṭṭhānā',
 'resistance': 'Appaṭighā', 'root': 'hetu', 'roots': 'hetū', 'seeing': 'dassanena', 'sense': 'kāmāvacarā',
 'sense sphere': 'kāmāvacarā', 'sphere': 'āvacarā', 'subject to mental': 'sāsavā', 'taints': 'āsavā',
 'things': 'Dhamma', 'thought': 'vitakkā', 'ties': 'ganthā', 'together': 'saha', 'unfixed': 'aniyatā',
 'unsurpassed': 'Anuttarā', 'wrong': 'parāmāsā', 'wrong grasping': 'parāmāsā', 'yokes': 'yogā'})

out, missing = [], []
for line in (d / f'{ch}.keywords.md').read_text(encoding='utf-8').splitlines():
    sid, kws = line.split('] ', 1)
    sid = sid[1:]
    m = M[sid]
    pairs = []
    for k in kws.split(', '):
        k = k.strip()
        if k not in m:
            missing.append((sid, k)); pairs.append(f'???={k}')
        else:
            pairs.append(f'{m[k]}={k}')
    out.append(f'[{sid}] ' + ', '.join(pairs))
(d / f'{ch}.mapped.md').write_text('\n'.join(out) + '\n', encoding='utf-8')
print('written', len(out), 'missing', missing)
