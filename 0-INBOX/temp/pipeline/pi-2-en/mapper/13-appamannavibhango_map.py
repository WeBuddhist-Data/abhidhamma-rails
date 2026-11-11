import pathlib
d = pathlib.Path(__file__).parent
ch = '13-appamannavibhango'
NDE = '(no direct equivalent)'

# the four measureless states: word stems per state
ST = {
 'metta': dict(name='mettā', inst='mettāya', acc='mettāsahagatena', acc2='mettāsahagataṃ', yana='mettāyanā',
               itatta='mettāyitattaṃ', ceto='mettācetovimutti'),
 'karuna': dict(name='karuṇā', inst='karuṇāya', acc='karuṇāsahagatena', acc2='karuṇāsahagataṃ', yana='karuṇāyanā',
                itatta='karuṇāyitattaṃ', ceto='karuṇācetovimutti'),
 'mudita': dict(name='muditā', inst='muditāya', acc='muditāsahagatena', acc2='muditāsahagataṃ', yana='muditāyanā',
                itatta='muditāyitattaṃ', ceto='muditācetovimutti'),
 'upekkha': dict(name='upekkhā', inst='upekkhāya', acc='upekkhāsahagatena', acc2='upekkhāsahagataṃ',
                 yana='upekkhāyanā', itatta='upekkhāyitattaṃ', ceto='upekkhācetovimutti'),
}

def state_terms(s, acc_form):
    """English labels for a given state, shared by every segment that names it."""
    t = ST[s]
    m = {'liberation': 'vimutti', 'liberation of mind': 'cetovimutti'}
    if s == 'metta':
        m.update({'loving-kindness': t['name'], 'friendliness': 'metti', 'friendly': t['yana'],
                  'state of friendliness': t['itatta'], 'mind through loving-kindness': t['ceto'],
                  'accompanied by loving-kindness': t[acc_form]})
    elif s == 'karuna':
        m.update({'compassion': t['name'], 'compassionate': t['yana'], 'state of compassion': t['itatta'],
                  'mind through compassion': t['ceto'], 'accompanied by compassion': t[acc_form]})
    elif s == 'mudita':
        m.update({'sympathetic': t['name'], 'sympathetic joy': t['name'], 'joy': t['name'], 'gladness': t['name'],
                  'glad': t['yana'], 'state of gladness': t['itatta'], 'mind through sympathetic': t['ceto'],
                  'accompanied by sympathetic': t[acc_form]})
    else:
        m.update({'equanimity': t['name'], 'equanimous': t['yana'], 'state of equanimity': t['itatta'],
                  'mind through equanimity': t['ceto'], 'accompanied by equanimity': t[acc_form]})
    return m

# 2-642 / 2-699: the four-fold pervading formula
PERVADE4 = {
 'abundant': 'vipulena', 'accompanied': 'sahagatena', 'accompanied by compassion': 'karuṇāsahagatena',
 'accompanied by equanimity': 'upekkhāsahagatena', 'accompanied by loving-kindness': 'mettāsahagatena',
 'accompanied by sympathetic': 'muditāsahagatena', 'across': 'tiriyaṃ', 'compassion': 'karuṇā', 'direction': 'disaṃ',
 'dwells': 'viharati', 'dwells pervading': 'pharitvā viharati', 'entire': 'sabbāvantaṃ',
 'entire world': 'sabbāvantaṃ lokaṃ', 'equanimity': 'upekkhā', 'everywhere': 'sabbadhi', 'expanded': 'mahaggatena',
 'himself': 'sabbattatāya', 'hostility': 'averena', 'ill': 'abyāpajjena', 'joy': 'muditā', 'likewise': 'tathā',
 'likewise the fourth': 'tathā catutthaṃ', 'loving-kindness': 'mettā', 'measureless': 'appamāṇena',
 'measureless states': 'appamaññāyo', 'mind': 'cetasā', 'mind accompanied': 'mettāsahagatena cetasā',
 'monk': 'bhikkhu', 'monk dwells': 'bhikkhu / viharati', 'monk dwells pervading': 'bhikkhu / pharitvā viharati',
 'pervading': 'pharitvā', 'pervading one direction': 'ekaṃ disaṃ pharitvā',
 'pervading the entire': 'sabbāvantaṃ / pharitvā', 'regarding': 'sabbattatāya', 'sympathetic': 'muditā',
 'sympathetic joy': 'muditā',
}

# 2-643/653/663/673: "how does a monk dwell ...", definition of the state and of mind
def how(s, extra):
    t = ST[s]
    m = {
     'accompanied': 'sahagataṃ', 'activity': 'mānasaṃ', 'aggregate': 'khandho',
     'aggregate of consciousness': 'viññāṇakkhandho', 'Aggregate of Consciousness': 'viññāṇakkhandho',
     'arisen': 'jātaṃ', 'associated': 'sampayuttaṃ', 'beings': 'sattesu', 'bright': 'paṇḍaraṃ', 'conjoined': 'saṃsaṭṭhaṃ',
     'consciousness': 'viññāṇaṃ', 'consciousness element': 'viññāṇadhātu', 'corresponding': 'tajjā', 'direction': 'disaṃ',
     'dwell': 'viharati', 'dwell pervading': 'pharitvā viharati', 'element': 'dhātu', 'faculty': 'indriyaṃ',
     'heart': 'hadayaṃ', 'mental': 'mānasaṃ', 'mental activity': 'mānasaṃ', 'mentality': 'mano', 'mind': 'cittaṃ',
     'mind accompanied': t['acc'] + ' cetasā', 'mind faculty': 'manindriyaṃ', 'mind is accompanied': 'cittaṃ / sahagataṃ',
     'mind sense-field': 'manāyatanaṃ', 'mind-consciousness': 'manoviññāṇa',
     'mind-consciousness element': 'manoviññāṇadhātu', 'monk': 'bhikkhu', 'monk dwell': 'bhikkhu / viharati',
     'monk dwell pervading': 'bhikkhu / pharitvā viharati', 'person': 'puggalaṃ', 'pervades': 'pharati',
     'pervading': 'pharitvā', 'pervading one direction': 'ekaṃ disaṃ pharitvā', 'seeing': 'disvā',
     'sense-field': 'āyatanaṃ', 'therefore': 'Tena', 'therein': 'Tattha', 'together': 'saha', 'towards': NDE,
    }
    m.update(state_terms(s, 'acc'))
    m.update(extra)
    return m

# 2-649/659/669/679: comment on "with a mind accompanied by ..."
def comment(s, extra=None):
    t = ST[s]
    m = {
     'accompanied': 'sahagataṃ', 'activity': 'mānasaṃ', 'arisen': 'jātaṃ', 'associated': 'sampayuttaṃ',
     'beings': 'sattesu', 'conjoined': 'saṃsaṭṭhaṃ', 'consciousness element': 'viññāṇadhātu', 'corresponding': 'tajjā',
     'element': 'dhātu', 'mental': 'mānasaṃ', 'mental activity': 'mānasaṃ', 'mentality': 'mano', 'mind': 'cittaṃ',
     'mind accompanied': t['acc'] + ' cetasā', 'mind is accompanied': 'cittaṃ / sahagataṃ',
     'mind-consciousness': 'manoviññāṇa', 'mind-consciousness element': 'manoviññāṇadhātu', 'therefore': 'Tena',
     'therein': 'Tattha', 'together': 'saha', 'towards': NDE,
    }
    m.update(state_terms(s, 'acc'))
    m.update(extra or {})
    return m

DIRS = {
 'across': 'tiriyaṃ', 'direction': 'disaṃ', 'eastern': 'puratthimaṃ', 'eastern direction': 'puratthimaṃ vā disaṃ',
 'intermediate': 'vidisaṃ', 'intermediate direction': 'vidisaṃ', 'northern': 'uttaraṃ',
 'northern direction': 'uttaraṃ vā disaṃ', 'southern': 'dakkhiṇaṃ', 'southern direction': 'dakkhiṇaṃ vā disaṃ',
 'western direction': 'pacchimaṃ vā disaṃ',
}
PHAR = {'pervading': 'pharitvā', 'pervading and resolving': 'pharitvā adhimuccitvā', 'resolving': 'adhimuccitvā'}
VIHAR_FULL = {
 'carries': 'yāpeti', 'conducts': 'carati', 'dwells': 'viharati', 'goes': 'vattati', 'going': 'pāleti',
 'himself': NDE, 'keeps': 'pāleti', 'maintains': 'yapeti', 'moves': 'iriyati', 'therefore': 'Tena',
}
VIHAR_PE = {'dwells': 'viharatī', 'therefore': 'tena'}
TATHA = {
 'across': 'tiriyaṃ', 'direction': 'disaṃ', 'directions': 'vidisaṃ', 'fourth direction': 'catutthaṃ disaṃ',
 'intermediate': 'vidisaṃ', 'intermediate directions': 'vidisaṃ', 'likewise': 'tathā',
}
SABBA = {
 'all-inclusive': 'Pariyādāya', 'completely': 'sabbena sabbaṃ', 'entire': 'sabbāvantaṃ',
 'entire world': 'sabbāvantaṃ loka', 'every': 'sabbathā', 'everywhere': 'sabbadhi', 'expression': 'vacana',
 'fully': 'asesaṃ', 'himself': 'sabbattatāya', 'regarding': 'sabbattatāya', 'remainder': 'nissesaṃ',
 'respect': 'sabbathā',
}
VIPUL = {'abundant': 'vipulaṃ', 'expanded': 'mahaggataṃ', 'hostility': 'avero', 'ill': 'abyāpajjo',
         'measureless': 'appamāṇaṃ'}
FOUR = {'compassion': 'karuṇā', 'equanimity': 'upekkhā', 'joy': 'muditā', 'loving-kindness': 'mettā',
        'measureless': 'appamaññāyo', 'measureless states': 'appamaññāyo', 'sympathetic': 'muditā',
        'sympathetic joy': 'muditā'}

# Abhidhamma classification: jhāna formula
def jhana(s, extra=None):
    t = ST[s]
    m = {
     'absorption': 'jhānaṃ', 'absorption accompanied': 'jhānaṃ / ' + t['acc2'], 'accompanied': 'sahagataṃ',
     'associated': 'sampayuttā', 'away': 'virāgā', 'born': 'vivekajaṃ', 'develops': 'bhāveti',
     'develops the path': 'maggaṃ bhāveti', 'dwells': 'viharati', 'enters': 'upasampajja',
     'enters and dwells': 'upasampajja viharati', 'examination': 'vicārānaṃ', 'fading': 'virāgā',
     'fine-material': 'rūpūpapattiyā', 'fine-material sphere': 'rūpūpapattiyā', 'fourth meditative': 'catutthaṃ jhānaṃ',
     'fourth meditative absorption': 'catutthaṃ jhānaṃ', 'happiness': 'sukhaṃ', 'joy': 'pītiyā',
     'Joy and happiness': 'pītisukhaṃ', 'meditative': 'jhānaṃ', 'meditative absorption': 'jhānaṃ',
     'Meditative absorption': 'jhānaṃ', 'meditative absorption accompanied': 'jhānaṃ / ' + t['acc2'], 'mind': 'ceto',
     'monk': 'bhikkhu', 'occasion': 'samaye', 'path': 'maggaṃ', 'path for rebirth': 'rūpūpapattiyā maggaṃ',
     'pleasures': 'kāmehi', 'rebirth': 'ūpapattiyā', 'remaining': 'Avasesā', 'remaining things': 'Avasesā dhammā',
     'secluded': 'vivicceva', 'secluded from sense': 'vivicceva kāmehi', 'seclusion': 'viveka', 'sense': 'kāmehi',
     'sense pleasures': 'kāmehi', 'sphere': NDE, 'stilling': 'vūpasamā',
     'stilling of thought': 'vitakkavicārānaṃ vūpasamā', 'therein': 'Tattha', 'things': 'dhammā', 'thought': 'vitakka',
     'thought and examination': 'vitakkavicārānaṃ', 'unwholesome': 'akusalehi',
     'unwholesome things': 'akusalehi dhammehi',
    }
    m.update(state_terms(s, 'acc2'))
    m.update(extra or {})
    return m

# result (vipāka) variant adds these
VIPAKA = {
 'accumulated': 'upacitattā', 'contact': 'phasso', 'done': 'katattā', 'fine-material-sphere': 'rūpāvacarassa',
 'non-distraction': 'avikkhepo', 'sphere': 'āvacarassa', 'things are wholesome': 'dhammā kusalā',
 'wholesome': 'kusalassa', 'wholesome action': 'kusalassa kammassa',
}
# functional (kiriya) variant
KIRIYA = {
 'dwelling': 'vihāraṃ', 'fine-material-sphere': 'rūpāvacaraṃ', 'functional': 'kiriyaṃ', 'life': 'diṭṭhadhamma',
 'pleasant': 'sukha', 'unwholesome': 'ākusalaṃ', 'wholesome': 'kusalaṃ',
 'wholesome nor unwholesome': 'neva kusalaṃ nākusalaṃ',
}
UPEK_ABANDON = {'abandoning': 'pahānā', 'abandoning of happiness': 'sukhassa ca pahānā', 'happiness': 'sukhassa',
                'pain': 'dukkhassa'}

M = {}
M['2-13-0'] = {'analysis': 'vibhaṅgo', 'measureless': 'Appamaññā', 'measureless states': 'Appamaññā'}
M['2-13-1-0'] = {'classification': 'bhājanīyaṃ', 'discourses': 'Suttanta'}
M['2-642'] = dict(PERVADE4)
M['2-13-1-1-0'] = {'loving-kindness': 'Mettā'}
M['2-643'] = how('metta', {'dear': 'piyaṃ', 'feel': 'mettāyeyya', 'pleasing': 'manāpaṃ'})
M['2-13-1-2-0'] = {'compassion': 'Karuṇā'}
M['2-653'] = how('karuna', {'feel': 'karuṇāyeyya', 'miserable': 'durūpetaṃ', 'wretched': 'duggataṃ'})
M['2-13-1-3-0'] = {'joy': 'Muditā', 'sympathetic': 'Muditā', 'sympathetic joy': 'Muditā'}
M['2-663'] = how('mudita', {'dear': 'piyaṃ', 'glad': 'mudito', 'pleasing': 'manāpaṃ'})
M['2-13-1-4-0'] = {'equanimity': 'Upekkhā'}
M['2-673'] = how('upekkha', {'displeasing': 'amanāpaṃ', 'equanimous': 'upekkhako', 'pleasing': 'manāpaṃ'})
for s, base in (('metta', 643), ('karuna', 653), ('mudita', 663), ('upekkha', 673)):
    M[f'2-{base+1}'] = dict(DIRS)
    M[f'2-{base+2}'] = dict(PHAR)
    M[f'2-{base+3}'] = dict(VIHAR_FULL if s in ('metta', 'karuna') else VIHAR_PE)
    M[f'2-{base+4}'] = dict(TATHA)
    M[f'2-{base+5}'] = dict(SABBA)
    M[f'2-{base+6}'] = comment(s)
    M[f'2-{base+7}'] = dict(VIPUL)
    M[f'2-{base+8}'] = dict(PHAR)
    if base != 673:
        M[f'2-{base+9}'] = dict(VIHAR_PE)
M['2-682'] = dict(VIHAR_PE, **{'classification': 'bhājanīyaṃ', 'discourses': 'Suttanta', 'finished': NDE})
M['2-13-2-0'] = {'abhidhamma': 'Abhidhamma', 'classification': 'bhājanīyaṃ'}
M['2-683'] = dict(FOUR)
M['2-684'] = jhana('metta')
M['2-685'] = jhana('metta')
M['2-686'] = jhana('karuna')
M['2-687'] = jhana('karuna')
M['2-688'] = jhana('mudita', {'joy': 'pītiyā'})
M['2-689'] = jhana('mudita', {'joy': 'pītiyā'})
M['2-690'] = jhana('upekkha', UPEK_ABANDON)
M['2-691'] = dict(FOUR)
M['2-692'] = jhana('metta', VIPAKA)
M['2-693'] = jhana('karuna', VIPAKA)
M['2-694'] = jhana('mudita', VIPAKA)
M['2-695'] = jhana('upekkha', dict(VIPAKA, **UPEK_ABANDON))
M['2-696'] = dict(FOUR)
M['2-697'] = jhana('metta', KIRIYA)
M['2-698'] = jhana('upekkha', dict(KIRIYA, **UPEK_ABANDON, **{
 'abhidhamma': 'Abhidhamma', 'classification': 'bhājanīyaṃ', 'compassion': 'karuṇā', 'finished': NDE,
 'joy': 'muditā', 'sympathetic': 'muditā', 'sympathetic joy': 'muditā'}))
M['2-13-3-0'] = {'answers': NDE, 'questions': 'Pañhā', 'Questions and Answers': 'Pañhāpucchakaṃ', 'section': NDE,
                 'Section of Questions': 'Pañhāpucchakaṃ'}
M['2-699'] = dict(PERVADE4)
M['2-700'] = {'conflict': 'saraṇā', 'free': 'araṇā', 'involve': 'saraṇā', 'measureless': 'appamaññānaṃ',
              'measureless states': 'appamaññānaṃ', 'neutral': 'abyākatā', 'unwholesome': 'akusalā',
              'wholesome': 'kusalā'}
M['2-13-3-1-0'] = {'triads': 'Tikaṃ'}
M['2-701'] = {
 'abandoned': 'pahātabbā', 'able': 'upādāniyā', 'accompanied': 'sahagatā', 'accompanied by equanimity': 'upekkhāsahagatā',
 'accompanied by happiness': 'sukhasahagatā', 'accompanied by joy': 'pītisahagatā', 'accumulation': 'ācaya',
 'arise': 'uppādino', 'arisen': 'uppannā', 'associated': 'sampayuttā', 'belong': NDE, 'beyond': 'āsekkhā',
 'birth': NDE, 'cause': 'hetukā', 'causes': 'hetukā', 'clung': 'upādāniyā', 'connected': 'saṃkilesikā',
 'connected with defilement': 'saṃkilesikā', 'defilement': 'saṃkilesikā', 'describable': 'vattabbā',
 'dismantling': 'āpacaya', 'dominant': 'ādhipatino', 'dominant factor': 'ādhipatino', 'due to arise': 'uppādino',
 'equanimity': 'upekkhā', 'examination': 'vicārā', 'expanded': 'mahaggatā', 'external': 'bahiddhā',
 'external objects': 'bahiddhārammaṇā', 'factor': 'ādhipatino', 'feeling': 'vedanāya',
 'future object': 'anāgatārammaṇā', 'happiness': 'sukha', 'having': NDE, 'internal': 'ajjhattā',
 'internal and external': 'ajjhattabahiddhā', 'invisible': 'anidassana', 'invisible and offer': 'anidassanaappaṭighā',
 'joy': 'pīti', 'leading to accumulation': 'ācayagāmino', 'limited': 'parittārammaṇā', 'measureless': 'appamaññāyo',
 'measureless objects': 'appamāṇārammaṇā', 'measureless states': 'appamaññāyo', 'meditative': 'bhāvanāya',
 'meditative development': 'bhāvanāya', 'middling': 'Majjhimā', 'neither-painful-nor-pleasant': 'adukkhamasukhāya',
 'neutral': 'abyākatā', 'object': 'ārammaṇā', 'objects': 'ārammaṇā', 'past object': 'atītārammaṇā', 'path': 'magga',
 'pleasant': 'sukhāya', 'pleasant feeling': 'sukhāya vedanāya', 'present object': 'paccuppannārammaṇā',
 'resistance': 'appaṭighā', 'results nor things': 'nevavipākanavipākadhammadhammā', 'seeing': 'dassanena',
 'subject to result': 'vipākadhammadhammā', 'things': 'dhammā', 'things subject': 'vipākadhammadhammā',
 'thought': 'vitakka', 'training': 'sekkha', 'undefiled': 'Asaṃkiliṭṭha', 'unfixed': 'aniyatā', 'wholesome': 'kusalā',
}
M['2-13-3-2-0'] = {'pairs': 'Dukaṃ'}
M['2-702'] = {
 'abandoned': 'pahātabbā', 'accompanied': 'sahagatā', 'accompanied by equanimity': 'upekkhāsahagatā',
 'accompanied by happiness': 'sukhasahagatā', 'accompanied by joy': 'pītisahagatā', 'along': 'ānuparivattino',
 'analysis': 'vibhaṅgo', 'answers': NDE, 'arise': 'sahabhuno', 'associated': 'sampayuttā', 'belong': NDE,
 'birth': NDE, 'cannot': 'na', 'causes': 'hetukā', 'clinging': 'upādānā', 'conditioned': 'saṅkhatā',
 'conflict': 'araṇā', 'conjoined': 'saṃsaṭṭhā', 'defilements': 'kilesā', 'derived': 'upādā', 'describable': 'vattabbā',
 'dissociated': 'vippayuttā', 'equanimity': 'upekkhā', 'examination': 'vicārā', 'external': 'bāhirā',
 'factors': 'cetasikā', 'fetters': 'saṃyojanā', 'fine-material': 'rūpāvacarā', 'fine-material sphere': 'rūpāvacarā',
 'finished': 'niṭṭhito', 'floods': 'oghā', 'follow': 'ānuparivattino', 'free': 'araṇā', 'grasping': 'parāmāsā',
 'happiness': 'sukha', 'having': 'sahetukā', 'hindrances': 'nīvaraṇā', 'immaterial': 'arūpā',
 'immaterial sphere': 'arūpāvacarā', 'invisible': 'anidassanā', 'joy': 'pīti', 'known': 'viññeyyā',
 'loving-kindness': 'Mettā', 'means': 'kenaci', 'measureless': 'appamaññāyo', 'measureless states': 'appamaññāyo',
 'meditative': 'bhāvanāya', 'meditative development': 'bhāvanāya', 'mental': 'cetasikā', 'mental factors': 'cetasikā',
 'mental taints': 'āsavā', 'mind': 'citta', 'minds': 'cittā', 'non-root': 'na hetu', 'objects': 'ārammaṇā',
 'originated': 'samuṭṭhānā', 'questions': 'Pañhā', 'Questions and Answers': 'Pañhāpucchakaṃ', 'resistance': 'appaṭighā',
 'root': 'hetu', 'roots': 'hetū', 'section': NDE, 'Section of Questions': 'Pañhāpucchakaṃ', 'seeing': 'dassanena',
 'sense': 'kāmāvacarā', 'sense sphere': 'kāmāvacarā', 'sphere': 'āvacarā', 'subject to mental': 'sāsavā',
 'surpassable': 'sauttarā', 'taints': 'āsavā', 'thought': 'vitakkā', 'ties': 'ganthā', 'together': 'saha',
 'unfixed': 'aniyatā', 'worldly': 'lokiyā', 'wrong': 'parāmāsā', 'wrong grasping': 'parāmāsā', 'yokes': 'yogā',
}

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
