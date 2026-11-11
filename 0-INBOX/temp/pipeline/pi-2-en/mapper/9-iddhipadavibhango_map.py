import pathlib, re
d = pathlib.Path(__file__).parent
root = d.parents[4]
ch = '9-iddhipadavibhango'
NDE = '(no direct equivalent)'

# chanda/vīriya/citta/vīmaṃsā + iddhipāda are sandhi compounds (chandiddhipādo …): the leading
# member takes the whole compound, "basis of success" the trailing part.

# ---- shared blocks -------------------------------------------------------
FOURB = {  # "Cattāro iddhipādā – … chandasamādhipadhānasaṅkhārasamannāgataṃ iddhipādaṃ bhāveti …"
 'bases': 'pādā', 'bases of success': 'iddhipādā', 'Bases of Success': 'iddhipādā', 'basis of success': 'iddhipādaṃ',
 'Basis of success': 'iddhipādaṃ', 'concentration': 'samādhi', 'concentration through desire': 'chandasamādhi',
 'concentration through energy': 'vīriyasamādhi', 'concentration through investigation': 'vīmaṃsāsamādhi',
 'concentration through mind': 'cittasamādhi', 'desire': 'chanda', 'develops': 'bhāveti',
 'develops the basis': 'iddhipādaṃ bhāveti', 'Develops the basis': 'iddhipādaṃ bhāveti', 'endeavour': 'padhāna',
 'endowed': 'samannāgataṃ', 'endowed with concentration': 'samādhipadhānasaṅkhārasamannāgataṃ',
 'formations': 'saṅkhāra', 'formations of endeavour': 'padhānasaṅkhāra', 'investigation': 'vīmaṃsā',
 'mind': 'citta', 'monk': 'bhikkhu', 'monk develops': 'bhikkhu / bhāveti', 'success': 'iddhi',
 'success endowed': 'samannāgataṃ iddhipādaṃ',
}
def HEAD(lead):  # "Chandiddhipādo" etc.
    return {'Basis of success': 'iddhipādo', 'basis of success': 'iddhipādo', 'success': 'iddhi',
            'success through desire': lead, 'Success Through Desire': lead, 'success through energy': lead,
            'Success Through Energy': lead, 'Success Through Mind': lead, 'Success Through Investigation': lead,
            'desire': lead, 'mind': lead, 'investigation': lead}
VERBS = {  # the four right efforts inside the definition
 'abandoning': 'pahānāya', 'arisen': 'uppannānaṃ', 'arising': 'uppādāya', 'endeavours': 'padahati',
 'evil': 'pāpakānaṃ', 'exerts': 'paggaṇhāti', 'exerts his mind': 'cittaṃ paggaṇhāti', 'expansion': 'vepullāya',
 'generates': 'janeti', 'generates desire': 'chandaṃ janeti', 'initiates': 'ārabhati',
 'initiates energy': 'vīriyaṃ ārabhati', 'non-arising': 'anuppādāya', 'non-confusion': 'asammosāya',
 'perfection': 'pāripūriyā', 'persistence': 'ṭhitiyā', 'strives': 'vāyamati', 'things': 'dhammānaṃ',
 'unwholesome': 'akusalānaṃ', 'unwholesome things': 'akusalānaṃ dhammānaṃ', 'wholesome': 'kusalānaṃ',
 'wholesome things': 'kusalānaṃ dhammānaṃ',
}
def CONC(conc, lead, gather):  # 2-432 / 2-435 / 2-438 / 2-441
    return dict(VERBS, **{
     'basis of success': 'iddhipādaṃ', 'Basis of success': 'iddhipādaṃ', 'concentration': 'samādhiṃ',
     conc[0]: conc[1], 'desire': lead if conc[0] == 'concentration through desire' else 'chandaṃ',
     'develop': 'bhāveti', 'develop the basis': 'iddhipādaṃ bhāveti', 'dominant': 'adhipatiṃ',
     'dominant factor': 'adhipatiṃ', 'factor': 'adhipatiṃ', 'endeavour': 'padhāna', 'endowed': 'samannāgataṃ',
     'endowed with concentration': 'samādhipadhānasaṅkhārasamannāgataṃ', 'formations': 'saṅkhārā',
     'formations of endeavour': 'padhānasaṅkhārā', 'gathering': gather, 'mind': 'cittaṃ', 'monk': 'bhikkhu',
     'monk develop': 'bhikkhu / bhāveti', 'obtains': 'labhati', 'obtains concentration': 'labhati samādhiṃ',
     'one-pointedness': 'ekaggataṃ', 'one-pointedness of mind': 'cittassekaggataṃ',
     'simply': 'tveva', 'success': 'iddhi',
     'reckoned': ['saṅkhyaṃ gacchati', 'saṅkhyaṃ / gacchati'],  # 2-432 has a variant bracket in between 'simply': 'tveva', 'success': 'iddhi',
     'success endowed': 'samannāgataṃ iddhipādaṃ', 'summing': 'abhisaṅkhipitvā', 'together': 'ekajjhaṃ'})
CHANDA = {'act': 'kattu', 'desire': 'chando', 'dhamma': 'dhamma', 'wholesome': 'kusalo',
          'wholesome desire': 'kusalo dhammacchando', 'wish': 'kamyatā', 'wishing': 'chandikatā'}
SAMADHI = {'mind': 'cittassa', 'stability': 'saṇṭhiti', 'steadiness': 'ṭhiti'}
SAMADHI_FULL = dict(SAMADHI, **{
 'calm': 'samatho', 'faculty': 'indriyaṃ', 'faculty of concentration': 'samādhindriyaṃ',
 'non-distraction': 'avikkhepo', 'non-wavering': 'avisāhāro', 'power': 'balaṃ', 'standing': 'avaṭṭhiti',
 'undistracted': 'avisāhaṭa'})
FORMATION = {  # "padhānasaṅkhāro? Yo cetasiko vīriyārambho…pe… sammāvāyāmo … samannāgato"
 'concentration': 'samādhi', 'effort': 'vāyāmo', 'endeavour': 'padhāna', 'endowed': 'upeto',
 'endowed with concentration': 'samādhipadhānasaṅkhārasamannāgato', 'formation': 'saṅkhāro',
 'formation of endeavour': 'padhānasaṅkhāro', 'formations': 'saṅkhāra', 'formations of endeavour': 'padhānasaṅkhāra',
 'furnished': 'samannāgato', 'initiation': 'ārambho', 'initiation of energy': 'vīriyārambho', 'mental': 'cetasiko',
 'mental initiation': 'cetasiko vīriyārambho', 'right': 'sammā', 'therefore': 'Tena', 'therein': 'Tattha',
}
ENDOWED_FULL = {'complete': 'sampanno', 'fully': 'samupeto', 'fully endowed': 'samupeto', 'having': NDE,
                'possessed': 'upapanno'}
MINDDEF = {'activity': 'mānasaṃ', 'consciousness element': 'viññāṇadhātu', 'corresponding': 'tajjā',
           'element': 'dhātu', 'mental': 'mānasaṃ', 'mental activity': 'mānasaṃ', 'mentality': 'mano',
           'mind': 'cittaṃ', 'mind-consciousness': 'manoviññāṇa', 'mind-consciousness element': 'manoviññāṇadhātu'}
WISDOM = {'investigation': 'vīmaṃsā', 'investigation of things': 'dhammavicayo', 'non-delusion': 'amoho',
          'things': 'dhamma', 'understanding': 'pajānanā', 'view': 'diṭṭhi', 'wisdom': 'paññā'}
PATHF = {'awakening': 'sambojjhaṅgo', 'awakening factor': 'sambojjhaṅgo', 'factor': 'sambojjhaṅgo',
         'factor of concentration': 'samādhisambojjhaṅgo', 'factor of energy': 'vīriyasambojjhaṅgo',
         'factor of investigation': 'dhammavicayasambojjhaṅgo', 'path': 'magga', 'path factor': 'maggaṅgaṃ'}
SUCC = {  # "Iddhīti. … iddhi samiddhi ijjhanā …; Iddhipādoti …; Iddhipādaṃ bhāvetīti …"
 'achievement': 'upasampadā', 'attainment': 'patti', 'basis of success': 'Iddhipādo', 'Basis of success': 'Iddhipādo',
 'cultivates': 'bahulīkaroti', 'develops': 'bhāveti', 'develops the basis': 'iddhipādaṃ bhāvetī',
 'Develops the basis': 'iddhipādaṃ bhāvetī', 'full attainment': 'sampatti', 'fully': 'samijjhanā',
 'obtaining': 'paṭilābho', 'practises': 'āsevati', 'prospering': 'samiddhi', 'realisation': 'sacchikiriyā',
 'succeeding': 'ijjhanā', 'success': 'iddhi', 'therefore': 'Tena', 'things': 'dhammānaṃ', 'touching': 'phusanā',
}
SUCC_AGG = dict(SUCC, **{
 'aggregate': 'khandho', 'aggregate of consciousness': ['viññāṇakkhandho', 'viññāṇakhandho'],
 'Aggregate of Consciousness': ['viññāṇakkhandho', 'viññāṇakhandho'], 'aggregate of feeling': 'vedanākkhandho',
 'aggregate of mental': 'saṅkhārakkhandho', 'Aggregate of Mental': 'saṅkhārakkhandho',
 'Aggregate of Perception': 'saññākkhandho', 'aggregate of perception': 'saññākkhandho', 'consciousness': 'viññāṇa',
 'feeling': 'vedanā', 'formations': 'saṅkhāra', 'mental': 'saṅkhāra', 'Mental Formations': 'saṅkhāra',
 'mental formations': 'saṅkhāra', 'perception': 'saññā'})
SUCC_ABH = dict(SUCC, **{'contact': 'phasso', 'exertion': 'paggāho', 'non-distraction': 'avikkhepo'})
ABH = {  # lokuttara frame
 'abandoning': 'pahānāya', 'abandoning of views': 'diṭṭhigatānaṃ pahānāya', 'absorption': 'jhānaṃ',
 'beyond': 'uttaraṃ', 'develops': 'bhāveti', 'develops the meditative': 'jhānaṃ bhāveti',
 'difficult': 'dukkhapaṭipadaṃ', 'difficult practice': 'dukkhapaṭipadaṃ', 'direct': 'ābhiññaṃ',
 'direct knowledge': 'ābhiññaṃ', 'dismantling': 'apacaya', 'dwells': 'viharati', 'enters': 'upasampajja',
 'enters and dwells': 'upasampajja viharati', 'knowledge': 'ābhiññaṃ', 'leading to dismantling': 'apacayagāmiṃ',
 'meditative': 'jhānaṃ', 'meditative absorption': 'jhānaṃ', 'Meditative absorption': 'jhānaṃ', 'monk': 'bhikkhu',
 'occasion': 'samaye', 'pleasures': 'kāmehi', 'practice': 'paṭipadaṃ', 'practice and slow': 'paṭipadaṃ dandhābhiññaṃ',
 'reaching': 'pattiyā', 'secluded': 'vivicceva', 'secluded from sense': 'vivicceva kāmehi', 'sense': 'kāmehi',
 'sense pleasures': 'kāmehi', 'slow': 'dandhābhiññaṃ', 'slow direct': 'dandhābhiññaṃ',
 'slow direct knowledge': 'dandhābhiññaṃ', 'stage': 'bhūmiyā', 'views': 'diṭṭhigatānaṃ',
}
ABH_DEV = dict(ABH, **{
 'basis of success': 'iddhipādaṃ', 'Basis of success': 'iddhipādaṃ', 'concentration': 'samādhi', 'desire': 'chanda',
 'develop': 'bhāveti', 'develop the basis': 'iddhipādaṃ bhāveti', 'develops the basis': 'iddhipādaṃ bhāveti',
 'Develops the basis': 'iddhipādaṃ bhāveti', 'endeavour': 'padhāna', 'endowed': 'samannāgataṃ',
 'endowed with concentration': 'samādhipadhānasaṅkhārasamannāgataṃ', 'formations': 'saṅkhāra',
 'formations of endeavour': 'padhānasaṅkhāra', 'investigation': 'vīmaṃsā', 'mind': 'citta',
 'monk develop': 'bhikkhu / bhāveti', 'success': 'iddhi', 'success endowed': 'samannāgataṃ iddhipādaṃ'})
def ABH_DEF(lead):  # 2-458 .. 2-461 "Tattha katamo chandiddhipādo? … Avasesā dhammā chandiddhipādasampayuttā"
    return dict(ABH, **{
     'associated': 'sampayuttā', 'basis of success': 'iddhipādo', 'Basis of success': 'iddhipādo',
     'remaining': 'Avasesā', 'remaining things': 'Avasesā dhammā', 'success': 'iddhi', 'therein': 'Tattha',
     'things': 'dhammā', 'Success Through Desire': lead, 'success through desire': lead,
     'Success Through Energy': lead, 'success through energy': lead, 'Success Through Mind': lead,
     'Success Through Investigation': lead})
QA = {'answers': NDE, 'questions': 'Pañhā', 'Questions and Answers': 'Pañhāpucchakaṃ', 'section': NDE,
      'Section of Questions': 'Pañhāpucchakaṃ'}

M = {}
M['2-9-0'] = {'analysis': 'vibhaṅgo', 'bases': 'pāda', 'bases of success': 'Iddhipāda',
              'Bases of Success': 'Iddhipāda', 'success': 'Iddhi'}
M['2-9-1-0'] = {'classification': 'bhājanīyaṃ', 'discourses': 'Suttanta'}
M['2-431'] = dict(FOURB)
M['2-9-1-1-0'] = HEAD('Chandiddhipādo')
M['2-432'] = CONC(('concentration through desire', 'chandasamādhi'), 'Chandaṃ', 'abhisaññahitvā')
M['2-433'] = dict(CHANDA, **SAMADHI_FULL, **ENDOWED_FULL)
M['2-433'].update(FORMATION)
M['2-433'].update({
 'burden': 'dhura', 'concentration through desire': 'chandasamādhi', 'desire': 'chando', 'effort': 'uyyāmo',
 'exertion': 'nikkamo', 'faculty of energy': 'vīriyindriyaṃ', 'firmness': 'thāmo', 'forward': 'parakkamo',
 'mind': 'cittassa', 'responsibility': 'dhuratā', 'striving': 'vāyāmo', 'taking': 'sampaggāho',
 'undiminished': 'anikkhitta', 'unrelaxed': 'asithila', 'vigour': 'ussoḷhī', 'zeal': 'ussāho'})
M['2-434'] = dict(SUCC_AGG)
M['2-9-1-2-0'] = HEAD('Vīriyiddhipādo')
M['2-435'] = CONC(('concentration through energy', 'vīriyasamādhi'), None, 'abhisaññūhitvā')
M['2-436'] = dict(FORMATION, **SAMADHI_FULL, **{'concentration through energy': 'vīriyasamādhi'})
M['2-437'] = dict(SUCC_AGG)
M['2-9-1-3-0'] = HEAD('Cittiddhipādo')
M['2-438'] = CONC(('concentration through mind', 'cittasamādhi'), None, 'abhisaññūhitvā')
M['2-439'] = dict(FORMATION, **SAMADHI, **{'concentration through mind': 'cittasamādhi'})
M['2-439'].update(MINDDEF)
M['2-440'] = dict(SUCC_AGG)
M['2-9-1-4-0'] = HEAD('Vīmaṃsiddhipādo')
M['2-441'] = CONC(('concentration through investigation', 'vīmaṃsāsamādhi'), None, 'abhisaññūhitvā')
M['2-441']['investigation'] = 'Vīmaṃsaṃ'
M['2-442'] = dict(FORMATION, **SAMADHI, **WISDOM, **{'concentration through investigation': 'vīmaṃsāsamādhi'})
M['2-443'] = dict(SUCC_AGG, **{'classification': 'bhājanīyaṃ', 'discourses': 'Suttanta', 'finished': NDE})
M['2-9-2-0'] = {'abhidhamma': 'Abhidhamma', 'classification': 'bhājanīyaṃ'}
M['2-444'] = dict(FOURB)
M['2-9-2-1-0'] = HEAD('Chandiddhipādo')
M['2-445'] = dict(ABH_DEV, **{'concentration through desire': 'chandasamādhi'})
M['2-446'] = dict(FORMATION, **SAMADHI, **PATHF, **CHANDA)
M['2-446']['concentration through desire'] = 'chandasamādhi'
M['2-447'] = dict(SUCC_ABH)
M['2-9-2-2-0'] = HEAD('Vīriyiddhipādo')
M['2-448'] = dict(ABH_DEV, **{'concentration through energy': 'vīriyasamādhi'})
M['2-449'] = dict(FORMATION, **SAMADHI, **PATHF, **{'concentration through energy': 'vīriyasamādhi'})
M['2-450'] = dict(SUCC_ABH)
M['2-9-2-3-0'] = HEAD('Cittiddhipādo')
M['2-451'] = dict(ABH_DEV, **{'concentration through mind': 'cittasamādhi'})
M['2-452'] = dict(FORMATION, **SAMADHI, **PATHF, **{'concentration through mind': 'cittasamādhi'})
M['2-452'].update(MINDDEF)
M['2-453'] = dict(SUCC_ABH)
M['2-9-2-4-0'] = HEAD('Vīmaṃsiddhipādo')
M['2-454'] = dict(ABH_DEV, **{'concentration through investigation': 'vīmaṃsāsamādhi'})
M['2-455'] = dict(FORMATION, **SAMADHI, **PATHF, **ENDOWED_FULL)
M['2-455'].update(WISDOM)
M['2-455']['concentration through investigation'] = 'vīmaṃsāsamādhi'
M['2-456'] = dict(SUCC_ABH)
M['2-457'] = {
 'bases': 'pādā', 'bases of success': 'iddhipādā', 'Bases of Success': 'iddhipādā', 'Basis of success': 'iddhipādo',
 'basis of success': 'iddhipādo', 'desire': 'chandiddhipādo', 'investigation': 'vīmaṃsiddhipādo',
 'mind': 'cittiddhipādo', 'success': 'iddhi', 'success through desire': 'chandiddhipādo',
 'Success Through Desire': 'chandiddhipādo', 'success through energy': 'vīriyiddhipādo',
 'Success Through Energy': 'vīriyiddhipādo', 'Success Through Investigation': 'vīmaṃsiddhipādo',
 'Success Through Mind': 'cittiddhipādo',
}
M['2-458'] = dict(ABH_DEF('chandiddhipādo'), **CHANDA)
M['2-458']['desire'] = 'chando'
M['2-459'] = dict(ABH_DEF('vīriyiddhipādo'), **PATHF, **{
 'effort': 'vāyāmo', 'initiation': 'ārambho', 'initiation of energy': 'vīriyārambho', 'mental': 'cetasiko',
 'mental initiation': 'cetasiko vīriyārambho', 'right': 'sammā'})
M['2-460'] = dict(ABH_DEF('cittiddhipādo'), **MINDDEF)
M['2-461'] = dict(ABH_DEF('vīmaṃsiddhipādo'), **PATHF, **{
 'abhidhamma': 'Abhidhamma', 'classification': 'bhājanīyaṃ', 'finished': NDE,
 'investigation': 'vīmaṃsiddhipādo', 'investigation of things': 'dhammavicayo', 'non-delusion': 'amoho',
 'right': 'sammā', 'understanding': 'pajānanā', 'view': 'diṭṭhi', 'wisdom': 'paññā'})
M['2-9-3-0'] = dict(QA)
M['2-462'] = dict(FOURB)
M['2-463'] = {'bases': 'pādānaṃ', 'bases of success': 'iddhipādānaṃ', 'Bases of Success': 'iddhipādānaṃ',
              'conflict': 'saraṇā', 'free': 'araṇā', 'involve': 'saraṇā', 'neutral': 'abyākatā', 'success': 'iddhi',
              'unwholesome': 'akusalā', 'wholesome': 'kusalā'}
M['2-9-3-1-0'] = {'triads': 'Tikaṃ'}
M['2-464'] = {
 'abandoned': 'pahātabbā', 'able': 'upādāniyā', 'accompanied': 'sahagatā',
 'accompanied by equanimity': 'upekkhāsahagatā', 'accompanied by happiness': 'sukhasahagatā',
 'accompanied by joy': 'pītisahagatā', 'arise': 'uppādino', 'arisen': 'uppannā', 'associated': 'sampayuttā',
 'belong': NDE, 'birth': NDE, 'cause': 'hetukā', 'causes': 'hetukā', 'clung': 'upādāniyā',
 'connected': 'saṃkilesikā', 'connected with defilement': 'saṃkilesikā', 'defilement': 'saṃkilesikā',
 'describable': 'vattabbā', 'dismantling': 'Apacaya', 'dominant': 'ādhipatino', 'dominant factor': 'ādhipatino',
 'due to arise': 'uppādino', 'equanimity': 'upekkhā', 'examination': 'vicāra', 'external': 'bahiddhā',
 'external objects': 'Bahiddhārammaṇā', 'factor': 'ādhipatino', 'feeling': 'vedanāya', 'fixed': 'niyatā',
 'future object': 'anāgatārammaṇā', 'happiness': 'sukha', 'having': NDE, 'internal': 'ajjhattā',
 'internal and external': 'ajjhattabahiddhā', 'invisible': 'Anidassana', 'invisible and offer': 'Anidassanaappaṭighā',
 'joy': 'pīti', 'leading to dismantling': 'Apacayagāmino', 'measureless': 'Appamāṇā',
 'measureless objects': 'Appamāṇārammaṇā', 'meditative': 'bhāvanāya', 'meditative development': 'bhāvanāya',
 'neither-painful-nor-pleasant': 'adukkhamasukhāya', 'object': 'ārammaṇā', 'objects': 'ārammaṇā',
 'past object': 'atītārammaṇā', 'path': 'magga', 'pleasant': 'sukhāya', 'pleasant feeling': 'sukhāya vedanāya',
 'present object': 'paccuppannārammaṇā', 'refined': 'Paṇītā', 'resistance': 'appaṭighā', 'rightness': 'Sammatta',
 'seeing': 'dassanena', 'subject to result': 'Vipākadhammadhammā', 'things': 'dhammā',
 'things subject': 'Vipākadhammadhammā', 'thought': 'vitakka', 'training': 'Sekkhā', 'undefiled': 'Asaṃkiliṭṭha',
 'wholesome': 'Kusalā',
}
M['2-9-3-2-0'] = {'pairs': 'Dukaṃ'}
M['2-465'] = dict(QA, **{
 'abandoned': 'pahātabbā', 'accompanied': 'sahagatā', 'accompanied by equanimity': 'upekkhāsahagatā',
 'accompanied by happiness': 'sukhasahagatā', 'accompanied by joy': 'pītisahagatā', 'along': 'ānuparivattino',
 'analysis': 'vibhaṅgo', 'arise': 'sahabhuno', 'arising': 'sahabhū', 'associated': 'sampayuttā', 'bases': 'pādā',
 'Bases of Success': 'iddhipādā', 'bases of success': 'iddhipādā', 'basis of success': 'iddhipādo',
 'Basis of success': 'iddhipādo', 'belong': NDE, 'beyond': 'uttarā', 'birth': NDE, 'cannot': 'na',
 'causes': 'hetukā', 'clinging': 'upādānā', 'conditioned': 'Saṅkhatā', 'conflict': 'Araṇā', 'conjoined': 'saṃsaṭṭhā',
 'defilements': 'kilesā', 'derived': 'upādā', 'describable': 'vattabbā', 'disjoined': 'visaṃsaṭṭho',
 'dissociated': 'vippayuttā', 'equanimity': 'upekkhā', 'examination': 'vicārā', 'external': 'bāhirā',
 'factor': 'acetasiko', 'factors': 'cetasikā', 'fetters': 'saṃyojanā', 'fine-material': 'rūpāvacarā',
 'fine-material sphere': 'rūpāvacarā', 'finished': 'niṭṭhito', 'fixed': 'Niyatā', 'floods': 'oghā',
 'follow': 'ānuparivattino', 'free': 'Araṇā', 'grasping': 'parāmāsā', 'happiness': 'sukha', 'having': 'Sahetukā',
 'hindrances': 'nīvaraṇā', 'immaterial': 'Arūpā', 'immaterial sphere': 'arūpāvacarā', 'internal': 'ajjhattiko',
 'investigation': 'Vīmaṃsiddhipādo', 'invisible': 'Anidassanā', 'joy': 'pīti', 'known': 'viññeyyā',
 'means': 'Kenaci', 'meditative': 'bhāvanāya', 'meditative development': 'bhāvanāya', 'mental': 'cetasikā',
 'mental factor': 'acetasiko', 'mental factors': 'cetasikā', 'mental taints': 'āsavā', 'mind': 'cittaṃ',
 'minds': 'cittā', 'non-root': 'na hetu', 'objects': 'ārammaṇā', 'originated': 'samuṭṭhānā',
 'resistance': 'Appaṭighā', 'root': 'hetu', 'roots': 'hetū', 'seeing': 'dassanena', 'sense': 'kāmāvacarā',
 'sense sphere': 'kāmāvacarā', 'sphere': 'āvacarā', 'subject to mental': 'sāsavā', 'success': 'iddhi',
 'success are conjoined': 'iddhipādā / saṃsaṭṭhā', 'Success Through Investigation': 'Vīmaṃsiddhipādo',
 'Success Through Mind': 'cittiddhipādo', 'taints': 'āsavā', 'thought': 'vitakkā', 'ties': 'ganthā',
 'together': 'saha', 'unsurpassed': 'Anuttarā', 'wrong': 'parāmāsā', 'wrong grasping': 'parāmāsā', 'yokes': 'yogā',
})

# ---- build ---------------------------------------------------------------
def segments(path):
    segs, buf = {}, []
    for line in path.read_text(encoding='utf-8').splitlines():
        buf.append(line)
        m = re.search(r'\^([\w-]+)\s*$', line)
        if m:
            segs[m.group(1)] = '\n'.join(buf); buf = []
    return segs

def resolve(val, text):
    """Pick the first alternative whose parts all occur; fix first-letter case to match the segment."""
    alts = val if isinstance(val, list) else [val]
    for a in alts:
        if a == NDE:
            return a
        parts = []
        for p in a.split(' / '):
            for c in (p, p[0].upper() + p[1:], p[0].lower() + p[1:]):
                if c in text:
                    parts.append(c); break
            else:
                break
        else:
            return ' / '.join(parts)
    return alts[0]

if __name__ == '__main__':
    segs = segments(root / 'AI_translation' / 'pali' / 'pi-2_split_chapters' / f'{ch}.md')
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
                pairs.append(f'{resolve(m[k], segs[sid])}={k}')
        out.append(f'[{sid}] ' + ', '.join(pairs))
    (d / f'{ch}.mapped.md').write_text('\n'.join(out) + '\n', encoding='utf-8')
    print('written', len(out), 'missing', missing)
