import pathlib
d = pathlib.Path(__file__).parent
ch = '11-maggangavibhango'
NDE = '(no direct equivalent)'

# bare list of the noble eightfold path (2-486, 2-488, 2-504)
NOBLE8 = {
 'concentration': 'samādhi', 'effort': 'vāyāmo', 'eightfold': 'aṭṭhaṅgiko', 'eightfold path': 'aṭṭhaṅgiko maggo',
 'intention': 'saṅkappo', 'livelihood': 'ājīvo', 'mindfulness': 'sati', 'namely': 'seyyathidaṃ', 'noble': 'Ariyo',
 'path': 'maggo', 'right': 'sammā', 'speech': 'vācā', 'view': 'diṭṭhi',
}
# bare list of the fivefold path (2-493, 2-496, 2-500, 2-502)
FIVE = {
 'concentration': 'samādhi', 'effort': 'vāyāmo', 'fivefold': 'Pañcaṅgiko', 'fivefold path': 'Pañcaṅgiko maggo',
 'intention': 'saṅkappo', 'mindfulness': 'sati', 'path': 'maggo', 'right': 'sammā', 'view': 'diṭṭhi',
}
# supramundane first-jhāna occasion formula (2-491, 2-494, 2-497, 2-499, 2-501, 2-503)
OCC = {
 'abandoning': 'pahānāya', 'abandoning of views': 'diṭṭhigatānaṃ pahānāya', 'absorption': 'jhānaṃ',
 'beyond': 'lokuttaraṃ', 'concentration': 'samādhi', 'develops': 'bhāveti', 'develops the meditative': 'jhānaṃ bhāveti',
 'difficult': 'dukkhapaṭipadaṃ', 'difficult practice': 'dukkhapaṭipadaṃ', 'direct': 'ābhiññaṃ',
 'direct knowledge': 'ābhiññaṃ', 'dismantling': 'apacaya', 'dwells': 'viharati', 'enters': 'upasampajja',
 'enters and dwells': 'upasampajja viharati', 'knowledge': 'ābhiññaṃ', 'leading to dismantling': 'apacayagāmiṃ',
 'meditative': 'jhānaṃ', 'meditative absorption': 'jhānaṃ', 'Meditative absorption': 'jhānaṃ', 'monk': 'bhikkhu',
 'occasion': 'samaye', 'path': 'maggo', 'pleasures': 'kāmehi', 'practice': 'paṭipadaṃ',
 'practice and slow': 'dukkhapaṭipadaṃ dandhābhiññaṃ', 'reaching': 'pattiyā', 'right': 'sammā',
 'secluded': 'vivicceva', 'secluded from sense': 'vivicceva kāmehi', 'sense': 'kāmehi', 'sense pleasures': 'kāmehi',
 'slow': 'dandhābhiññaṃ', 'slow direct': 'dandhābhiññaṃ', 'slow direct knowledge': 'dandhābhiññaṃ',
 'stage': 'bhūmiyā', 'therein': 'Tattha', 'view': 'diṭṭhi', 'views': 'diṭṭhigatānaṃ',
}
# resultant (vipāka) extension (2-499, 2-501, 2-503)
VIPAKA = {
 'associated': 'sampayuttā', 'contact': 'phasso', 'developed': 'bhāvitattā', 'done': 'katattā',
 'emptiness': 'suññataṃ', 'non-distraction': 'avikkhepo', 'remaining': 'Avasesā', 'remaining things': 'Avasesā dhammā',
 'things': 'dhammā', 'things are wholesome': 'dhammā kusalā', 'wholesome': 'kusalā',
 'wholesome meditative': 'kusalassa jhānassa', 'wholesome meditative absorption': 'kusalassa jhānassa',
}
# Abhidhamma definitions of the path factors (2-492, 2-495, 2-497, 2-503)
DEF = {
 'associated': 'sampayuttā', 'awakening': 'sambojjhaṅgo', 'awakening factor': 'sambojjhaṅgo', 'factor': 'aṅgaṃ',
 'factor of concentration': 'samādhisambojjhaṅgo', 'factor of energy': 'vīriyasambojjhaṅgo',
 'factor of investigation': 'dhammavicayasambojjhaṅgo', 'factor of mindfulness': 'satisambojjhaṅgo',
 'initiation': 'ārambho', 'initiation of energy': 'vīriyārambho', 'investigation': 'vicayo',
 'investigation of things': 'dhammavicayo', 'mental': 'cetasiko', 'mental initiation': 'cetasiko vīriyārambho',
 'mind': 'cittassa', 'non-delusion': 'amoho', 'path factor': 'maggaṅgaṃ', 'recollection': 'anussati',
 'remaining': 'Avasesā', 'remaining things': 'Avasesā dhammā', 'steadiness': 'ṭhiti', 'things': 'dhammā',
 'thinking': 'takko', 'thought': 'vitakko', 'understanding': 'pajānanā', 'wisdom': 'paññā', 'therein': 'Tattha',
 'right': 'sammā', 'view': 'diṭṭhi', 'concentration': 'samādhi',
}
QA = {'answers': NDE, 'questions': 'Pañhā', 'Questions and Answers': 'Pañhāpucchakaṃ', 'section': NDE,
      'Section of Questions': 'Pañhāpucchakaṃ'}

M = {}
M['2-11-0'] = {'analysis': 'vibhaṅgo', 'factors': 'aṅga', 'path': 'Magga', 'Path Factors': 'Maggaṅga',
               'path factors': 'Maggaṅga'}
M['2-11-1-0'] = {'classification': 'bhājanīyaṃ', 'discourses': 'Suttanta'}
M['2-486'] = dict(NOBLE8)
M['2-487'] = {
 'abandoned': 'pahāya', 'abandoning': 'pahānāya', 'abandoning of happiness': 'sukhassa ca pahānā',
 'absorption': 'jhānaṃ', 'abstaining': 'veramaṇī', 'abstaining from false': 'Musāvādā veramaṇī',
 'abstaining from killing': 'Pāṇātipātā veramaṇī', 'abstaining from sexual': 'kāmesumicchācārā veramaṇī',
 'abstaining from taking': 'adinnādānā veramaṇī', 'ardent': 'ātāpī', 'arisen': 'uppannānaṃ', 'arising': 'uppādāya',
 'away': 'virāgā', 'beings': 'Pāṇātipātā', 'body': 'kāye', 'born': 'vivekajaṃ', 'cessation': 'nirodhe',
 'cessation of suffering': 'dukkhanirodhe', 'chatter': 'samphappalāpā', 'clearly': 'sampajāno',
 'comprehending': 'sampajāno', 'concentration': 'samādhi', 'confidence': 'sampasādanaṃ', 'contemplating': 'ānupassī',
 'contemplating feelings': 'vedanānupassī', 'contemplating mental': 'dhammānupassī',
 'contemplating mental objects': 'dhammānupassī', 'contemplating the body': 'kāyānupassī',
 'contemplating the mind': 'cittānupassī', 'covetousness': 'abhijjhā', 'covetousness and grief': 'abhijjhādomanassaṃ',
 'declare': 'ācikkhanti', 'desire': 'chandaṃ', 'disappearance': 'atthaṅgamā', 'disciple': 'sāvako',
 'divisive': 'pisuṇāya', 'dwells': 'viharati', 'dwells contemplating': 'kāyānupassī viharati',
 'dwells contemplating feelings': 'vedanānupassī viharati', 'dwells contemplating mental': 'dhammānupassī viharati',
 'dwells happily': 'sukhavihārī', 'effort': 'vāyāmo', 'endeavours': 'padahati', 'enters': 'upasampajja',
 'enters and dwells': 'upasampajja viharati', 'equanimity': 'upekkhā', 'equanimous': 'upekkhako', 'evil': 'pāpakānaṃ',
 'examination': 'vicāraṃ', 'exerts': 'paggaṇhāti', 'exerts his mind': 'cittaṃ paggaṇhāti', 'expansion': 'vepullāya',
 'experiences': 'paṭisaṃvedeti', 'experiences happiness': 'sukhañca / paṭisaṃvedeti', 'fading': 'virāgā',
 'false': 'Musā', 'false speech': 'Musāvādā', 'feelings': 'vedanāsu', 'feelings in feelings': 'vedanāsu vedanānupassī',
 'fourth meditative': 'catutthaṃ jhānaṃ', 'fourth meditative absorption': 'catutthaṃ jhānaṃ', 'generates': 'janeti',
 'generates desire': 'chandaṃ janeti', 'grief': 'domanassaṃ', 'grief with regard': 'loke abhijjhādomanassaṃ',
 'happily': 'sukhavihārī', 'happiness': 'sukhaṃ', 'harmlessness': 'avihiṃsā', 'harsh': 'pharusāya', 'having': NDE,
 'idle': 'samphappalāpā', 'initiates': 'ārabhati', 'initiates energy': 'vīriyaṃ ārabhati', 'inner': 'ajjhattaṃ',
 'intention': 'saṅkappo', 'joy': 'pīti', 'Joy and happiness': 'pītisukhaṃ', 'killing': 'ātipātā',
 'killing living': 'Pāṇātipātā', 'knowledge': 'ñāṇaṃ', 'livelihood': 'ājīvo', 'living': 'jīvikaṃ', 'makes': 'kappeti',
 'meditative': 'jhānaṃ', 'Meditative absorption': 'jhānaṃ', 'meditative absorption': 'jhānaṃ', 'mental': 'dhammesu',
 'mental objects': 'dhammesu', 'mind': 'cittaṃ', 'mindful': 'satimā', 'mindfulness': 'sati',
 'misconduct': 'micchācārā', 'monk': 'bhikkhu', 'monk dwells': 'bhikkhu / viharati',
 'monk dwells contemplating': 'bhikkhu / kāyānupassī viharati', 'monk generates': 'bhikkhu / janeti',
 'monk generates desire': 'bhikkhu / chandaṃ janeti', 'noble': 'ariya', 'non-arising': 'anuppādāya',
 'non-confusion': 'asammosāya', 'non-ill-will': 'abyāpāda', 'objects': 'dhammesu',
 'objects in mental': 'dhammesu dhammānupassī', 'ones': 'ariyā', 'origin': 'samudaye',
 'origin of suffering': 'dukkhasamudaye', 'pain': 'dukkhassa', 'painful': 'adukkhamasukhaṃ',
 'painful nor pleasant': 'adukkhamasukhaṃ', 'perfection': 'pāripūriyā', 'persistence': 'ṭhitiyā',
 'pleasant': 'adukkhamasukhaṃ', 'pleasures': 'kāmehi', 'purity': 'pārisuddhiṃ', 'regard': 'loke',
 'removed': 'vineyya', 'removed covetousness': 'vineyya / abhijjhā', 'renunciation': 'Nekkhamma', 'right': 'sammā',
 'secluded': 'vivicca', 'secluded from sense': 'vivicceva kāmehi', 'seclusion': 'viveka', 'sense': 'kāmehi',
 'sense pleasures': 'kāmehi', 'sexual': 'kāmesu', 'speech': 'vācā', 'stilling': 'vūpasamā',
 'stilling of thought': 'vitakkavicārānaṃ vūpasamā', 'strives': 'vāyamati', 'suffering': 'Dukkhe', 'taking': 'ādānā',
 'therein': 'Tattha', 'things': 'dhammānaṃ', 'thought': 'vitakkaṃ', 'thought and examination': 'vitakkavicārānaṃ',
 'unification': 'ekodibhāvaṃ', 'unwholesome': 'akusalānaṃ', 'unwholesome things': 'akusalānaṃ dhammānaṃ',
 'view': 'diṭṭhi', 'wholesome': 'kusalānaṃ', 'wholesome things': 'kusalānaṃ dhammānaṃ', 'wrong': 'micchā',
}
M['2-488'] = dict(NOBLE8)
M['2-489'] = {
 'cessation': 'nirodha', 'classification': 'bhājanīyaṃ', 'concentration': 'samādhiṃ', 'develops': 'bhāveti',
 'discourses': 'Suttanta', 'dispassion': 'virāga', 'effort': 'vāyāmaṃ', 'finished': NDE, 'intention': 'saṅkappaṃ',
 'livelihood': 'ājīvaṃ', 'mindfulness': 'satiṃ', 'monk': 'bhikkhu', 'monk develops': 'bhikkhu / bhāveti',
 'release': 'vossagga', 'right': 'sammā', 'ripening': 'pariṇāmiṃ', 'seclusion': 'viveka', 'speech': 'vācaṃ',
 'therein': 'Tattha', 'view': 'diṭṭhiṃ',
}
M['2-11-2-0'] = {'abhidhamma': 'Abhidhamma', 'classification': 'bhājanīyaṃ'}
M['2-490'] = dict(NOBLE8, **{'eightfold': 'Aṭṭhaṅgiko', 'eightfold path': 'Aṭṭhaṅgiko maggo'})
M['2-491'] = dict(OCC, **{'eightfold': 'aṭṭhaṅgiko', 'eightfold path': 'aṭṭhaṅgiko maggo'})
M['2-492'] = dict(DEF, **{
 'absorption': 'appanā', 'abstaining': 'virati', 'abstinence': 'veramaṇī', 'application': 'abhiniropanā',
 'bodily': 'kāya', 'bodily misconduct': 'kāyaduccaritehi', 'Bodily misconduct': 'kāyaduccaritehi', 'bridge': 'setu',
 'committing': 'akaraṇaṃ', 'desisting': 'paṭivirati', 'destroying': 'ghāto', 'doing': 'akiriyā', 'effort': 'vāyāmo',
 'eightfold': 'aṭṭhaṅgiko', 'eightfold path': 'aṭṭhaṅgiko maggo', 'intention': 'saṅkappo', 'kinds': NDE,
 'limit': 'velā', 'livelihood': 'ājīvo', 'mind': 'cetaso', 'mindfulness': 'sati', 'misconduct': 'duccaritehi',
 'overstepping': 'anatikkamo', 'path': 'maggo', 'refraining': 'ārati', 'speech': 'vācā',
 'transgressing': 'anajjhāpatti', 'verbal': 'vacī', 'verbal misconduct': 'vacīduccaritehi', 'wrong': 'micchā'})
M['2-493'] = dict(FIVE)
M['2-494'] = dict(OCC, **{'effort': 'vāyāmo', 'fivefold': 'pañcaṅgiko', 'fivefold path': 'pañcaṅgiko maggo',
                          'intention': 'saṅkappo', 'mindfulness': 'sati'})
M['2-495'] = dict(DEF, **{'effort': 'vāyāmo', 'fivefold': 'pañcaṅgiko', 'fivefold path': 'pañcaṅgiko maggo',
                          'intention': 'saṅkappo', 'mindfulness': 'sati', 'path': 'maggo'})
M['2-496'] = dict(FIVE)
M['2-497'] = dict(OCC, **DEF)
M['2-497'].update({'effort': 'vāyāmena', 'intention': 'saṅkappena', 'mindfulness': 'satiyā', 'path': 'maggaṅgaṃ'})
M['2-498'] = {'concentration': 'samādhi', 'eightfold': 'Aṭṭhaṅgiko', 'eightfold path': 'Aṭṭhaṅgiko maggo',
              'path': 'maggo', 'right': 'sammā', 'view': 'diṭṭhi'}
M['2-499'] = dict(OCC, **VIPAKA)
M['2-499'].update({'eightfold': 'aṭṭhaṅgiko', 'eightfold path': 'aṭṭhaṅgiko maggo'})
M['2-500'] = dict(FIVE)
M['2-501'] = dict(OCC, **VIPAKA)
M['2-501'].update({'effort': 'vāyāmo', 'fivefold': 'pañcaṅgiko', 'fivefold path': 'pañcaṅgiko maggo',
                   'intention': 'saṅkappo', 'mindfulness': 'sati'})
M['2-502'] = dict(FIVE)
M['2-503'] = dict(OCC, **DEF)
M['2-503'].update(VIPAKA)
M['2-503'].update({
 'abhidhamma': 'Abhidhamma', 'calm': 'samatho', 'classification': 'bhājanīyaṃ', 'effort': 'vāyāmena',
 'faculty': 'indriyaṃ', 'faculty of concentration': 'samādhindriyaṃ', 'finished': NDE, 'intention': 'saṅkappena',
 'mindfulness': 'satiyā', 'non-wavering': 'avisāhāro', 'path': 'maggaṅgaṃ', 'power': 'balaṃ',
 'stability': 'saṇṭhiti', 'standing': 'avaṭṭhiti', 'undistracted': 'avisāhaṭa'})
M['2-11-3-0'] = dict(QA)
M['2-504'] = dict(NOBLE8)
M['2-505'] = {
 'conflict': 'saraṇā', 'factors': 'aṅgānaṃ', 'free': 'araṇā', 'involve': 'saraṇā', 'neutral': 'abyākatā',
 'path': 'maggaṅgānaṃ', 'Path Factors': 'maggaṅgānaṃ', 'path factors': 'maggaṅgānaṃ', 'unwholesome': 'akusalā',
 'wholesome': 'kusalā',
}
M['2-11-3-1-0'] = {'triads': 'Tikaṃ'}
M['2-506'] = {
 'abandoned': 'pahātabbā', 'able': 'anupādāniyā', 'accompanied': 'sahagato',
 'accompanied by equanimity': 'upekkhāsahagato', 'accompanied by happiness': 'sukhasahagato',
 'accompanied by joy': 'pītisahagato', 'accumulation': 'ācaya', 'arise': 'uppādino', 'arisen': 'uppannā',
 'associated': 'sampayutto', 'belong': NDE, 'beyond': 'asekkhā', 'birth': NDE, 'cause': 'hetukā',
 'causes': 'hetukā', 'clung': 'anupādāniyā', 'connected': 'asaṃkilesikā', 'connected with defilement': 'asaṃkilesikā',
 'defilement': 'saṃkilesikā', 'describable': 'vattabbā', 'dismantling': 'apacayagāmino', 'dominant': 'ādhipatino',
 'dominant factor': 'ādhipatino', 'due to arise': 'uppādino', 'equanimity': 'upekkhā', 'examination': 'vicāra',
 'external': 'bahiddhā', 'external objects': 'Bahiddhārammaṇā', 'factor': 'ādhipatino', 'factors': 'maggaṅgā',
 'feeling': 'vedanāya', 'fixed': 'niyatā', 'future object': 'anāgatārammaṇā', 'happiness': 'sukha', 'having': NDE,
 'intention': 'saṅkappo', 'internal': 'ajjhattā', 'internal and external': 'ajjhattabahiddhā',
 'invisible': 'Anidassana', 'invisible and offer': 'Anidassanaappaṭighā', 'joy': 'pīti',
 'leading to dismantling': 'apacayagāmino', 'measureless': 'Appamāṇā', 'measureless objects': 'Appamāṇārammaṇā',
 'meditative': 'bhāvanāya', 'meditative development': 'bhāvanāya', 'neither-painful-nor-pleasant': 'adukkhamasukhāya',
 'neutral': 'abyākatā', 'object': 'ārammaṇā', 'objects': 'ārammaṇā', 'past object': 'atītārammaṇā', 'path': 'magga',
 'Path Factors': 'maggaṅgā', 'path factors': 'maggaṅgā', 'pleasant': 'sukhāya', 'pleasant feeling': 'sukhāya vedanāya',
 'present object': 'paccuppannārammaṇā', 'refined': 'Paṇītā', 'resistance': 'appaṭighā', 'right': 'Sammā',
 'rightness': 'sammatta', 'seeing': 'dassanena', 'subject to result': 'vipākadhammadhammā',
 'things': 'vipākadhammadhammā', 'things subject': 'vipākadhammadhammā', 'thought': 'vitakka', 'training': 'sekkhā',
 'undefiled': 'Asaṃkiliṭṭha', 'unfixed': 'aniyatā', 'wholesome': 'kusalā',
}
M['2-11-3-2-0'] = {'pairs': 'Dukaṃ'}
M['2-507'] = dict(QA, **{
 'abandoned': 'pahātabbā', 'accompanied': 'sahagato', 'accompanied by equanimity': 'upekkhāsahagatā',
 'accompanied by happiness': 'sukhasahagato', 'accompanied by joy': 'pītisahagato', 'along': 'ānuparivattino',
 'analysis': 'vibhaṅgo', 'arise': 'sahabhuno', 'associated': 'sampayuttā', 'belong': NDE, 'beyond': 'Lokuttarā',
 'birth': NDE, 'cannot': 'na', 'causes': 'hetukā', 'clinging': 'upādānā', 'conditioned': 'Saṅkhatā',
 'conflict': 'Araṇāti', 'conjoined': 'saṃsaṭṭhā', 'defilements': 'kilesā', 'derived': 'upādā',
 'describable': 'vattabbā', 'dissociated': 'vippayuttā', 'equanimity': 'upekkhā', 'examination': 'vicāro',
 'external': 'Bāhirā', 'factors': 'maggaṅgā', 'fetters': 'saṃyojanā', 'fine-material': 'rūpāvacarā',
 'fine-material sphere': 'rūpāvacarā', 'finished': 'niṭṭhito', 'fixed': 'niyatā', 'floods': 'oghā',
 'follow': 'ānuparivattino', 'free': 'Araṇāti', 'grasping': 'parāmāsā', 'happiness': 'sukha', 'having': 'sahetukā',
 'hindrances': 'nīvaraṇā', 'immaterial': 'Arūpā', 'immaterial sphere': 'arūpāvacarā', 'intention': 'saṅkappo',
 'invisible': 'Anidassanā', 'joy': 'pīti', 'known': 'viññeyyā', 'means': 'Kenaci', 'meditative': 'bhāvanāya',
 'meditative development': 'bhāvanāya', 'mental': 'Cetasikā', 'mental factors': 'Cetasikā', 'mental taints': 'āsavā',
 'mind': 'Citta', 'minds': 'cittā', 'non-root': 'na hetu', 'objects': 'sārammaṇā', 'originated': 'samuṭṭhānā',
 'path': 'maggaṅgā', 'Path Factors': 'Maggaṅga', 'path factors': 'maggaṅgā', 'resistance': 'Appaṭighā',
 'right': 'Sammā', 'root': 'hetu', 'roots': 'hetū', 'seeing': 'dassanena', 'sense': 'kāmāvacarā',
 'sense sphere': 'kāmāvacarā', 'sphere': 'āvacarā', 'subject to mental': 'sāsavā', 'taints': 'āsavā',
 'thought': 'vitakkā', 'ties': 'ganthā', 'together': 'saha', 'unfixed': 'aniyatā', 'unsurpassed': 'Anuttarā',
 'view': 'diṭṭhi', 'wrong': 'parāmāsā', 'wrong grasping': 'parāmāsā', 'yokes': 'yogā',
})

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
