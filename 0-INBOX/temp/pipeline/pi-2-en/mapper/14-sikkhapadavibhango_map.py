import pathlib
d = pathlib.Path(__file__).parent
ch = '14-sikkhapadavibhango'
NDE = '(no direct equivalent)'


def mg(*ds, **kw):
    r = {}
    for x in ds:
        r.update(x)
    r.update(kw)
    return r


# names of the five training rules
RULES = {
 'abstaining': 'veramaṇī', 'abstaining from false': 'musāvādā veramaṇī',
 'abstaining from killing': 'pāṇātipātā veramaṇī', 'abstaining from sexual': 'kāmesumicchācārā veramaṇī',
 'abstaining from taking': 'adinnādānā veramaṇī', 'abstaining from wine': 'surāmerayamajjapamādaṭṭhānā veramaṇī',
 'beings': 'pāṇātipātā', 'cause': 'ṭṭhānā', 'false': 'musā', 'false speech': 'musāvādā',
 'heedlessness': 'pamāda', 'intoxicants': 'majja', 'killing': 'ātipātā', 'killing living': 'pāṇātipātā',
 'living': 'pāṇātipātā', 'misconduct': 'micchācārā', 'rule': 'padaṃ', 'rule of abstaining': 'veramaṇī sikkhāpadaṃ',
 'rules': 'padāni', 'sexual': 'kāmesu', 'speech': 'vādā', 'spirits': 'meraya', 'taking': 'ādānā',
 'training': 'sikkhā', 'training rule': 'sikkhāpadaṃ', 'training rules': 'sikkhāpadāni',
 'Training Rules': 'sikkhāpadāni', 'wine': 'surā',
}
# the sense-sphere wholesome mind formula and the definitions of the rule
DEF = mg(RULES, {
 'abstinence': 'veramaṇī', 'accompanied': 'sahagataṃ', 'accompanied by equanimity': 'upekkhāsahagataṃ',
 'accompanied by joy': 'somanassasahagataṃ', 'arisen': 'uppannaṃ', 'associated': 'sampayuttā', 'bridge': 'setu',
 'committing': 'akaraṇaṃ', 'contact': 'phasso', 'desisting': 'paṭivirati', 'destroying': 'ghāto',
 'dissociated': 'vippayuttaṃ', 'dissociated from knowledge': 'ñāṇavippayuttaṃ', 'doing': 'akiriyā',
 'equanimity': 'upekkhā', 'exertion': 'paggāho', 'intending': 'sañcetanā', 'intention': 'cetanā',
 'joy': 'somanassa', 'knowledge': 'ñāṇa', 'limit': 'velā', 'mind': 'cittaṃ', 'non-distraction': 'avikkhepo',
 'occasion': 'samaye', 'overstepping': 'anatikkamo', 'prompting': 'sasaṅkhārena', 'refraining': 'ārati',
 'remaining': 'Avasesā', 'remaining things': 'Avasesā dhammā', 'sense': 'kāmāvacaraṃ',
 'sense sphere': 'kāmāvacaraṃ', 'sphere': 'āvacaraṃ', 'sphere has arisen': 'kāmāvacaraṃ / uppannaṃ',
 'state of intending': 'sañcetayitattaṃ', 'therein': 'Tattha', 'things': 'dhammā',
 'transgressing': 'anajjhāpatti', 'wholesome': 'kusalaṃ', 'wholesome mind': 'kusalaṃ cittaṃ',
})
# inferior / middling / refined and the four dominants
DOM = {
 'desire': 'chandādhipateyyaṃ', 'dominant': 'ādhipateyyaṃ', 'dominant factor': 'ādhipateyyaṃ',
 'factor': 'ādhipateyyaṃ', 'inferior': 'hīnaṃ', 'investigation': 'vīmaṃsādhipateyyaṃ', 'middling': 'majjhimaṃ',
 'refined': 'paṇītaṃ',
}
JHANA = {
 'abandoning': 'pahānāya', 'abandoning of views': 'diṭṭhigatānaṃ pahānāya', 'absorption': 'jhānaṃ',
 'beyond': 'lokuttaraṃ', 'develops': 'bhāveti', 'develops the meditative': 'jhānaṃ bhāveti',
 'difficult': 'dukkhapaṭipadaṃ', 'difficult practice': 'dukkhapaṭipadaṃ', 'direct': 'ābhiññaṃ',
 'direct knowledge': 'ābhiññaṃ', 'dismantling': 'apacaya', 'dwells': 'viharati', 'enters': 'upasampajja',
 'enters and dwells': 'upasampajja viharati', 'knowledge': 'ābhiññaṃ', 'leading to dismantling': 'apacayagāmiṃ',
 'meditative': 'jhānaṃ', 'meditative absorption': 'jhānaṃ', 'Meditative absorption': 'jhānaṃ',
 'occasion': 'samaye', 'pleasures': 'kāmehi', 'practice': 'paṭipadaṃ',
 'practice and slow': 'dukkhapaṭipadaṃ dandhābhiññaṃ', 'reaching': 'pattiyā', 'secluded': 'vivicceva',
 'secluded from sense': 'vivicceva kāmehi', 'sense': 'kāmehi', 'sense pleasures': 'kāmehi',
 'slow': 'dandhābhiññaṃ', 'slow direct': 'dandhābhiññaṃ', 'slow direct knowledge': 'dandhābhiññaṃ',
 'stage': 'bhūmiyā', 'views': 'diṭṭhigatānaṃ',
}
QA = {'answers': NDE, 'questions': 'Pañhā', 'Questions and Answers': 'Pañhāpucchakaṃ', 'section': NDE,
      'Section of Questions': 'Pañhāpucchakaṃ'}

M = {}
M['2-14-0'] = {'analysis': 'vibhaṅgo', 'rules': 'pada', 'training': 'Sikkhā', 'training rules': 'Sikkhāpada',
               'Training Rules': 'Sikkhāpada'}
M['2-14-1-0'] = {'abhidhamma': 'Abhidhamma', 'classification': 'bhājanīyaṃ'}
for s in ('2-703', '2-708', '2-714'):
    M[s] = dict(RULES)
for s in ('2-704', '2-705', '2-706', '2-707'):
    M[s] = dict(DEF)
M['2-709'] = mg(DEF, DOM)
# 2-710 / 2-711 have the intention only in "associated with the intention" (cetanāya)
M['2-710'] = mg(DEF, DOM, {'intention': 'cetanāya'})
M['2-711'] = mg(DEF, DOM, {'sense': 'kāmāvacare', 'sense sphere': 'kāmāvacare', 'sphere': 'āvacare',
                           'sphere has arisen': 'kāmāvacare / uppannaṃ', 'intention': 'cetanāya'})
M['2-712'] = mg(DEF, {
 'associated': 'sampayuttaṃ', 'mental': 'dhammārammaṇaṃ', 'mental object': 'dhammārammaṇaṃ',
 'object': 'ārammaṇaṃ', 'sight': 'rūpārammaṇaṃ', 'things are training': 'dhammā sikkhā',
 'whatever': 'yaṃ yaṃ vā panārabbha'})
M['2-713'] = mg(JHANA, {
 'abhidhamma': 'Abhidhamma', 'classification': 'bhājanīyaṃ', 'contact': 'phasso',
 'develops the path': 'maggaṃ bhāveti', 'fine-material': 'rūpūpapattiyā', 'fine-material sphere': 'rūpūpapattiyā',
 'finished': NDE, 'immaterial': 'arūpūpapattiyā', 'immaterial sphere': 'arūpūpapattiyā',
 'non-distraction': 'avikkhepo', 'path': 'maggaṃ', 'path for rebirth': 'ūpapattiyā maggaṃ', 'rebirth': 'ūpapattiyā',
 'sphere': NDE, 'things': 'dhammā', 'things are training': 'dhammā sikkhā', 'training': 'sikkhā'})
M['2-14-2-0'] = dict(QA)
M['2-715'] = {
 'conflict': 'saraṇā', 'free': 'araṇā', 'involve': 'saraṇā', 'neutral': 'abyākatā', 'rules': 'padānaṃ',
 'training': 'sikkhā', 'training rules': 'sikkhāpadānaṃ', 'Training Rules': 'sikkhāpadānaṃ',
 'unwholesome': 'akusalā', 'wholesome': 'kusalā'}
M['2-14-2-1-0'] = {'triads': 'Tikaṃ'}
M['2-716'] = {
 'abandoned': 'pahātabbā', 'able': 'upādāniyā', 'accompanied': 'sahagatā',
 'accompanied by equanimity': 'upekkhāsahagatā', 'accompanied by happiness': 'sukhasahagatā',
 'accompanied by joy': 'pītisahagatā', 'accumulation': 'ācaya', 'arise': 'uppādino', 'arisen': 'uppannā',
 'associated': 'sampayuttā', 'belong': NDE, 'beyond': 'āsekkhā', 'birth': NDE, 'cause': 'hetukā',
 'causes': 'hetukā', 'clung': 'upādāniyā', 'connected': 'saṃkilesikā', 'connected with defilement': 'saṃkilesikā',
 'defilement': 'saṃkilesikā', 'describable': 'vattabbā', 'dominant': 'ādhipatino', 'dominant factor': 'ādhipatino',
 'due to arise': 'uppādino', 'equanimity': 'upekkhā', 'examination': 'vicārā', 'external': 'bahiddhā',
 'external objects': 'bahiddhārammaṇā', 'factor': 'ādhipatino', 'feeling': 'vedanāya', 'happiness': 'sukha',
 'having': NDE, 'internal': 'ajjhattā', 'internal and external': 'ajjhattabahiddhā', 'invisible': 'anidassana',
 'invisible and offer': 'anidassanaappaṭighā', 'joy': 'pīti', 'leading to accumulation': 'ācayagāmino',
 'limited': 'parittā', 'meditative': 'bhāvanāya', 'meditative development': 'bhāvanāya', 'middling': 'majjhimā',
 'neither-painful-nor-pleasant': 'adukkhamasukhāya', 'object': 'ārammaṇā', 'objects': 'ārammaṇā', 'path': 'magga',
 'pleasant': 'sukhāya', 'pleasant feeling': 'sukhāya vedanāya', 'resistance': 'appaṭighā', 'seeing': 'dassanena',
 'subject to result': 'vipākadhammadhammā', 'things': 'dhammā', 'things subject': 'vipākadhammadhammā',
 'thought': 'vitakka', 'training': 'sekkha', 'undefiled': 'asaṃkiliṭṭha', 'unfixed': 'aniyatā',
 'wholesome': 'Kusalāyeva'}
M['2-14-2-2-0'] = {'pairs': 'Dukaṃ'}
M['2-717'] = mg(QA, {
 'abandoned': 'pahātabbā', 'accompanied': 'sahagatā', 'accompanied by equanimity': 'upekkhāsahagatā',
 'accompanied by happiness': 'sukhasahagatā', 'accompanied by joy': 'pītisahagatā', 'along': 'ānuparivattino',
 'analysis': 'vibhaṅgo', 'arise': 'sahabhuno', 'associated': 'sampayuttā', 'belong': NDE, 'birth': NDE,
 'cannot': 'na', 'causes': 'hetukā', 'clinging': 'upādānā', 'conditioned': 'saṅkhatā', 'conflict': 'araṇā',
 'conjoined': 'saṃsaṭṭhā', 'defilements': 'kilesā', 'derived': 'upādā', 'describable': 'vattabbā',
 'dissociated': 'vippayuttā', 'equanimity': 'upekkhā', 'examination': 'vicārā', 'external': 'bāhirā',
 'factors': 'cetasikā', 'fetters': 'saṃyojanā', 'fine-material': 'rūpāvacarā', 'fine-material sphere': 'rūpāvacarā',
 'finished': 'niṭṭhito', 'floods': 'oghā', 'follow': 'ānuparivattino', 'free': 'araṇā', 'grasping': 'parāmāsā',
 'happiness': 'sukha', 'having': 'sahetukā', 'hindrances': 'nīvaraṇā', 'immaterial': 'arūpā',
 'immaterial sphere': 'arūpāvacarā', 'invisible': 'anidassanā', 'joy': 'pīti', 'known': 'viññeyyā',
 'means': 'kenaci', 'meditative': 'bhāvanāya', 'meditative development': 'bhāvanāya', 'mental': 'cetasikā',
 'mental factors': 'cetasikā', 'mental taints': 'āsavā', 'mind': 'citta', 'minds': 'cittā', 'objects': 'sārammaṇā',
 'originated': 'samuṭṭhānā', 'resistance': 'appaṭighā', 'roots': 'hetū', 'rules': 'pada', 'seeing': 'dassanena',
 'sense': 'kāmāvacarā', 'sense sphere': 'kāmāvacarā', 'sphere': 'āvacarā', 'subject to mental': 'sāsavā',
 'surpassable': 'sauttarā', 'taints': 'āsavā', 'thought': 'vitakkā', 'ties': 'ganthā', 'together': 'saha',
 'training': 'Sikkhā', 'Training Rules': 'Sikkhāpada', 'training rules': 'Sikkhāpada', 'unfixed': 'aniyatā',
 'worldly': 'lokiyā', 'wrong': 'parāmāsā', 'wrong grasping': 'parāmāsā', 'yokes': 'yogā'})

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
