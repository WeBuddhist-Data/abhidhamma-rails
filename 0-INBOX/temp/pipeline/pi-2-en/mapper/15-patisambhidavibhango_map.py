import pathlib
d = pathlib.Path(__file__).parent
ch = '15-patisambhidavibhango'
NDE = '(no direct equivalent)'

# the four analytical knowledges and the closing "language / ready understanding" formula
PS = {
 'analytical': 'paṭisambhidā', 'analytical knowledge': 'paṭisambhidā', 'Analytical Knowledges': 'paṭisambhidā',
 'analytical knowledges': 'paṭisambhidā', 'expression': 'ābhilāpe', 'knowledge': 'ñāṇaṃ',
 'knowledge of language': 'niruttipaṭisambhidā', 'knowledge of meaning': 'atthapaṭisambhidā',
 'knowledge of principles': 'dhammapaṭisambhidā', 'knowledge of ready': 'paṭibhānapaṭisambhidā',
 'Knowledge with regard': 'ñāṇaṃ', 'knowledges': 'ñāṇesu', 'language': 'nirutti', 'meaning': 'attha',
 'principles': 'dhamma', 'ready': 'paṭibhāna', 'ready understanding': 'paṭibhāna', 'regard': NDE,
 'regard to knowledges': 'ñāṇesu', 'understanding': 'paṭibhāna',
}
# Abhidhamma classification: added closing formula + "contact ... non-distraction"
ABH = dict(PS, **{
 'contact': 'phasso', 'illuminate': 'jotakānī', 'illuminate this meaning': 'idamatthajotakānī',
 'knowledges illuminate': 'ñāṇāni idamatthajotakānī', 'known': 'paññatti', 'knows': 'jānāti',
 'language': 'niruttiyā', 'non-distraction': 'avikkhepo', 'occasion': 'samaye', 'things': 'dhammā',
 'things are made': 'dhammānaṃ paññatti',
})
# sense-sphere mind with knowledge / view (2-725, 726, 730, 731)
MIND8 = {
 'accompanied': 'sahagataṃ', 'accompanied by equanimity': 'upekkhāsahagataṃ',
 'accompanied by joy': 'somanassasahagataṃ', 'arisen': 'uppannaṃ', 'associated': 'sampayuttaṃ',
 'dissociated': 'vippayuttaṃ', 'equanimity': 'upekkhā', 'joy': 'somanassa', 'mental': 'dhammārammaṇaṃ',
 'mental object': 'dhammārammaṇaṃ', 'mind': 'cittaṃ', 'object': 'ārammaṇaṃ', 'prompting': 'sasaṅkhārena',
 'sight': 'rūpārammaṇaṃ', 'whatever': 'yaṃ yaṃ',
}
# fine-material path, earth device (2-727, 738)
JH_RUPA = {
 'absorption': 'jhānaṃ', 'develops': 'bhāveti', 'develops the path': 'maggaṃ bhāveti', 'device': 'kasiṇaṃ',
 'dwells': 'viharati', 'earth': 'pathavī', 'earth device': 'pathavīkasiṇaṃ', 'enters': 'upasampajja',
 'enters and dwells': 'upasampajja viharati', 'fine-material': 'rūpūpapattiyā', 'fine-material sphere': 'rūpūpapattiyā',
 'meditative': 'jhānaṃ', 'meditative absorption': 'jhānaṃ', 'Meditative absorption': 'jhānaṃ', 'path': 'maggaṃ',
 'path for rebirth': 'rūpūpapattiyā maggaṃ', 'pleasures': 'kāmehi', 'rebirth': 'ūpapattiyā', 'secluded': 'vivicceva',
 'secluded from sense': 'vivicceva kāmehi', 'sense': 'kāmehi', 'sense pleasures': 'kāmehi', 'sphere': NDE,
 'things are wholesome': 'dhammā kusalā', 'wholesome': 'kusalā',
}
# immaterial path, neither-perception-nor-non-perception (2-728, 739, 745)
NEVASANNA = {
 'abandoning': 'pahānā', 'abandoning of happiness': 'sukhassa ca pahānā', 'absorption': 'jhānaṃ',
 'accompanied': 'sahagataṃ', 'beyond': 'samatikkamma', 'completely': 'sabbaso',
 'Completely passing': 'sabbaso / samatikkamma', 'completely passing': 'sabbaso / samatikkamma',
 'dwells': 'viharati', 'enters': 'upasampajja', 'enters and dwells': 'upasampajja viharati', 'field': 'āyatanaṃ',
 'field of nothingness': 'ākiñcaññāyatanaṃ', 'fourth meditative': 'catutthaṃ jhānaṃ',
 'fourth meditative absorption': 'catutthaṃ jhānaṃ', 'happiness': 'sukhassa', 'meditative': 'jhānaṃ',
 'meditative absorption': 'jhānaṃ', 'Meditative absorption': 'jhānaṃ',
 'neither-perception-nor-non-perception': 'nevasaññānāsaññāyatanasaññāsahagataṃ', 'nothingness': 'ākiñcaññāyatanaṃ',
 'passing': 'samatikkamma', 'perception': 'saññā',
}
JH_ARUPA = dict(NEVASANNA, **{
 'develops': 'bhāveti', 'develops the path': 'maggaṃ bhāveti', 'immaterial': 'arūpūpapattiyā',
 'immaterial sphere': 'arūpūpapattiyā', 'path': 'maggaṃ', 'path for rebirth': 'arūpūpapattiyā maggaṃ',
 'rebirth': 'ūpapattiyā', 'sphere': NDE, 'things are wholesome': 'dhammā kusalā', 'wholesome': 'kusalā',
})
# supramundane first path (2-729, 740)
JH_LOK = {
 'abandoning': 'pahānāya', 'abandoning of views': 'diṭṭhigatānaṃ pahānāya', 'absorption': 'jhānaṃ',
 'beyond': 'uttaraṃ', 'develops': 'bhāveti', 'develops the meditative': 'jhānaṃ bhāveti', 'difficult': 'dukkha',
 'difficult practice': 'dukkhapaṭipadaṃ', 'direct': 'ābhiññaṃ', 'direct knowledge': 'ābhiññaṃ',
 'dismantling': 'apacaya', 'dwells': 'viharati', 'enters': 'upasampajja', 'enters and dwells': 'upasampajja viharati',
 'leading to dismantling': 'apacayagāmiṃ', 'meditative': 'jhānaṃ', 'meditative absorption': 'jhānaṃ',
 'Meditative absorption': 'jhānaṃ', 'pleasures': 'kāmehi', 'practice': 'paṭipadaṃ',
 'practice and slow': 'dukkhapaṭipadaṃ dandhābhiññaṃ', 'reaching': 'pattiyā', 'secluded': 'vivicceva',
 'secluded from sense': 'vivicceva kāmehi', 'sense': 'kāmehi', 'sense pleasures': 'kāmehi', 'slow': 'dandhābhiññaṃ',
 'slow direct': 'dandhābhiññaṃ', 'slow direct knowledge': 'dandhābhiññaṃ', 'stage': 'bhūmiyā',
 'things are wholesome': 'dhammā kusalā', 'views': 'diṭṭhigatānaṃ', 'wholesome': 'kusalā',
}
# results / functional: "there is contact, feeling ... life faculty; whatever other ..."
CETASIKA = {
 'arisen things': 'samuppannā / dhammā', 'dependently': 'paṭicca', 'dependently arisen things': 'paṭiccasamuppannā / dhammā',
 'equanimity faculty': 'upekkhindriyaṃ', 'faculty': 'indriyaṃ', 'feeling': 'vedanā', 'immaterial': 'arūpino',
 'intention': 'cetanā', 'life': 'jīvitindriyaṃ', 'life faculty': 'jīvitindriyaṃ', 'mind': 'cittaṃ',
 'mind faculty': 'manindriyaṃ', 'one-pointedness': 'ekaggatā', 'one-pointedness of mind': 'cittassekaggatā',
 'perception': 'saññā', 'whatever': 'ye vā pana',
}
NEUTRAL = {'neutral': 'abyākatā', 'things are neutral': 'dhammā abyākatā'}
KAMA_VIP = {'accumulated': 'upacitattā', 'done': 'katattā', 'sense-sphere': 'kāmāvacarassa',
            'sense-sphere wholesome': 'kāmāvacarassa kusalassa', 'wholesome': 'kusalassa',
            'wholesome action': 'kusalassa kammassa'}
AKUS_VIP = {'accumulated': 'upacitattā', 'done': 'katattā', 'unwholesome': 'akusalassa'}
# five sense-consciousnesses
PANCA = {
 'accompanied': 'sahagataṃ', 'accompanied by equanimity': 'upekkhāsahagataṃ', 'arisen': 'uppannaṃ',
 'body-consciousness': 'kāyaviññāṇaṃ', 'ear-consciousness': 'sotaviññāṇaṃ', 'equanimity': 'upekkhā',
 'eye-consciousness': 'cakkhuviññāṇaṃ', 'nose-consciousness': 'ghānaviññāṇaṃ', 'object': 'ārammaṇaṃ',
 'resultant': 'vipākaṃ', 'sight': 'rūpārammaṇaṃ', 'smell': 'gandhārammaṇaṃ', 'sound': 'saddārammaṇaṃ',
 'tangible': 'phoṭṭhabbārammaṇaṃ', 'tangible thing': 'phoṭṭhabbārammaṇaṃ', 'taste': 'rasārammaṇaṃ',
 'thing': 'phoṭṭhabbārammaṇaṃ', 'tongue-consciousness': 'jivhāviññāṇaṃ',
}
# mind element / mind-consciousness element
MANO = {
 'accompanied': 'sahagatā', 'accompanied by equanimity': 'upekkhāsahagatā', 'accompanied by joy': 'somanassasahagatā',
 'arisen': 'uppannā', 'consciousness element': 'viññāṇadhātu', 'element': 'dhātu', 'element has arisen': 'dhātu uppannā',
 'equanimity': 'upekkhā', 'examination': 'vicāro', 'mental': 'dhammārammaṇā', 'mental object': 'dhammārammaṇā',
 'mind element': 'manodhātu', 'mind-consciousness': 'manoviññāṇa', 'mind-consciousness element': 'manoviññāṇadhātu',
 'object': 'ārammaṇā', 'resultant': 'vipākā', 'sight': 'rūpārammaṇā', 'tangible': 'phoṭṭhabbārammaṇā',
 'tangible thing': 'phoṭṭhabbārammaṇā', 'thing': 'phoṭṭhabbārammaṇā', 'thought': 'vitakko',
}
MANO8 = dict(MANO, **{'associated': 'sampayuttā', 'dissociated': 'vippayuttā',
                      'dissociated from knowledge': 'ñāṇavippayuttā', 'joy': 'somanassa', 'prompting': 'sasaṅkhārena'})
KIRIYA = {'functional': 'kiriyā', 'unwholesome': 'ākusalā', 'wholesome': 'kusalā',
          'wholesome nor unwholesome': 'neva kusalā nākusalā'}

def J(*ds):
    out = {}
    for x in ds:
        out.update(x)
    return out

M = {}
M['2-15-0'] = {'analysis': 'vibhaṅgo', 'analytical': 'Paṭisambhidā', 'Analytical Knowledges': 'Paṭisambhidā',
               'analytical knowledges': 'Paṭisambhidā', 'knowledges': 'Paṭisambhidā'}
M['2-15-1-0'] = {'classification': 'bhājanīyaṃ', 'discourses': 'Suttanta'}
M['2-15-1-1-0'] = {'section': 'vāro', 'summary': 'Saṅgaha', 'Summary Section': 'Saṅgahavāro'}
M['2-718'] = J(PS, {'meaning': 'Atthe', 'principles': 'dhamme', 'section': 'vāro', 'summary': 'saṅgaha',
                    'Summary Section': 'saṅgahavāro'})
M['2-15-1-2-0'] = {'section': 'vāro', 'truths': 'Sacca', 'Truths Section': 'Saccavāro'}
M['2-719'] = J(PS, {'cessation': 'nirodhe', 'cessation of suffering': 'dukkhanirodhe', 'origin': 'samudaye',
                    'origin of suffering': 'dukkhasamudaye', 'section': 'vāro', 'suffering': 'Dukkhe',
                    'truths': 'sacca', 'Truths Section': 'saccavāro'})
M['2-15-1-3-0'] = {'cause': 'Hetu', 'section': 'vāro'}
M['2-720'] = J(PS, {'cause': 'Hetumhi', 'fruit': 'phale', 'section': 'vāro'})
M['2-15-1-4-0'] = {'section': 'vāro', 'things': 'Dhamma', 'Things Section': 'Dhammavāro'}
M['2-721'] = J(PS, {'born': 'jātā', 'brought': 'sañjātā', 'forth': 'sañjātā', 'manifest': 'pātubhūtā',
                    'produced': 'nibbattā', 'section': 'vāro', 'things': 'dhammā', 'Things Section': 'dhammavāro',
                    'whatever': 'Ye'})
M['2-15-1-5-0'] = {'dependent': 'Paṭicca', 'origination': 'samuppāda', 'Origination Section': 'samuppādavāro',
                   'section': 'vāro'}
M['2-722'] = J(PS, {'aging': 'Jarā', 'aging and death': 'Jarāmaraṇe', 'cessation': 'nirodhe',
                    'cessation of aging': 'jarāmaraṇanirodhe', 'death': 'maraṇe', 'knowledge of aging': 'Jarāmaraṇe ñāṇaṃ',
                    'origin': 'samudaye'})
M['2-723'] = J(PS, {'birth': 'Jātiyā', 'cessation': 'nirodhe', 'cessation of formations': 'saṅkhāranirodhe',
                    'clinging': 'upādāne', 'consciousness': 'viññāṇe', 'contact': 'phasse', 'craving': 'taṇhāya',
                    'dependent': 'paṭicca', 'existence': 'bhave', 'feeling': 'vedanāya', 'form': 'rūpe',
                    'formations': 'saṅkhāresu', 'knowledge of consciousness': 'viññāṇe ñāṇaṃ',
                    'knowledge of formations': 'saṅkhāresu ñāṇaṃ', 'material': 'rūpe', 'material form': 'rūpe',
                    'mentality': 'nāma', 'mentality and material': 'nāmarūpe', 'origin': 'samudaye',
                    'origination': 'samuppāda', 'Origination Section': 'samuppādavāro', 'section': 'vāro',
                    'sense-fields': 'āyatane'})
M['2-15-1-6-0'] = {'scripture': 'Pariyatti', 'Scripture Section': 'Pariyattivāro', 'section': 'vāro'}
M['2-724'] = J(PS, {
 'accounts': 'abbhutadhammaṃ', 'birth': 'jātakaṃ', 'classification': 'bhājanīyaṃ', 'discourses': 'suttaṃ',
 'expositions': 'veyyākaraṇaṃ', 'finished': NDE, 'inspired': 'udānaṃ', 'knows': 'jānāti', 'marvellous': 'abbhuta',
 'meaning': 'atthaṃ', 'mixed': 'geyyaṃ', 'monk': 'bhikkhu', 'prose-and-verse': 'geyyaṃ',
 'question-and-answer': 'vedallaṃ', 'scripture': 'pariyatti', 'Scripture Section': 'pariyattivāro', 'section': 'vāro',
 'spoken': 'bhāsitassa', 'stories': 'jātakaṃ', 'teaching': 'dhammaṃ', 'texts': 'itivuttakaṃ', 'therein': 'Tattha',
 'thing': NDE, 'utterances': 'udānaṃ', 'verses': 'gāthaṃ', 'knowledges': 'Ñāṇesu',
 'regard to knowledges': 'Ñāṇesu'})
M['2-15-2-0'] = {'abhidhamma': 'Abhidhamma', 'classification': 'bhājanīyaṃ'}
M['2-15-2-1-0'] = {'section': 'vāro', 'wholesome': 'Kusala'}
KUS_MIND = {'sense': 'kāmāvacaraṃ', 'sense sphere': 'kāmāvacaraṃ', 'sphere': 'āvacaraṃ',
            'sphere has arisen': 'kāmāvacaraṃ / uppannaṃ', 'things are wholesome': 'dhammā kusalā',
            'wholesome': 'kusalaṃ', 'wholesome mind': 'kusalaṃ cittaṃ'}
M['2-725'] = J(ABH, MIND8, KUS_MIND)
M['2-726'] = J(ABH, MIND8, KUS_MIND, {'dissociated from knowledge': 'ñāṇavippayuttaṃ'})
M['2-727'] = J(ABH, JH_RUPA)
M['2-728'] = J(ABH, JH_ARUPA)
M['2-729'] = J(ABH, JH_LOK)
M['2-15-2-2-0'] = {'section': 'vāro', 'unwholesome': 'Akusala'}
AKUS_MIND = {'things are unwholesome': 'dhammā akusalā', 'unwholesome': 'akusalaṃ', 'unwholesome mind': 'akusalaṃ cittaṃ',
             'view': 'diṭṭhigata'}
M['2-730'] = J(ABH, MIND8, AKUS_MIND)
M['2-731'] = J(ABH, MIND8, AKUS_MIND, {'aversion': 'paṭigha', 'doubt': 'vicikicchā', 'grief': 'domanassa',
                                      'restlessness': 'uddhacca'})
M['2-15-2-3-0'] = {'section': 'vāro'}
M['2-732'] = J(ABH, NEUTRAL, CETASIKA, KAMA_VIP, PANCA)
M['2-733'] = J(ABH, NEUTRAL, CETASIKA, KAMA_VIP, PANCA, {'accompanied by happiness': 'sukhasahagataṃ',
                                                      'happiness': 'sukhaṃ'})
M['2-734'] = J(ABH, NEUTRAL, CETASIKA, KAMA_VIP, MANO)
M['2-735'] = J(ABH, NEUTRAL, CETASIKA, KAMA_VIP, MANO, {'happiness': 'sukhaṃ', 'joy': 'pīti',
                                                     'joy faculty': 'somanassindriyaṃ'})
M['2-736'] = J(ABH, NEUTRAL, CETASIKA, KAMA_VIP, MANO)
M['2-737'] = J(ABH, NEUTRAL, KAMA_VIP, MANO8, {'whatever': 'yaṃ yaṃ'})
M['2-738'] = J(ABH, NEUTRAL, JH_RUPA, KAMA_VIP, {'fine-material-sphere': 'rūpāvacarassa', 'sphere': 'āvacarassa'})
M['2-739'] = J(ABH, NEUTRAL, JH_ARUPA, KAMA_VIP, {'immaterial-sphere': 'arūpāvacarassa', 'sphere': 'āvacarassa'})
M['2-740'] = J(ABH, NEUTRAL, JH_LOK, KAMA_VIP, {'developed': 'bhāvitattā', 'emptiness': 'suññataṃ',
                                             'wholesome': 'kusalassa'})
M['2-741'] = J(ABH, NEUTRAL, CETASIKA, AKUS_VIP, PANCA, {'pain': 'dukkhaṃ'})
M['2-742'] = J(ABH, NEUTRAL, CETASIKA, AKUS_VIP, MANO)
M['2-15-2-4-0'] = {'functional': 'Kiriya', 'section': 'vāro'}
M['2-743'] = J(ABH, NEUTRAL, CETASIKA, MANO, KIRIYA)
M['2-744'] = J(ABH, NEUTRAL, CETASIKA, MANO, KIRIYA, {'concentration': 'samādhindriyaṃ', 'joy': 'somanassa'})
M['2-745'] = J(ABH, NEUTRAL, MANO8, NEVASANNA, KIRIYA, {
 'develops': 'bhāveti', 'dwelling': 'vihāraṃ', 'fine-material-sphere': 'rūpāvacaraṃ', 'immaterial-sphere': 'arūpāvacaraṃ',
 'immaterial-sphere meditative absorption': 'arūpāvacaraṃ jhānaṃ', 'life': 'diṭṭhadhamma', 'pleasant': 'sukha'})
M['2-746'] = J(PS, {
 'abhidhamma': 'Abhidhamma', 'analytical knowledges arise': 'paṭisambhidā / uppajjanti', 'arise': 'uppajjanti',
 'arises': 'uppajjati', 'arisings': 'uppādesu', 'associated': 'sampayuttesu', 'classification': 'bhājanīyaṃ',
 'finished': NDE, 'fruits': 'phalesu', 'functional': 'kiriyato', 'knowledge': 'ñāṇa', 'knowledges': 'paṭisambhidā',
 'knowledges arise': 'paṭisambhidā / uppajjanti', 'mind': 'cittuppādesu', 'paths': 'maggesu',
 'sense-sphere': 'kāmāvacara', 'side': NDE, 'wholesome': 'kusalato'})
M['2-15-3-0'] = {'answers': NDE, 'questions': 'Pañhā', 'Questions and Answers': 'Pañhāpucchakaṃ', 'section': NDE,
                 'Section of Questions': 'Pañhāpucchakaṃ'}
M['2-747'] = J(PS, {'knowledge': 'paṭisambhidā', 'knowledges': 'paṭisambhidā'})
M['2-748'] = {'analytical': 'paṭisambhidānaṃ', 'Analytical Knowledges': 'paṭisambhidānaṃ',
              'analytical knowledges': 'paṭisambhidānaṃ', 'conflict': 'saraṇā', 'free': 'araṇā', 'involve': 'saraṇā',
              'knowledges': 'paṭisambhidānaṃ', 'neutral': 'abyākatā', 'unwholesome': 'akusalā', 'wholesome': 'kusalā'}
M['2-15-3-1-0'] = {'triads': 'Tikaṃ'}
QPS = {'analytical': 'paṭisambhidā', 'analytical knowledge': 'paṭisambhidā', 'analytical knowledges': 'paṭisambhidā',
       'Analytical Knowledges': 'paṭisambhidā', 'analytical knowledges belong': 'paṭisambhidā',
       'knowledge': 'paṭisambhidā', 'knowledge of meaning': 'atthapaṭisambhidā', 'knowledges': 'paṭisambhidā',
       'knowledges are unfixed': 'paṭisambhidā aniyatā', 'knowledges belong': 'paṭisambhidā', 'meaning': 'attha'}
M['2-749'] = J(QPS, {
 'abandoned': 'pahātabbā', 'able': 'upādāniyā', 'accompanied': 'sahagatā', 'accompanied by equanimity': 'upekkhāsahagatā',
 'accompanied by happiness': 'sukhasahagatā', 'accompanied by joy': 'pītisahagatā', 'accumulation': 'ācaya',
 'arise': 'uppādino', 'arisen': 'uppannā', 'associated': 'sampayuttā', 'belong': NDE, 'beyond': 'asekkhā',
 'birth': NDE, 'cause': 'hetukā', 'causes': 'hetukā', 'clung': 'upādāniyā', 'connected': 'saṃkilesikā',
 'connected with defilement': 'saṃkilesikā', 'defilement': 'saṃkilesikā', 'describable': 'vattabbā',
 'dismantling': 'apacaya', 'dominant': 'ādhipatino', 'dominant factor': 'ādhipatino', 'due to arise': 'uppādino',
 'equanimity': 'upekkhā', 'examination': 'vicārā', 'expanded': 'mahaggatārammaṇā', 'external': 'bahiddhā',
 'external object': 'bahiddhārammaṇā', 'external objects': 'bahiddhārammaṇā', 'factor': 'ādhipatino',
 'feeling': 'vedanāya', 'fixed': 'niyatā', 'future object': 'anāgatārammaṇā', 'happiness': 'sukha', 'having': NDE,
 'internal': 'ajjhattā', 'internal and external': 'ajjhattabahiddhā', 'invisible': 'Anidassana',
 'invisible and offer': 'Anidassanaapaṭighā', 'joy': 'pīti', 'knowledge of language': 'Niruttipaṭisambhidā',
 'language': 'Nirutti', 'leading to accumulation': 'ācayagāmino', 'leading to dismantling': 'apacayagāminī',
 'limited': 'parittā', 'limited object': 'parittārammaṇā', 'measureless': 'appamāṇā',
 'measureless objects': 'appamāṇārammaṇā', 'meditative': 'bhāvanāya', 'meditative development': 'bhāvanāya',
 'middling': 'majjhimā', 'neither-painful-nor-pleasant': 'adukkhamasukhāya', 'neutral': 'abyākatā',
 'object': 'ārammaṇā', 'objects': 'ārammaṇā', 'past object': 'atītārammaṇā', 'path': 'magga', 'pleasant': 'sukhāya',
 'pleasant feeling': 'sukhāya vedanāya', 'present object': 'paccuppannārammaṇā', 'refined': 'paṇītā',
 'resistance': 'apaṭighā', 'results nor things': 'nevavipākanavipākadhammadhammā', 'rightness': 'sammatta',
 'seeing': 'dassanena', 'subject to result': 'vipākadhammadhammā', 'thing': 'dhammā',
 'thing subject': 'vipākadhammadhammā', 'things': 'dhammā', 'things subject': 'vipākadhammadhammā',
 'thought': 'vitakka', 'training': 'sekkhā', 'undefiled': 'asaṃkiliṭṭha', 'unfixed': 'aniyatā', 'wholesome': 'kusalā'})
M['2-15-3-2-0'] = {'pairs': 'Dukaṃ'}
M['2-750'] = J(QPS, {
 'abandoned': 'pahātabbā', 'accompanied': 'sahagatā', 'accompanied by equanimity': 'upekkhāsahagatā',
 'accompanied by happiness': 'sukhasahagatā', 'accompanied by joy': 'pītisahagatā', 'along': 'ānuparivattino',
 'analysis': 'vibhaṅgo', 'answers': NDE, 'arise': 'sahabhuno', 'associated': 'sampayuttā', 'belong': NDE,
 'beyond': 'uttarā', 'birth': NDE, 'cannot': 'na', 'causes': 'hetukā', 'clinging': 'upādānā',
 'conditioned': 'saṅkhatā', 'conflict': 'Araṇā', 'conjoined': 'saṃsaṭṭhā', 'defilements': 'kilesā',
 'derived': 'upādā', 'describable': 'vattabbā', 'dissociated': 'vippayuttā', 'equanimity': 'upekkhā',
 'examination': 'vicārā', 'external': 'bāhirā', 'factors': 'cetasikā', 'fetters': 'saṃyojanā',
 'fine-material': 'rūpāvacarā', 'fine-material sphere': 'rūpāvacarā', 'finished': 'niṭṭhito', 'fixed': 'niyatā',
 'floods': 'oghā', 'follow': 'ānuparivattino', 'free': 'Araṇā', 'grasping': 'parāmāsā', 'happiness': 'sukha',
 'hindrances': 'nīvaraṇā', 'immaterial': 'arūpā', 'immaterial sphere': 'arūpāvacarā', 'invisible': 'anidassanā',
 'joy': 'pīti', 'known': 'viññeyyā', 'means': 'kenaci', 'meditative': 'bhāvanāya',
 'meditative development': 'bhāvanāya', 'mental': 'cetasikā', 'mental factors': 'cetasikā', 'mental taint': 'āsavo',
 'mental taints': 'āsavā', 'mind': 'citta', 'minds': 'cittā', 'non-roots': 'na hetū', 'objects': 'ārammaṇā',
 'originated': 'samuṭṭhānā', 'questions': 'Pañhā', 'Questions and Answers': 'Pañhāpucchakaṃ',
 'resistance': 'appaṭighā', 'roots': 'Hetū', 'section': NDE, 'Section of Questions': 'Pañhāpucchakaṃ',
 'seeing': 'dassanena', 'sense': 'kāmāvacarā', 'sense sphere': 'kāmāvacarā', 'sphere': 'āvacarā',
 'subject to mental': 'sāsavā', 'surpassable': 'sauttarā', 'taint': 'āsavo', 'taints': 'āsavā', 'thought': 'vitakkā',
 'ties': 'ganthā', 'together': 'saha', 'unfixed': 'aniyatā', 'unsurpassed': 'anuttarā', 'worldly': 'lokiyā',
 'wrong': 'parāmāsā', 'wrong grasping': 'parāmāsā', 'yokes': 'yogā'})

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
