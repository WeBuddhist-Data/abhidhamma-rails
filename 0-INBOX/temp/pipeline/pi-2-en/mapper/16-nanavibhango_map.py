import pathlib
d = pathlib.Path(__file__).parent
ch = '16-nanavibhango'
NDE = '(no direct equivalent)'

def J(*ds):
    out = {}
    for x in ds:
        out.update(x)
    return out

GROUND = {'ground': 'vatthu', 'ground of knowledge': 'ñāṇavatthu', 'knowledge': 'ñāṇa'}
# "the wisdom, understanding ... non-delusion, investigation of things, right view (that arises concerning X)"
FORM = {
 'arises': 'uppajjati', 'concerning': 'ārabbha', 'investigation': 'vicayo', 'investigation of things': 'dhammavicayo',
 'non-delusion': 'amoho', 'right': 'sammā', 'therein': 'tattha', 'things': 'dhamma', 'understanding': 'pajānanā',
 'view': 'diṭṭhi', 'view that arises': 'uppajjati / sammādiṭṭhi', 'wisdom': 'paññā',
}

# matrix of ones (2-751) and its exposition (2-761, 2-766) share the five-consciousness list
ONES_TAIL = {
 'adopt': 'kappeti', 'attainment': 'samāpajjati', 'away': 'cavati', 'bodily': 'kāyakammaṃ',
 'bodily action': 'kāyakammaṃ', 'cognise': 'paṭivijānāti', 'consciousness': 'viññāṇā', 'dream': 'supinaṃ',
 'emerge': 'vuṭṭhāti', 'enter': 'samāpajjati', 'except': 'aññatra', 'falling': 'abhinipāta', 'kinds': NDE,
 'kinds of consciousness': 'viññāṇā', 'pass': 'cavati', 'posture': 'iriyāpathaṃ', 'reborn': 'uppajjati',
 'sleep': 'supati', 'thing': 'dhammaṃ', 'undertake': 'paṭṭhapeti', 'unwholesome': 'ākusalaṃ',
 'unwholesome thing': 'kusalākusalaṃ dhammaṃ', 'verbal': 'vacīkammaṃ', 'verbal action': 'vacīkammaṃ',
 'wake': 'paṭibujjhati', 'wholesome': 'kusalākusalaṃ', 'immediate': 'samanantarā', 'succession': 'samanantarā',
 'makes': 'vibhāvanā', 'plain': 'vibhāvanā', 'really': 'yāthāvaka', 'wisdom': 'paññā',
 'wisdom that makes': 'vibhāvanā paññā', 'bases': 'vatthu',
}

# matrix of twos (2-752) / its exposition (2-767): "X paññā" items
TWOS = {
 'able': 'saṃyojaniyā', 'accompanied': 'sahagatā', 'accompanied by equanimity': 'upekkhāsahagatā',
 'accompanied by happiness': 'sukhasahagatā', 'accompanied by joy': 'pītisahagatā', 'beyond': 'uttarā', 'birth': NDE,
 'bound': 'saṃyojaniyā', 'bound by fetters': 'saṃyojaniyā', 'bound by ties': 'ganthaniyā',
 'bound by yokes': 'yoganiyā', 'brings': 'jāpikā', 'brought': 'jāpita', 'cannot': 'na', 'clinging': 'upādāna',
 'clung': 'upādāniyā', 'connected': 'saṃkilesikā', 'connected with defilement': 'saṃkilesikā',
 'defilement': 'saṃkilesikā', 'defilements': 'kilesa', 'dissociated': 'vippayuttā',
 'dissociated from clinging': 'upādānavippayuttā', 'dissociated from wrong': 'parāmāsavippayuttā',
 'equanimity': 'upekkhā', 'examination': 'vicārā', 'fetters': 'saṃyojaniyā', 'fine-material': 'rūpāvacarā',
 'fine-material sphere': 'rūpāvacarā', 'fixed': 'niyatā', 'Fixed wisdom': 'niyatā paññā',
 'fixed wisdom': 'niyatā paññā', 'floods': 'oghaniyā', 'goal': 'attha', 'grasped': 'parāmaṭṭhā',
 'grasping': 'parāmāsa', 'happiness': 'sukha', 'hindrances': 'nīvaraṇiyā', 'immaterial': 'arūpāvacarā',
 'immaterial sphere': 'arūpāvacarā', 'joy': 'pīti', 'known': 'viññeyyā', 'leads': 'niyyānikā', 'means': 'kenaci',
 'mental': 'āsava', 'mental taints': 'āsava', 'obstructed': 'nīvaraṇiyā', 'sense': 'kāmāvacarā',
 'sense sphere': 'kāmāvacarā', 'sphere': 'āvacarā', 'subject to mental': 'sāsavā', 'surpassable': 'sauttarā',
 'surpassable wisdom': 'sauttarā paññā', 'Surpassable wisdom': 'sauttarā paññā', 'swept': 'oghaniyā',
 'taints': 'āsava', 'thought': 'vitakkā', 'ties': 'ganthaniyā', 'unfixed': 'aniyatā',
 'unfixed wisdom': 'aniyatā paññā', 'unsurpassed': 'anuttarā', 'unsurpassed wisdom': 'anuttarā paññā',
 'wisdom': 'paññā', 'Wisdom accompanied': 'pītisahagatā paññā', 'wisdom accompanied': 'sukhasahagatā paññā',
 'wisdom connected': 'saṃkilesikā paññā', 'Wisdom connected': 'saṃkilesikā paññā',
 'Wisdom dissociated': 'āsavavippayuttā sāsavā paññā', 'wisdom dissociated': 'āsavavippayuttā sāsavā paññā',
 'Wisdom included': 'pariyāpannā paññā', 'wisdom included': 'pariyāpannā paññā',
 'wisdom not accompanied': 'na pītisahagatā paññā', 'wisdom not connected': 'asaṃkilesikā paññā',
 'wisdom not included': 'apariyāpannā paññā', 'wisdom subject': 'sāsavā paññā', 'Wisdom subject': 'sāsavā paññā',
 'wisdom that brings': 'atthajāpikā paññā', 'Wisdom that brings': 'atthajāpikā paññā',
 'Wisdom that leads': 'niyyānikā paññā', 'wisdom that leads': 'niyyānikā paññā',
 'wisdom whose goal': 'jāpitatthā paññā', 'Wisdom with examination': 'savicārā paññā',
 'wisdom with examination': 'savicārā paññā', 'Wisdom with joy': 'sappītikā paññā',
 'wisdom with joy': 'sappītikā paññā', 'Wisdom with thought': 'savitakkā paññā',
 'wisdom with thought': 'savitakkā paññā', 'wisdom without examination': 'avicārā paññā',
 'wisdom without joy': 'appītikā paññā', 'wisdom without mental': 'anāsavā paññā',
 'wisdom without thought': 'avitakkā paññā', 'worldly': 'lokiyā', 'Worldly wisdom': 'lokiyā paññā',
 'worldly wisdom': 'lokiyā paññā', 'wrong': 'parāmāsa', 'wrong grasping': 'parāmāsa', 'wrongly': 'parāmaṭṭhā',
 'wrongly grasped': 'parāmaṭṭhā', 'yokes': 'yoganiyā',
}

M = {}
M['2-16-0'] = {'analysis': 'vibhaṅgo', 'knowledge': 'Ñāṇa'}
M['2-16-1-0'] = {'matrix': 'mātikā', 'ones': 'Ekaka'}
M['2-751'] = J(GROUND, ONES_TAIL, {
 'abandoned': 'pahātabbā', 'able': 'upādāniyā', 'accompanied': 'sahagatā', 'accompanied by joy': 'pītisahagatā',
 'accumulation': 'ācaya', 'arise': 'uppajjanti', 'arisen': 'Uppanna', 'arisen objects': 'uppannārammaṇā',
 'attention': 'amanasikārā', 'belong': NDE, 'beyond': 'āsekkhā', 'birth': NDE, 'bound': 'saṃyojaniyā',
 'bound by fetters': 'saṃyojaniyā', 'bound by ties': 'ganthaniyā', 'bound by yokes': 'yoganiyā',
 'bringing-to-mind': 'asamannāhārā', 'causes': 'hetukā', 'clung': 'upādāniyā', 'conditioned': 'saṅkhatā',
 'connected': 'saṃkilesikā', 'connected with defilement': 'saṃkilesikā', 'defiled': 'saṃkilesikā',
 'defilement': 'saṃkilesikā', 'different': 'Nānā', 'dismantling': 'āpacaya', 'dissociated': 'vippayuttā',
 'engagement': 'anābhogā', 'examination': 'vicārā', 'experience': 'paccanubhonti', 'external': 'bāhirārammaṇā',
 'external objects': 'bāhirārammaṇā', 'factors': 'acetasikā', 'fetters': 'saṃyojaniyā', 'field': 'gocara',
 'field and range': 'gocaravisayaṃ', 'fine-material': 'rūpāvacarā', 'fine-material sphere': 'rūpāvacarā',
 'floods': 'oghaniyā', 'grasped': 'parāmaṭṭhā', 'hindrances': 'nīvaraṇiyā', 'immaterial': 'arūpāvacarā',
 'immaterial sphere': 'arūpāvacarā', 'internal': 'Ajjhattika', 'internal bases': 'Ajjhattikavatthukā', 'joy': 'pīti',
 'limited': 'parittā', 'meditative': 'bhāvanāya', 'meditative development': 'bhāvanāya', 'mental': 'acetasikā',
 'mental factors': 'acetasikā', 'mental taints': 'sāsavā', 'mere': 'mattā', 'neutral': 'abyākatā',
 'not-after': 'acarimaṃ', 'not-before': 'apubbaṃ', 'objects': 'ārammaṇā', 'objects arisen': 'purejātārammaṇā',
 'obstructed': 'nīvaraṇiyā', 'outside': 'apariyāpannā', 'roots': 'hetū', 'seeing': 'dassanena', 'sense': 'kāmāvacarā',
 'sense sphere': 'kāmāvacarā', 'sphere': 'āvacarā', 'subject to mental': 'sāsavā', 'swept': 'oghaniyā',
 'taints': 'sāsavā', 'thought': 'vitakka', 'ties': 'ganthaniyā', 'training': 'sekkha', 'unbroken': 'Asambhinna',
 'undefiled': 'asaṃkiliṭṭha', 'unfixed': 'aniyatā', 'uninterruptedly': 'abbokiṇṇā', 'worldly': 'lokiyā',
 'wrongly': 'parāmaṭṭhā', 'wrongly grasped': 'parāmaṭṭhā', 'yokes': 'yoganiyā'})
M['2-16-2-0'] = {'matrix': 'mātikā', 'twos': 'Duka'}
# the matrix list starts each item with a capital; the positive member only occurs capitalised there
M['2-752'] = J(GROUND, TWOS, {
 'goal': 'Attha', 'surpassable': 'Sauttarā', 'surpassable wisdom': 'Sauttarā paññā', 'Surpassable wisdom': 'Sauttarā paññā',
 'Wisdom dissociated': 'Āsavavippayuttā sāsavā paññā', 'wisdom dissociated': 'Āsavavippayuttā sāsavā paññā',
 'wisdom that brings': 'Atthajāpikā paññā', 'Wisdom that brings': 'Atthajāpikā paññā',
 'Wisdom with examination': 'Savicārā paññā', 'wisdom with examination': 'Savicārā paññā',
 'Wisdom with joy': 'Sappītikā paññā', 'wisdom with joy': 'Sappītikā paññā', 'Wisdom with thought': 'Savitakkā paññā',
 'wisdom with thought': 'Savitakkā paññā', 'worldly': 'Lokiyā', 'Worldly wisdom': 'Lokiyā paññā',
 'worldly wisdom': 'Lokiyā paññā', 'Wisdom included': 'Pariyāpannā paññā', 'wisdom included': 'Pariyāpannā paññā',
 'fixed': 'Niyatā', 'Fixed wisdom': 'Niyatā paññā', 'fixed wisdom': 'Niyatā paññā', 'leads': 'Niyyānikā',
 'Wisdom that leads': 'Niyyānikā paññā', 'wisdom that leads': 'Niyyānikā paññā'})
M['2-16-3-0'] = {'matrix': 'mātikā', 'threes': 'Tika'}
M['2-753'] = J(GROUND, {
 'able': 'upādāniyā', 'accompanied': 'sahagatā', 'accompanied by equanimity': 'upekkhāsahagatā',
 'accompanied by happiness': 'sukhasahagatā', 'accompanied by joy': 'pītisahagatā', 'accumulation': 'ācaya',
 'arise': 'uppādinī', 'arisen': 'uppannā', 'Arisen wisdom': 'Uppannā paññā', 'belong': NDE, 'beyond': 'asekkhā',
 'birth': NDE, 'cause': 'hetukā', 'clung': 'upādāniyā', 'concerning': NDE, 'dismantling': 'apacaya',
 'dominant': 'ādhipatinī', 'dominant factor': 'ādhipatinī', 'due to arise': 'uppādinī', 'equanimity': 'upekkhā',
 'examination': 'vicārā', 'expanded': 'mahaggatā', 'expanded object': 'mahaggatārammaṇā',
 'expanded wisdom': 'mahaggatā paññā', 'external': 'bahiddhā', 'external object': 'bahiddhārammaṇā',
 'external wisdom': 'bahiddhā paññā', 'factor': 'ādhipatinī', 'future object': 'anāgatārammaṇā',
 'future wisdom': 'anāgatā paññā', 'giving': 'Dāna', 'happiness': 'sukha', 'higher wisdom': 'adhipaññāya',
 'internal': 'ajjhattā', 'internal and external': 'ajjhattabahiddhā', 'internal object': 'ajjhattārammaṇā',
 'Internal wisdom': 'Ajjhattā paññā', 'joy': 'pīti', 'joy and wisdom': 'Pītisahagatā paññā',
 'leading to accumulation': 'ācayagāminī', 'leading to dismantling': 'apacayagāminī', 'learning': 'suta',
 'limited': 'parittā', 'limited object': 'parittārammaṇā', 'Limited wisdom': 'Parittā paññā',
 'limited wisdom': 'Parittā paññā', 'means': 'upāya', 'measureless': 'appamāṇā',
 'measureless object': 'appamāṇārammaṇā', 'measureless wisdom': 'appamāṇā paññā', 'meditative': 'bhāvanā',
 'meditative development': 'bhāvanā', 'mind': 'citte', 'object': 'ārammaṇā', 'past object': 'atītārammaṇā',
 'Past wisdom': 'Atītā paññā', 'path': 'magga', 'present object': 'paccuppannārammaṇā',
 'present wisdom': 'paccuppannā paññā', 'reflection': 'Cintā', 'skill': 'kosallaṃ',
 'subject to result': 'vipākadhammadhammā', 'thing': 'dhammā', 'thing subject': 'vipākadhammadhammā',
 'thought': 'vitakka', 'training': 'sekkhā', 'unarisen': 'anuppannā', 'unarisen wisdom': 'anuppannā paññā',
 'virtue': 'sīla', 'wisdom': 'paññā', 'Wisdom accompanied': 'Pītisahagatā paññā',
 'wisdom accompanied': 'sukhasahagatā paññā', 'wisdom both internal': 'ajjhattabahiddhā paññā',
 'Wisdom concerning higher': 'Adhisīle paññā', 'wisdom concerning higher': 'adhipaññāya paññā',
 'wisdom due': 'uppādinī paññā', 'wisdom leading': 'apacayagāminī paññā', 'Wisdom leading': 'Ācayagāminī paññā',
 'wisdom made': 'sutamayā paññā', 'Wisdom made': 'Cintāmayā paññā',
 'Wisdom with thought': 'Savitakkasavicārā paññā', 'wisdom with thought': 'Savitakkasavicārā paññā',
 'wisdom without thought': 'avitakkavicāramattā paññā'})
M['2-16-4-0'] = {'fours': 'Catukka', 'matrix': 'mātikā'}
M['2-754'] = J(GROUND, {
 'accumulation': 'ācayāya', 'aging': 'Jarā', 'aging and death': 'Jarāmaraṇe', 'analytical': 'paṭisambhidā',
 'analytical knowledges': 'paṭisambhidā', 'Analytical Knowledges': 'paṭisambhidā', 'birth': 'Jātiyā',
 'breaking': 'nibbedha', 'cessation': 'nirodhe', 'cessation of aging': 'jarāmaraṇanirodhe',
 'cessation of formations': 'saṅkhāranirodhe', 'cessation of suffering': 'dukkhanirodhe', 'clinging': 'upādāne',
 'conformity': 'ānulomikaṃ', 'consciousness': 'viññāṇe', 'contact': 'phasse', 'conventional': 'sammuti',
 'craving': 'taṇhāya', 'death': 'maraṇe', 'disenchantment': 'nibbidāya', 'dismantling': 'apacayāya',
 'distinction': 'visesa', 'encompassing': 'pariye', "encompassing others' minds": 'pariye', 'endowed': 'samaṅgissa',
 'existence': 'bhave', 'feeling': 'vedanāya', 'fine-material': 'rūpāvacarā', 'fine-material sphere': 'rūpāvacarā',
 'form': 'rūpe', 'formations': 'saṅkhāresu', 'fruit': 'phala', 'immaterial': 'arūpāvacarā',
 'immaterial sphere': 'arūpāvacarā', 'inferential': 'anvaye', 'inferential knowledge': 'anvaye ñāṇaṃ',
 'knowledge': 'ñāṇaṃ', 'knowledge of aging': 'Jarāmaraṇe ñāṇaṃ', 'knowledge of consciousness': 'viññāṇe ñāṇaṃ',
 'knowledge of encompassing': 'pariye / ñāṇaṃ', 'knowledge of formations': 'saṅkhāresu ñāṇaṃ',
 'knowledges': 'paṭisambhidā', 'material': 'rūpe', 'material form': 'rūpe', 'mentality': 'nāma',
 'mentality and material': 'nāmarūpe', 'minds': 'pariye', 'modes': 'paṭipadā', 'objects': 'ārammaṇāni',
 'origin': 'samudaye', 'origin of suffering': 'dukkhasamudaye', 'others': 'pariye', "others' minds": 'pariye',
 'path': 'magga', 'penetration': 'paṭivedhāya', 'practice': 'paṭipadā', 'sense': 'Kāmāvacarā',
 'sense sphere': 'Kāmāvacarā', 'sense-fields': 'āyatane', 'shares in breaking': 'nibbedhabhāginī',
 'shares in decline': 'Hānabhāginī', 'shares in distinction': 'visesabhāginī',
 'shares in stability': 'ṭhitibhāginī', 'sphere': 'āvacarā', 'stability': 'ṭhiti', 'suffering': 'Dukkhe',
 'teaching': 'Dhamme', 'truths': 'saccānulomikaṃ', 'wisdom': 'paññā', 'wisdom for accumulation': 'paññā ācayāya',
 'wisdom for disenchantment': 'paññā nibbidāya', 'wisdom for dismantling': 'paññā apacayāya',
 'wisdom not included': 'apariyāpannā paññā', 'wisdom that shares': 'ṭhitibhāginī paññā',
 'Wisdom that shares': 'Hānabhāginī paññā'})
M['2-16-5-0'] = {'fives': 'Pañcaka', 'matrix': 'mātikā'}
M['2-755'] = J(GROUND, {'concentration': 'samādhi', 'five-factored': 'Pañcaṅgiko', 'five-knowledged': 'pañcañāṇiko',
                        'right': 'sammā'})
M['2-16-6-0'] = {'matrix': 'mātikā', 'Matrix of Sixes': 'Chakkamātikā', 'sixes': 'Chakka'}
M['2-756'] = J(GROUND, {'direct': 'abhiññāsu', 'direct knowledges': 'abhiññāsu', 'knowledges': 'abhiññāsu',
                        'wisdom': 'paññā'})
M['2-16-7-0'] = {'matrix': 'mātikā', 'sevens': 'Sattaka'}
M['2-757'] = J(GROUND, {'grounds': 'vatthūni', 'seventy-seven': 'Sattasattati'})
M['2-16-8-0'] = {'eights': 'Aṭṭhaka', 'matrix': 'mātikā'}
M['2-758'] = J(GROUND, {'fruits': 'phalesu', 'paths': 'maggesu', 'wisdom': 'paññā'})
M['2-16-9-0'] = {'matrix': 'mātikā', 'nines': 'Navaka'}
M['2-759'] = J(GROUND, {'attainments': 'samāpattīsu', 'dwelling': 'vihāra', 'successive': 'anupubba', 'wisdom': 'paññā'})
M['2-16-10-0'] = {'matrix': 'mātikā', 'Matrix of Tens': 'Dasakamātikā', 'tens': 'Dasaka'}
M['2-760'] = J(GROUND, {
 'absorptions': 'jhāna', 'assemblies': 'parisāsu', 'attainments': 'samāpattīnaṃ', 'away': 'cutūpapātaṃ',
 'beings': 'sattānaṃ', 'bull': 'āsabhaṃ', 'cause': 'hetuso', 'circumstance': 'ṭhānaso', 'claims': 'paṭijānāti',
 'claims the place': 'ṭhānaṃ paṭijānāti', 'cleansing': 'vodānaṃ', 'concentrations': 'samādhi',
 'defilement': 'saṃkilesaṃ', 'destruction': 'khayaṃ', 'different': 'nānā', 'elements': 'dhātu',
 'emergence': 'vuṭṭhānaṃ', 'endowed': 'samannāgato', 'everywhere': 'sabbattha', 'faculties': 'indriya',
 'impossible': 'aṭṭhānato', 'inclinations': 'ādhimuttikataṃ', 'knows': 'pajānāti', 'leads': 'gāminiṃ',
 'liberations': 'vimokkha', 'lion': 'sīha', 'lives': 'pubbenivāsānussatiṃ', 'meditative': 'jhāna',
 'meditative absorptions': 'jhāna', 'mental': 'āsavānaṃ', 'mental taints': 'āsavānaṃ', 'passing': 'cutūpapātaṃ',
 'past lives': 'pubbenivāsānussatiṃ', 'persons': 'parapuggalānaṃ', 'place': 'ṭhānaṃ', 'power': 'balaṃ',
 'power the Tathāgata': 'balaṃ āgamma tathāgato', 'really': 'yathābhūtaṃ', 'rebirth': 'ūpapātaṃ',
 'recollection': 'ānussatiṃ', 'relying': 'āgamma', 'roar': 'nādaṃ', 'roars': 'nadati',
 'roars his lion': 'sīhanādaṃ nadati', 'rolling': 'pavatteti', 'rolling the wheel': 'brahmacakkaṃ pavatteti',
 'sets rolling': 'pavatteti', 'taints': 'āsavānaṃ', 'Tathāgata claims': 'tathāgato / paṭijānāti', 'ten': 'dasa',
 'ten Tathāgata-powers': 'dasa / tathāgatabalāni', 'undertakings': 'samādānānaṃ',
 'undertakings of action': 'kammasamādānānaṃ', 'wheel': 'cakkaṃ', 'wheel of Brahmā': 'brahmacakkaṃ'})
M['2-16-11-0'] = {'matrix': 'Mātikā'}
M['2-16-11-1-0'] = {'exposition': 'niddeso', 'ones': 'Ekaka'}
M['2-761'] = {
 'abandoned': 'pahātabbameva', 'able': 'upādāniyameva', 'accompanied': 'sahagatameva',
 'accompanied by joy': 'pītisahagatameva', 'accumulation': 'ācaya', 'aging': 'jarā', 'arisen': 'uppannaṃ',
 'belonging': NDE, 'beyond': 'āsekkha', 'birth': NDE, 'bound': 'saṃyojaniyameva',
 'bound by fetters': 'saṃyojaniyameva', 'bound by ties': 'ganthaniyameva', 'bound by yokes': 'yoganiyameva',
 'causes': 'hetukameva', 'clung': 'upādāniyameva', 'conditioned': 'saṅkhatameva', 'connected': 'saṃkilesikameva',
 'connected with defilement': 'saṃkilesikameva', 'consciousness': 'viññāṇā', 'defiled': 'saṃkilesikameva',
 'defilement': 'saṃkilesikameva', 'dismantling': 'āpacaya', 'dissociated': 'vippayuttameva',
 'examination': 'vicārameva', 'factors': 'acetasikameva', 'fetters': 'saṃyojaniyameva',
 'fine-material': 'rūpāvacarameva', 'fine-material sphere': 'rūpāvacarameva', 'floods': 'oghaniyameva',
 'grasped': 'parāmaṭṭhameva', 'having': NDE, 'hindrances': 'nīvaraṇiyameva', 'immaterial': 'arūpameva',
 'immaterial sphere': 'arūpāvacarameva', 'impermanent': 'aniccameva', 'joy': 'pīti', 'kinds': NDE,
 'kinds of consciousness': 'viññāṇā', 'knowable': 'viññeyyameva', 'limited': 'parittameva',
 'meditative': 'bhāvanāya', 'meditative development': 'bhāvanāya', 'mental': 'acetasikameva',
 'mental factors': 'acetasikameva', 'mental taints': 'sāsavameva', 'mind-consciousness': 'manoviññāṇa',
 'neutral': 'abyākatameva', 'objects': 'ārammaṇameva', 'obstructed': 'nīvaraṇiyameva',
 'outside': 'apariyāpannameva', 'overcome': 'ābhibhūtameva', 'roots': 'hetumeva', 'seeing': 'dassanena',
 'sense': 'kāmāvacarameva', 'sense sphere': 'kāmāvacarameva', 'simply': 'hetumeva', 'sphere': 'āvacarameva',
 'subject to mental': 'sāsavameva', 'swept': 'oghaniyameva', 'taints': 'sāsavameva', 'thought': 'vitakka',
 'ties': 'ganthaniyameva', 'training': 'sekkha', 'undefiled': 'asaṃkiliṭṭha', 'unfixed': 'aniyatameva',
 'worldly': 'lokiyameva', 'wrongly': 'parāmaṭṭhameva', 'wrongly grasped': 'parāmaṭṭhameva',
 'yokes': 'yoganiyameva',
}
M['2-762'] = {
 'arise': 'uppajjanti', 'arisen': 'uppannasmiṃ', 'arisen objects': 'uppannārammaṇā', 'bases': 'vatthukā',
 'body-consciousness': 'kāyaviññāṇassa', 'consciousness': 'viññāṇā', 'different': 'Nānā',
 'ear-consciousness': 'sotaviññāṇassa', 'external': 'bāhirā', 'external objects': 'bāhirārammaṇā',
 'eye-consciousness': 'cakkhuviññāṇassa', 'internal': 'ajjhattikā', 'internal bases': 'Ajjhattikavatthukā',
 'kinds': NDE, 'kinds of consciousness': 'viññāṇā', 'nose-consciousness': 'ghānaviññāṇassa', 'object': 'ārammaṇe',
 'objects': 'ārammaṇā', 'objects arisen': 'purejātārammaṇā', 'thing': 'aññaṃ',
 'tongue-consciousness': 'jivhāviññāṇassa', 'unbroken': 'asambhinnasmiṃ',
}
M['2-763'] = {
 'body-consciousness': 'kāyaviññāṇaṃ', 'body-consciousness experience': 'kāyaviññāṇaṃ na paccanubhoti',
 'ear-consciousness': 'sotaviññāṇaṃ', 'experience': 'paccanubhoti',
 'experience the field': 'gocaravisayaṃ paccanubhontī', 'eye-consciousness': 'cakkhuviññāṇaṃ',
 'eye-consciousness experience': 'cakkhuviññāṇaṃ na paccanubhoti', 'field': 'gocara',
 'field and range': 'gocaravisayaṃ', 'nose-consciousness': 'ghānaviññāṇaṃ',
 'range of body-consciousness': 'kāyaviññāṇassa gocaravisayaṃ',
 'range of eye-consciousness': 'cakkhuviññāṇassa gocaravisayaṃ', 'tongue-consciousness': 'jivhāviññāṇaṃ',
}
M['2-764'] = {
 'arise': 'uppajjanti', 'attends': 'manasikarontassa', 'attention': 'amanasikārā', 'bringing-to-mind': 'asamannāhārā',
 'brings': 'samannāharantassa', 'mind': 'samannāharantassa', 'moment': 'khaṇe', 'not-after': 'acarimaṃ',
 'not-before': 'apubbaṃ', 'single': 'ekakkhaṇe', 'succession': 'paṭipāṭiyā', 'unbroken': 'paṭipāṭiyā',
 'uninterruptedly': 'abbokiṇṇā',
}
M['2-765'] = {
 'arise': 'uppajjati', 'arising': 'uppanna', 'arising of body-consciousness': 'kāyaviññāṇassa uppannasamanantarā',
 'arising of eye-consciousness': 'cakkhuviññāṇassa uppannasamanantarā', 'body-consciousness': 'kāyaviññāṇaṃ',
 'body-consciousness arise': 'kāyaviññāṇaṃ na uppajjati', 'ear-consciousness': 'sotaviññāṇaṃ',
 'eye-consciousness': 'cakkhuviññāṇaṃ', 'eye-consciousness arise': 'cakkhuviññāṇaṃ na uppajjati',
 'immediate': 'samanantarā', 'nose-consciousness': 'ghānaviññāṇaṃ', 'succession': 'samanantarā',
 'tongue-consciousness': 'jivhāviññāṇaṃ',
}
M['2-766'] = J(GROUND, ONES_TAIL, {
 'attention': 'manasikāro', 'bringing-to-mind': 'samannāhāro', 'coming': 'āpāta', 'element': 'dhātuyā',
 'engagement': 'ābhogo', 'lying': 'seyyaṃ', 'mere': 'mattā', 'mind': 'mano', 'mind element': 'manodhātuyā',
 'ones': 'Ekakaṃ', 'sitting': 'nisajjaṃ', 'standing': 'ṭhānaṃ', 'towards': 'āvaṭṭanā', 'turning': 'āvaṭṭanā',
 'walking': 'gamanaṃ'})
M['2-16-11-2-0'] = {'exposition': 'niddeso', 'twos': 'Duka'}
M['2-767'] = J(GROUND, TWOS, {
 'arahant': 'arahato', 'associated': 'sampayuttā', 'attainment': 'samāpattiṃ', 'direct': 'abhiññaṃ',
 'direct knowledge': 'abhiññaṃ', 'equanimity is wisdom': 'Upekkhāsampayuttā paññā',
 'examination is wisdom': 'Vicārasampayuttā paññā', 'fruits': 'phalesu', 'fruits is wisdom': 'phalesu paññā',
 'functional': 'kiriyābyākate', 'functional neutral': 'kiriyābyākate', 'happiness is wisdom': 'Sukhasampayuttā paññā',
 'joy is wisdom': 'Pītisampayuttā paññā', 'neutral': 'ābyākate', 'paths': 'maggesu',
 'paths is wisdom': 'maggesu paññā', 'planes': 'bhūmīsu', 'planes is wisdom': 'bhūmīsu kusalābyākate paññā',
 'produced': 'uppannāya', 'producing': 'uppādentassa', 'sphere are wisdom': 'apariyāpannā paññā',
 'sphere is wisdom': 'Kāmāvacarakusalābyākate paññā', 'therein': 'Tattha',
 'thought is wisdom': 'Vitakkasampayuttā paññā', 'twos': 'Dukaṃ', 'wholesome': 'kusale',
 'wholesome and neutral': 'kusalābyākate'})
M['2-16-11-3-0'] = {'exposition': 'niddeso', 'threes': 'Tika'}
M['2-768'] = {
 'acceptance': 'khantiṃ', 'arranged': 'vihitesu', 'attainment': 'samāpannassa', 'attainment is wisdom': 'samāpannassa paññā',
 'branches': 'ṭṭhānesu', 'concerning': NDE, 'conforming': 'anulomikaṃ', 'conformity': 'ānulomikaṃ',
 'consciousness': 'viññāṇaṃ', 'consideration': 'pekkhaṃ', 'craft': 'sippāyatanesu', 'entered': 'samāpannassa',
 'feeling': 'vedanā', 'fields': 'āyatanesu', 'form': 'rūpaṃ', 'formations': 'saṅkhārā', 'hearing': 'sutvā',
 'impermanent': 'anicca', 'kind': 'evarūpiṃ', 'learning': 'suta', 'material': 'rūpaṃ', 'material form': 'rūpaṃ',
 'meditative': 'bhāvanā', 'meditative development': 'bhāvanā', 'obtains': 'paṭilabhati',
 'ownership': 'kammassakataṃ', 'perception': 'saññā', 'preference': 'ruciṃ', 'reflection': 'nijjhāna',
 'science': 'vijjā', 'skill': 'yoga', 'therein': 'tattha', 'things': 'dhamma', 'truths': 'saccānulomikaṃ',
 'understanding': 'mudiṃ', 'view': 'diṭṭhiṃ', 'whatever': 'yaṃ', 'wisdom': 'paññā',
 'wisdom made': 'sutamayā paññā', 'Wisdom made': 'cintāmayā paññā',
}
M['2-769'] = J(FORM, {
 'attainment': 'samāpannassa', 'attainment is wisdom': 'samāpannassa paññā', 'entered': 'samāpannassa',
 'giving': 'Dānaṃ', 'meditative': 'bhāvanā', 'meditative development': 'bhāvanā', 'relation': 'ādhigaccha',
 'virtue': 'Sīlaṃ', 'wisdom made': 'sīlamayā paññā', 'Wisdom made': 'dānamayā paññā'})
M['2-770'] = J(FORM, {
 'concerning': NDE, 'attainment': 'samāpattiṃ', 'code': 'Pātimokkha', 'entering': 'samāpajjantassa',
 'fine-material-sphere': 'Rūpāvacarārūpāvacarasamāpattiṃ', 'fruits': 'phalesu', 'higher wisdom': 'adhipaññāya',
 'himself': NDE, 'immaterial-sphere': 'ārūpāvacara', 'mind': 'citte', 'monastic': 'Pātimokkha', 'paths': 'maggesu',
 'restraining': 'saṃvarantassa', 'restraint': 'saṃvaraṃ', 'virtue': 'sīle',
 'Wisdom concerning higher': 'adhisīle paññā', 'wisdom concerning higher': 'adhipaññāya paññā'})
M['2-771'] = J(FORM, {
 'abandoned': 'pahīyanti', 'arise': 'uppajjanti', 'arisen': 'uppannā', 'attending': 'manasikaroto',
 'case': 'tatrupāyā', 'cease': 'nirujjhanti', 'expansion': 'vepullāya', 'means': 'upāya',
 'perfection': 'pāripūriyā', 'skill': 'kosallaṃ', 'things': 'dhammā', 'unwholesome': 'akusalā',
 'unwholesome things': 'akusalā dhammā', 'wholesome': 'kusalā', 'wholesome things': 'kusalā dhammā'})
FUNC = {'functional': 'kiriyābyākate', 'functional neutral': 'kiriyābyākate', 'neutral': 'ābyākate',
        'planes': 'bhūmīsu', 'wholesome': 'kusale', 'wisdom': 'paññā'}
M['2-772'] = J(FUNC, {'planes is wisdom': 'bhūmīsu vipāke paññā', 'subject to result': 'vipākadhammadhammā',
                      'thing': 'dhammā', 'thing subject': 'vipākadhammadhammā'})
M['2-773'] = J(FUNC, {'able': 'upādāniyā', 'birth': NDE, 'clung': 'upādāniyā', 'fruits': 'phalesu',
                      'fruits is wisdom': 'phalesu paññā', 'paths': 'maggesu', 'planes is wisdom': 'bhūmīsu vipāke paññā'})
M['2-774'] = {
 'associated': 'sampayuttā', 'dissociated': 'vippayuttā', 'examination': 'vicāra',
 'examination is wisdom': 'vitakkavicārasampayuttā paññā', 'thought': 'vitakka', 'thought and examination': 'vitakkavicāra',
 'wisdom': 'paññā', 'wisdom dissociated': 'vitakkavicāravippayuttā paññā',
 'Wisdom dissociated': 'vitakkavippayuttā vicārasampayuttā paññā', 'Wisdom with thought': 'savitakkasavicārā paññā',
 'wisdom with thought': 'savitakkasavicārā paññā', 'wisdom without thought': 'avitakkavicāramattā paññā',
}
M['2-775'] = {
 'accompanied': 'sahagatā', 'accompanied by equanimity': 'upekkhāsahagatā', 'accompanied by happiness': 'sukhasahagatā',
 'accompanied by joy': 'pītisahagatā', 'associated': 'sampayuttā', 'equanimity': 'upekkhā',
 'equanimity is wisdom': 'upekkhāsampayuttā paññā', 'happiness': 'sukha', 'happiness is wisdom': 'sukhasampayuttā paññā',
 'joy': 'pīti', 'joy is wisdom': 'pītisampayuttā paññā', 'wisdom': 'paññā', 'wisdom accompanied': 'sukhasahagatā paññā',
 'Wisdom accompanied': 'pītisahagatā paññā',
}
M['2-776'] = J(FUNC, {
 'accumulation': 'ācaya', 'dismantling': 'apacaya', 'leading to accumulation': 'ācayagāminī',
 'leading to dismantling': 'apacayagāminī', 'paths': 'maggesu', 'paths is wisdom': 'maggesu paññā',
 'planes is wisdom': 'bhūmīsu kusale paññā', 'Wisdom leading': 'ācayagāminī paññā', 'wisdom leading': 'apacayagāminī paññā'})
M['2-777'] = J(FUNC, {
 'arahantship': 'arahatta', 'beyond': 'asekkhā', 'fruit': 'phale', 'fruits': 'phalesu', 'fruits is wisdom': 'phalesu paññā',
 'highest': 'upariṭṭhimā', 'paths': 'maggesu', 'planes is wisdom': 'bhūmīsu kiriyābyākate paññā', 'training': 'sekkhā'})
M['2-778'] = {
 'expanded': 'mahaggatā', 'expanded wisdom': 'mahaggatā paññā', 'fine-material': 'rūpāvacarārūpāvacarakusalābyākate',
 'fruits': 'phalesu', 'immaterial': 'ārūpāvacara', 'limited': 'parittā', 'limited wisdom': 'parittā paññā',
 'Limited wisdom': 'parittā paññā', 'measureless': 'appamāṇā', 'measureless wisdom': 'appamāṇā paññā',
 'neutral': 'ābyākate', 'paths': 'maggesu', 'sense': 'kāmāvacara', 'sense sphere': 'kāmāvacara', 'sphere': 'āvacara',
 'spheres': 'āvacara', 'wholesome': 'kusalābyākate', 'wholesome and neutral': 'kusalābyākate', 'wisdom': 'paññā',
}
M['2-779'] = J(FORM, {'limited': 'Paritte', 'limited object': 'parittārammaṇā', 'object': 'ārammaṇā', 'things': 'dhamme'})
M['2-780'] = J(FORM, {'expanded': 'Mahaggate', 'expanded object': 'mahaggatārammaṇā', 'object': 'ārammaṇā',
                      'things': 'dhamme'})
M['2-781'] = J(FORM, {'measureless': 'Appamāṇe', 'measureless object': 'appamāṇārammaṇā', 'object': 'ārammaṇā',
                      'things': 'dhamme'})
M['2-782'] = J(FORM, {'cause': 'hetukā', 'noble': 'Ariya', 'object': 'ārammaṇā', 'path': 'maggaṃ', 'paths': 'maggesu',
                      'paths is wisdom': 'maggesu paññā'})
M['2-783'] = J(FORM, {'dominant': 'adhipatiṃ', 'dominant factor': 'adhipatiṃ', 'factor': 'adhipatiṃ', 'noble': 'Ariya',
                      'path': 'maggaṃ'})
M['2-784'] = J(FUNC, {'arise': 'uppādinī', 'arisen': 'uppannā', 'describable': 'vattabbā', 'due to arise': 'uppādinī',
                      'unarisen': 'anuppannā'})
M['2-785'] = {'wisdom': 'paññā'}
M['2-786'] = J(FORM, {'object': 'ārammaṇā', 'past object': 'atītārammaṇā', 'things': 'dhamme'})
M['2-787'] = J(FORM, {'future object': 'anāgatārammaṇā', 'object': 'ārammaṇā', 'things': 'dhamme'})
M['2-788'] = J(FORM, {'object': 'ārammaṇā', 'present object': 'paccuppannārammaṇā', 'things': 'dhamme'})
M['2-789'] = {'external': 'bahiddhā', 'internal': 'ajjhattā', 'internal and external': 'ajjhattabahiddhā', 'wisdom': 'paññā'}
M['2-790'] = J(FORM, {'internal': 'Ajjhatte', 'internal object': 'ajjhattārammaṇā', 'internal things': 'Ajjhatte dhamme',
                      'object': 'ārammaṇā', 'things': 'dhamme'})
M['2-791'] = J(FORM, {'external': 'Bahiddhā', 'external object': 'bahiddhārammaṇā', 'external things': 'Bahiddhādhamme',
                      'object': 'ārammaṇā', 'things': 'dhamme'})
M['2-792'] = J(FORM, GROUND, {'external': 'bahiddhā', 'external object': 'bahiddhārammaṇā', 'internal': 'Ajjhatta',
                              'internal and external': 'Ajjhattabahiddhā', 'object': 'ārammaṇā', 'things': 'dhamme',
                              'threes': 'Tikaṃ'})
M['2-16-11-4-0'] = {'exposition': 'niddeso', 'fours': 'Catukka'}
M['2-793'] = J(FORM, {
 'acceptance': 'khanti', 'actions': 'kammānaṃ', 'ascetics': 'samaṇa', 'aside': 'Ṭhapetvā', 'badly-done': 'dukkaṭānaṃ',
 'beings': 'sattā', 'brahmins': 'brāhmaṇā', 'conduct': 'sammaggatā', 'conforming': 'anulomikā',
 'conformity': 'ānulomikaṃ', 'consciousness': 'viññāṇaṃ', 'consideration': 'pekkhā', 'declare': 'pavedentī',
 'direct': 'abhiññā', 'direct knowledge': 'abhiññā', 'endowed': 'samaṅgissa', 'father': 'pitā', 'feeling': 'vedanā',
 'form': 'Rūpaṃ', 'formations': 'saṅkhārā', 'fruit': 'phalaṃ', 'fruits': 'phalesu', 'having': NDE,
 'impermanent': 'anicca', 'kind': 'evarūpā', 'knowledge': 'ñāṇaṃ', 'material': 'Rūpaṃ', 'material form': 'Rūpaṃ',
 'mental': 'sāsavā', 'mental taints': 'sāsavā', 'mother': 'mātā', 'path': 'magga', 'paths': 'maggesu',
 'perception': 'saññā', 'practice': 'paṭipannā', 'preference': 'ruci', 'realised': 'sacchikatvā',
 'reborn': 'opapātikā', 'reflection': 'nijjhāna', 'sacrificed': 'hutaṃ', 'setting': 'Ṭhapetvā',
 'spontaneously': 'opapātikā', 'spontaneously reborn': 'opapātikā', 'subject to mental': 'sāsavā',
 'taints': 'sāsavā', 'themselves': 'sayaṃ', 'truths': 'saccānulomikaṃ', 'well-done': 'sukata', 'whatever': 'yā',
 'wholesome': 'kusalā', 'wholesome wisdom': 'kusalā paññā'})
M['2-794'] = J(FORM, {
 'cessation': 'nirodhe', 'cessation of suffering': 'dukkhanirodhe', 'endowed': 'samaṅgissa', 'knowledge': 'ñāṇaṃ',
 'origin': 'samudaye', 'origin of suffering': 'dukkhasamudaye', 'path': 'Magga', 'suffering': 'dukkhe'})
M['2-795'] = {
 'fine-material': 'rūpāvacarā', 'fine-material sphere': 'rūpāvacarā', 'fruits': 'phalesu',
 'fruits is wisdom': 'phalesu paññā', 'immaterial': 'arūpāvacarā', 'immaterial sphere': 'arūpāvacarā',
 'neutral': 'ābyākate', 'paths': 'maggesu', 'sense': 'kāmāvacarā', 'sense sphere': 'kāmāvacarā', 'sphere': 'āvacarā',
 'sphere is wisdom': 'Kāmāvacarakusalābyākate paññā', 'wholesome': 'kusalābyākate',
 'wholesome and neutral': 'kusalābyākate', 'wisdom': 'paññā', 'wisdom not included': 'apariyāpannā paññā',
}
M['2-796'] = J(FORM, {
 'ascetics': 'samaṇā', 'aside': 'ṭhapetvā', 'beings': 'sattānaṃ', 'brahmins': 'brāhmaṇā', 'cessation': 'nirodhaṃ',
 'cessation of suffering': 'dukkhanirodhaṃ', 'concentrated': 'samāhitaṃ', 'concentrated mind': 'samāhitaṃ citta',
 'contracted': 'saṃkhittaṃ', 'contracted mind': 'saṃkhittaṃ citta', 'conventional': 'sammuti', 'delusion': 'samohaṃ',
 'directly': 'abbhaññaṃsu', 'directly knew': 'abbhaññaṃsu', 'directly knew suffering': 'dukkhaṃ abbhaññaṃsu',
 'distracted': 'vikkhittaṃ', 'distracted mind': 'vikkhittaṃ citta', 'draws': 'neti', 'encompassed': 'paricca',
 'encompassing': 'pariye', "encompassing others' minds": 'pariye', 'expanded': 'mahaggataṃ',
 'expanded mind': 'mahaggataṃ citta', 'fathomed': 'pariyogāḷhena', 'freed': 'vimuttaṃ', 'freed mind': 'vimuttaṃ citta',
 'fruits': 'phalesu', 'hate': 'sadosaṃ', 'having': NDE, 'inference': 'nayaṃ', 'inferential': 'anvaye',
 'inferential knowledge': 'anvaye ñāṇaṃ', 'knew': 'abbhaññaṃsu', 'know': 'abhijānissanti', 'knowledge': 'ñāṇaṃ',
 'knowledge of encompassing': 'pariye ñāṇaṃ', 'known': 'ñātena', 'knows': 'pajānāti', 'lust': 'sarāgaṃ',
 'mind': 'cittaṃ', 'mind with delusion': 'samohaṃ citta', 'mind with hate': 'sadosaṃ citta',
 'mind with lust': 'sarāgaṃ citta', 'mind without delusion': 'vītamohaṃ citta',
 'mind without hate': 'vītadosaṃ citta', 'mind without lust': 'vītarāgaṃ citta', 'minds': 'ceto', 'monk': 'bhikkhu',
 'origin': 'samudayaṃ', 'origin of suffering': 'dukkhasamudayaṃ', 'others': 'pariye', "others' minds": 'pariye',
 'paths': 'maggesu', 'persons': 'puggalānaṃ', 'remaining': 'avasesā', 'remaining wisdom': 'avasesā paññā',
 'setting': 'ṭhapetvā', 'suffering': 'dukkhaṃ', 'suffering they directly': 'dukkhaṃ abbhaññaṃsu',
 'surpassable': 'sauttaraṃ', 'surpassable mind': 'sauttaraṃ citta', 'teaching': 'dhamme',
 'unconcentrated': 'asamāhitaṃ', 'unconcentrated mind': 'asamāhitaṃ citta', 'understood': 'viditena',
 'unexpanded': 'amahaggataṃ', 'unexpanded mind': 'amahaggataṃ citta', 'unfreed': 'avimuttaṃ',
 'unfreed mind': 'avimuttaṃ citta', 'unsurpassable': 'anuttaraṃ', 'unsurpassable mind': 'anuttaraṃ citta',
 'whatever': 'Ye hi keci', 'concerning': NDE})
M['2-797'] = {
 'accumulation': 'ācayāya', 'dismantling': 'apacayāya', 'fine-material': 'rūpāvacarārūpāvacarakusale',
 'immaterial': 'ārūpāvacara', 'paths': 'maggesu', 'remaining': 'avasesā', 'remaining wisdom': 'avasesā paññā',
 'sense': 'Kāmāvacara', 'sense sphere': 'Kāmāvacara', 'sphere': 'āvacara', 'spheres': 'āvacara', 'therein': 'tattha',
 'wholesome': 'kusale', 'wisdom': 'paññā', 'wisdom for accumulation': 'paññā ācayāya',
}
M['2-798'] = {
 'becomes': 'hoti', 'direct': 'abhiññāyo', 'direct knowledges': 'abhiññāyo', 'disenchantment': 'nibbidāya',
 'dispassionate': 'vītarāgo', 'knowledges': 'abhiññāyo', 'paths': 'maggesu', 'penetrate': 'paṭivijjhati',
 'penetrates': 'paṭivijjhati', 'penetration': 'paṭivedhāya', 'pleasures': 'kāmesu', 'remaining': 'avasesā',
 'remaining wisdom': 'avasesā paññā', 'sense': 'kāmesu', 'sense pleasures': 'kāmesu', 'therein': 'tattha',
 'towards': NDE, 'truths': 'saccāni', 'wisdom': 'paññā', 'wisdom for disenchantment': 'paññā nibbidāya',
}
M['2-799'] = {
 'absence': 'avitakka', 'absorption': 'jhānassa', 'accompanied': 'sahagatā',
 'accompanied by disenchantment': 'nibbidāsahagatā', 'accompanied by equanimity': 'upekkhāsahagatā',
 'accompanied by joy': 'pītisukhasahagatā', 'attentions': 'manasikārā',
 'attentions accompanied': 'kāmasahagatā saññāmanasikārā', 'beset': 'samudācaranti', 'breaking': 'nibbedha',
 'conformity': 'anudhammatā', 'connected': 'ūpasañhitā', 'connected with dispassion': 'virāgūpasañhitā',
 'consciousness': 'Viññāṇañcāyatanassa', 'disenchantment': 'nibbidā', 'dispassion': 'virāgūpasañhitā',
 'distinction': 'visesa', 'equanimity': 'upekkhā', 'field': 'āyatana', 'field of infinite': 'Ākāsānañcāyatanassa',
 'field of nothingness': 'Ākiñcaññāyatanassa', 'form': 'rūpa', 'fourth meditative': 'Catutthassa jhānassa',
 'fourth meditative absorption': 'Catutthassa jhānassa', 'gained': 'lābhiṃ', 'happiness': 'sukha',
 'infinite': 'ānañcāyatana', 'infinite consciousness': 'Viññāṇañcāyatanassa', 'infinite space': 'Ākāsānañcāyatanassa',
 'joy': 'pīti', 'Joy and happiness': 'pītisukha', 'material': 'rūpa', 'material form': 'rūpa',
 'meditative': 'jhānassa', 'meditative absorption': 'jhānassa', 'Meditative absorption': 'jhānassa',
 'mindfulness': 'sati', 'mindfulness in conformity': 'tadanudhammatā sati',
 'neither-pain-nor-pleasure': 'Adukkhamasukha',
 'neither-perception-nor-non-perception': 'Nevasaññānāsaññāyatanasahagatā', 'nothingness': 'Ākiñcaññāyatanassa',
 'perceptions': 'saññā', 'perceptions and attentions': 'saññāmanasikārā', 'pleasure': 'kāma', 'sense': 'kāma',
 'sense pleasure': 'kāma', 'shares in breaking': 'nibbedhabhāginī', 'shares in decline': 'hānabhāginī',
 'shares in distinction': 'visesabhāginī', 'shares in stability': 'ṭhitibhāginī', 'space': 'Ākāsānañcāyatanassa',
 'stability': 'ṭhiti', 'stands': 'santiṭṭhati', 'stands firm': 'santiṭṭhati',
 'state stands': 'tadanudhammatā sati santiṭṭhati', 'therein': 'tattha', 'thought': 'vitakka', 'wisdom': 'paññā',
 'wisdom that shares': 'ṭhitibhāginī paññā', 'Wisdom that shares': 'hānabhāginī paññā',
}
M['2-800'] = {
 'analytical': 'paṭisambhidā', 'analytical knowledge': 'paṭisambhidā', 'Analytical Knowledges': 'paṭisambhidā',
 'analytical knowledges': 'paṭisambhidā', 'expression': 'ābhilāpe', 'knowledge': 'ñāṇaṃ',
 'knowledge of language': 'niruttipaṭisambhidā', 'knowledge of meaning': 'atthapaṭisambhidā',
 'knowledge of principles': 'dhammapaṭisambhidā', 'knowledge of ready': 'paṭibhānapaṭisambhidā',
 'Knowledge with regard': 'ñāṇaṃ', 'knowledges': 'ñāṇesu', 'language': 'nirutti', 'meaning': 'Atthe',
 'principles': 'dhamme', 'ready': 'paṭibhāna', 'ready understanding': 'paṭibhāna', 'regard': NDE,
 'regard to knowledges': 'ñāṇesu', 'therein': 'Tattha', 'understanding': 'paṭibhāna',
}
M['2-801'] = J(FORM, {
 'concentration': 'samādhiṃ', 'difficult': 'dukkha', 'difficult practice': 'dukkhapaṭipadā', 'difficulty': 'kasirena',
 'direct': 'ābhiññā', 'direct knowledge': 'ābhiññā', 'easy': 'sukha', 'easy practice': 'sukhapaṭipadā',
 'knowing': 'abhijānantassa', 'knowledge': 'ābhiññā', 'modes': 'paṭipadā', 'practice': 'paṭipadā',
 'practice and quick': 'dukkhapaṭipadā khippābhiññā', 'practice and slow': 'dukkhapaṭipadā dandhābhiññā',
 'producing': 'uppādentassa', 'quick': 'khippābhiññā', 'quick direct': 'khippābhiññā',
 'quick direct knowledge': 'khippābhiññā', 'quickly': 'khippaṃ', 'slow': 'dandhābhiññā', 'slow direct': 'dandhābhiññā',
 'slow direct knowledge': 'dandhābhiññā', 'slowly': 'dandhaṃ', 'therein': 'tattha', 'trouble': 'Kicchena',
 'Wisdom of difficult': 'dukkhapaṭipadā dandhābhiññā paññā', 'wisdom of easy': 'sukhapaṭipadā dandhābhiññā paññā'})
M['2-802'] = J(FORM, {
 'aging': 'jarā', 'aging and death': 'jarāmaraṇe', 'cessation': 'nirodhe', 'cessation of aging': 'jarāmaraṇanirodhe',
 'concentration': 'Samādhissa', 'death': 'maraṇe', 'endowed': 'samaṅgissa', 'fully': 'nikāma', 'knowledge': 'ñāṇaṃ',
 'knowledge of aging': 'jarāmaraṇe ñāṇaṃ', 'limited': 'parittā', 'limited object': 'parittārammaṇā',
 'limited wisdom': 'parittā parittārammaṇā paññā', 'Limited wisdom': 'parittā parittārammaṇā paññā',
 'mastered': 'lābhissa', 'measureless': 'appamāṇā', 'measureless object': 'appamāṇārammaṇā',
 'measureless wisdom': 'appamāṇā appamāṇārammaṇā paññā', 'object': 'ārammaṇaṃ', 'objects': 'ārammaṇāni',
 'origin': 'samudaya', 'path': 'Magga', 'pervades': 'pharantassa', 'vast': 'vipulaṃ'})
M['2-803'] = J(FORM, GROUND, {
 'birth': 'jātiyā', 'cessation': 'nirodha', 'cessation of formations': 'saṅkhāranirodhaṃ', 'clinging': 'upādāne',
 'consciousness': 'viññāṇe', 'contact': 'phasse', 'craving': 'taṇhāya', 'endowed': 'samaṅgissa', 'existence': 'bhave',
 'feeling': 'vedanāya', 'form': 'rūpe', 'formations': 'Saṅkhāre', 'fours': 'Catukkaṃ', 'knowledge': 'ñāṇaṃ',
 'knowledge of consciousness': 'viññāṇepetaṃ ñāṇaṃ', 'knowledge of formations': 'saṅkhāresu ñāṇaṃ',
 'material': 'rūpe', 'material form': 'rūpe', 'mentality': 'nāma', 'mentality and material': 'nāmarūpe',
 'origin': 'samudaya', 'sense-fields': 'āyatane', 'teaching': 'Dhamma', 'therein': 'Tattha'})
M['2-16-11-5-0'] = {'exposition': 'niddeso', 'fives': 'Pañcaka'}
M['2-804'] = J(GROUND, {
 'absorptions': 'jhānesu', 'arises': 'uppajjati', 'attained': 'ādhigato', 'concentration': 'samādhi', 'divine': 'Dibba',
 'effort': 'sasaṅkhāra', 'emerge': 'vuṭṭhahāmī', 'emerged': 'vuṭṭhitassa', 'enter': 'samāpajjāmi', 'eye': 'cakkhu',
 'five-factored': 'pañcaṅgiko', 'five-knowledged': 'pañcañāṇiko', 'fives': 'Pañcakaṃ', 'forceful': 'niggayha',
 'happiness': 'sukha', 'joy': 'Pīti', 'knowledge': 'ñāṇaṃ', 'knowledge arises': 'ñāṇaṃ uppajjati', 'light': 'āloka',
 'maintained': 'sasaṅkhāraniggayhavāritagato', 'meditative': 'jhānesu', 'meditative absorptions': 'jhānesu',
 'mind': 'ceto', 'mindful': 'sato', 'minds': 'citte', 'noble': 'ariyo', 'obtained': 'laddho',
 'oneself': 'paccattaññeva', 'others': 'Paracitte', "others' minds": 'Paracitte', 'peaceful': 'santo',
 'people': 'akāpurisasevito', 'pervasion': 'pharaṇatā', 'pleasant': 'sukho', 'practised': 'sevito', 'refined': 'paṇīto',
 'reviewing': 'paccavekkhaṇā', 'reviewing knowledge': 'paccavekkhaṇāñāṇaṃ', 'right': 'sammā', 'sign': 'nimittaṃ',
 'suppression': 'vārita', 'therein': 'Tattha', 'tranquillisation': 'paṭippassaddha',
 'unification': 'ekodibhāvādhigato', 'unworldly': 'nirāmiso', 'wisdom': 'paññā'})
M['2-16-11-6-0'] = {'exposition': 'niddeso', 'sixes': 'Chakka'}
M['2-805'] = J(GROUND, {
 'away': 'cutūpapāte', 'beings': 'sattānaṃ', 'destruction': 'khaye', 'direct': 'abhiññāsu',
 'direct knowledges': 'abhiññāsu', 'ear': 'sota', 'ear element': 'sotadhātu', 'element': 'dhātu', 'kinds': 'vidhe',
 'knowledge': 'ñāṇaṃ', 'knowledges': 'abhiññāsu', 'lives': 'pubbenivāsānussatiyā', 'mental': 'āsavānaṃ',
 'mental taints': 'āsavānaṃ', 'minds': 'citte', 'others': 'paracitte', "others' minds": 'paracitte',
 'passing': 'cutūpapāte', 'past lives': 'pubbenivāsānussatiyā', 'power': 'Iddhi', 'purification': 'visuddhiyā',
 'rebirth': 'ūpapāte', 'recollection': 'ānussatiyā', 'sixes': 'Chakkaṃ', 'supernormal': 'Iddhi', 'taints': 'āsavānaṃ',
 'therein': 'Tattha', 'wisdom': 'paññā'})
M['2-16-11-7-0'] = {'exposition': 'niddeso', 'sevens': 'Sattaka'}
M['2-806'] = J(GROUND, {
 'aging': 'jarā', 'aging and death': 'jarāmaraṇa', 'away': 'virāga', 'birth': 'jāti', 'birth as condition': 'jātipaccayā',
 'cessation': 'nirodha', 'clinging': 'upādāna', 'clinging as condition': 'upādānapaccayā', 'condition': 'paccayā',
 'consciousness': 'viññāṇa', 'consciousness as condition': 'viññāṇapaccayā', 'contact': 'phassa',
 'contact as condition': 'phassapaccayā', 'craving': 'taṇhā', 'craving as condition': 'taṇhāpaccayā', 'death': 'maraṇa',
 'destruction': 'khaya', 'existence': 'bhava', 'existence as condition': 'bhavapaccayā', 'fading': 'virāga',
 'feeling': 'vedanā', 'feeling as condition': 'vedanāpaccayā', 'fixity': 'ṭṭhiti', 'form': 'rūpa',
 'form as condition': 'nāmarūpapaccayā', 'formations': 'saṅkhārā', 'formations as condition': 'saṅkhārapaccayā',
 'grounds': 'vatthūni', 'ignorance': 'avijjā', 'ignorance as condition': 'avijjāpaccayā', 'itself': 'tampi',
 'knowledge': 'ñāṇaṃ', 'material': 'rūpa', 'material form': 'rūpa', 'mentality': 'nāma',
 'mentality and material': 'nāmarūpa', 'sense-fields': 'āyatana', 'sense-fields as condition': 'saḷāyatanapaccayā',
 'sevens': 'Sattakaṃ', 'seventy-seven': 'sattasattati', 'therein': 'Tattha', 'things': 'dhamma', 'vanishing': 'vaya'})
M['2-16-11-8-0'] = {'eights': 'Aṭṭhaka', 'exposition': 'niddeso'}
M['2-807'] = J(GROUND, {
 'arahantship': 'arahatta', 'eights': 'Aṭṭhakaṃ', 'fruit': 'phale', 'fruits': 'phalesu', 'non-returning': 'anāgāmi',
 'once-returning': 'sakadāgāmi', 'path': 'magge', 'paths': 'maggesu', 'stream-entry': 'Sotāpatti', 'therein': 'Tattha',
 'wisdom': 'paññā'})
M['2-16-11-9-0'] = {'exposition': 'niddeso', 'nines': 'Navaka'}
M['2-808'] = J(GROUND, {
 'absorption': 'jhāna', 'attainment': 'samāpattiyā', 'attainments': 'samāpattīsu', 'cessation': 'nirodha',
 'consciousness': 'viññāṇañcāyatanasamāpattiyā', 'dwelling': 'vihāra', 'emerged': 'vuṭṭhitassa', 'feeling': 'vedayita',
 'field': 'āyatana', 'field of infinite': 'ākāsānañcāyatana', 'field of nothingness': 'ākiñcaññāyatanasamāpattiyā',
 'fourth meditative': 'catutthajjhāna', 'fourth meditative absorption': 'catutthajjhāna', 'infinite': 'ānañcāyatana',
 'infinite consciousness': 'viññāṇañcāyatanasamāpattiyā', 'infinite space': 'ākāsānañcāyatanasamāpattiyā',
 'meditative': 'jhāna', 'meditative absorption': 'jhāna', 'Meditative absorption': 'jhāna',
 'neither-perception-nor-non-perception': 'nevasaññānāsaññāyatanasamāpattiyā', 'nines': 'Navakaṃ',
 'nothingness': 'ākiñcaññāyatanasamāpattiyā', 'perception': 'saññā', 'reviewing': 'paccavekkhaṇā',
 'reviewing knowledge': 'paccavekkhaṇāñāṇaṃ', 'space': 'ākāsānañcāyatanasamāpattiyā', 'successive': 'anupubba',
 'therein': 'Tattha', 'wisdom': 'paññā'})
M['2-16-11-10-0'] = {'exposition': 'niddeso', 'tens': 'Dasaka'}
TEN = J(FORM, {'knowledge': 'ñāṇaṃ', 'knows': 'pajānāti', 'really': 'yathābhūtaṃ', 'therein': 'Tattha'})
CONDUCT = {
 'bodily': 'kāya', 'Bodily misconduct': 'kāyaduccarita', 'bodily misconduct': 'kāyaduccarita',
 'bodily conduct': 'kāyasucarita', 'good bodily': 'kāyasucarita', 'good bodily conduct': 'kāyasucarita',
 'verbal': 'vacī', 'verbal conduct': 'vacīsucarita', 'good verbal': 'vacīsucarita', 'good verbal conduct': 'vacīsucarita',
 'verbal misconduct': 'vacīduccarita', 'mental': 'mano', 'mental conduct': 'manosucarita',
 'good mental': 'manosucarita', 'good mental conduct': 'manosucarita', 'mental misconduct': 'manoduccarita',
 'misconduct': 'duccarita', 'conduct': 'sucarita', 'body': 'kāyassa', 'body after death': 'kāyassa bhedā paraṃ maraṇā',
 'breakup': 'bhedā', 'death': 'maraṇā', 'bad': 'duggatiṃ', 'bad destination': 'duggatiṃ', 'destination': 'gatiṃ',
 'good destination': 'sugatiṃ', 'heavenly': 'saggaṃ', 'heavenly world': 'saggaṃ lokaṃ', 'hell': 'nirayaṃ',
 'place': 'vinipātaṃ', 'ruin': 'vinipātaṃ',
}
M['2-809'] = J(TEN, CONDUCT, {
 'accomplished': 'sampanno', 'accomplished in view': 'diṭṭhisampanno', 'accordingly': 'upādāya',
 'acknowledge': 'uddiseyya', 'agreeable': 'manāpo', 'agreeable result': 'manāpo vipāko', 'arahant': 'arahaṃ',
 'arahants': 'arahanto', 'arise': 'uppajjeyyuṃ', 'awakened': 'sambuddho', 'Awakened Buddha': 'sammāsambuddho',
 'awakened Buddha': 'sammāsambuddho', 'blood': 'lohitaṃ', 'buddha': 'sammāsambuddho', 'buddhas': 'sammāsambuddhā',
 'cannot': 'anavakāso', 'causes': 'hetū', 'deprive': 'voropeyya', 'desired': 'kanto', 'disagreeable': 'amanāpo',
 'disagreeable result': 'amanāpo vipāko', 'eighth': 'aṭṭhamaṃ', 'exercise': 'kareyya', 'existence': 'bhavaṃ',
 'father': 'pitaraṃ', 'formation': 'saṅkhāraṃ', 'fully': 'sammā', 'Fully Awakened': 'sammāsambuddho',
 'Fully Awakened Buddha': 'sammāsambuddho', 'fully awakened Buddha': 'sammāsambuddho', 'happen': 'anavakāso',
 'hatred': 'paduṭṭhena', 'impossible': 'Aṭṭhānametaṃ', 'king': 'rājā', 'kings': 'rājāno', 'life': 'jīvitā',
 'man': 'puriso', 'mind': 'cittena', 'mother': 'mātaraṃ', 'order': 'saṅghaṃ', 'ordinary': 'puthujjano',
 'ordinary person': 'puthujjano', 'permanent': 'niccato', 'person': 'puggalo',
 'person accomplished': 'diṭṭhisampanno puggalo', 'pleasant': 'sukhato', 'produce': 'nibbatteyya',
 'reborn': 'upapajjeyya', 'rulership': 'sakkattaṃ', 'sakka': 'sakkattaṃ', 'self': 'atthato', 'shed': 'uppādeyya',
 'teacher': 'satthāraṃ', 'thing': 'dhammaṃ', 'undesired': 'akanto', 'unwished-for': 'aniṭṭho',
 'whatever': 'Ye ye', 'wheel-turning': 'cakkavattī', 'wished-for': 'iṭṭho', 'woman': 'itthī',
 'world system': 'lokadhātuyā'})
M['2-810'] = J(TEN, {
 'action which ripen': 'kammasamādānāni / vipaccanti', 'blocked': 'paṭibāḷhāni', 'body': 'upadhi', 'cause': 'hetuso',
 'circumstance': 'ṭhānaso', 'destination': 'gati', 'effort': 'payoga', 'evil': 'pāpakāni',
 'evil undertakings': 'pāpakāni kammasamādānāni', 'fortunate': 'sampatti',
 'good undertakings': 'kalyāṇāni kammasamādānāni', 'ripen': 'vipaccanti', 'undertakings': 'samādānāni',
 'undertakings of action': 'kammasamādānāni', 'unfortunate': 'vipattiṃ'})
M['2-811'] = J(TEN, {
 'animal': 'tiracchāna', 'everywhere': 'sabbattha', 'ghosts': 'petti', 'gods': 'deva', 'hell': 'niraya',
 'human': 'manussa', 'leads': 'gāmī', 'path': 'maggo', 'realm': 'visaya', 'womb': 'yoni'})
M['2-812'] = J(TEN, {'aggregates': 'khandha', 'different': 'nānā', 'diversity': 'nānattaṃ', 'elements': 'dhātu',
                     'sense-fields': 'āyatana'})
INCL = {
 'attend': 'payirupāsanti', 'attended': 'payirupāsiṃsu', 'beings': 'sattānaṃ', 'frequent': 'bhajanti',
 'frequented': 'bhajiṃsu', 'inclination': 'ādhimuttikā', 'inclination resort': 'ādhimuttikā / sevanti',
 'inclination resorted': 'ādhimuttikā / seviṃsu', 'inclination will resort': 'ādhimuttikā / sevissanti',
 'inferior': 'hīnādhimuttikā', 'inferior inclination': 'hīnādhimuttikā',
 'inferior inclination resort': 'hīnādhimuttikā / sevanti', 'inferior inclination resorted': 'hīnādhimuttikā / seviṃsu',
 'refined': 'paṇītādhimuttikā', 'refined inclination': 'paṇītādhimuttikā',
 'refined inclination resort': 'paṇītādhimuttikā / sevanti',
 'refined inclination resorted': 'paṇītādhimuttikā / seviṃsu', 'resort': 'sevanti', 'resorted': 'seviṃsu',
}
M['2-813'] = J(TEN, INCL, {'different': 'nānā', 'inclinations': 'ādhimuttikataṃ'})
M['2-814'] = {
 'bad': 'dvākāre', 'bad character': 'dvākāre', 'beings': 'sattānaṃ', 'capable': 'bhabbābhabbe', 'character': 'ākāre',
 'conduct': 'caritaṃ', 'disposition': 'āsayaṃ', 'dull': 'mudindriye', 'dull faculties': 'mudindriye',
 'dust': 'rajakkhe', 'easy': 'suviññāpaye', 'eyes': 'akkhe', 'faculties': 'indriye', 'good character': 'svākāre',
 'hard': 'duviññāpaye', 'incapable': 'ābhabbe', 'inclination': 'adhimuttiṃ', 'instruct': 'viññāpaye',
 'knowledge': 'ñāṇaṃ', 'knows': 'pajānāti', 'persons': 'parapuggalānaṃ', 'really': 'yathābhūtaṃ',
 'sharp': 'tikkhindriye', 'sharp faculties': 'tikkhindriye', 'tendencies': 'anusayaṃ', 'therein': 'Tattha',
 'underlying': 'anusayaṃ', 'underlying tendencies': 'anusayaṃ',
}
M['2-815'] = {
 'acceptance': 'khanti', 'arisen': 'samuppannesu', 'avoiding': 'anupagamma', 'beings': 'sattā', 'body': 'sarīra',
 'conditionality': 'paccayatā', 'conforming': 'anulomikā', 'death': 'maraṇā', 'dependently': 'paṭicca',
 'disposition': 'āsayo', 'eternal': 'Sassato', 'exist': 'hoti', 'exist after death': 'hoti tathāgato paraṃ maraṇā',
 'existence': 'bhava', 'exists': 'hoti', 'extremes': 'ante', 'finite': 'antavā', 'gained': 'paṭiladdhā',
 'infinite': 'anantavā', 'knowledge': 'ñāṇaṃ', 'non-existence': 'vibhava', 'really': 'yathābhūtaṃ', 'regard': NDE,
 'rely': 'sannissitā', 'soul': 'jīvaṃ', 'specific': 'idappaccayatā', 'Tathāgata exists': 'hoti tathāgato',
 'thing': 'aññaṃ', 'things': 'dhammesu', 'view': 'diṭṭhi', 'view of existence': 'bhavadiṭṭhi',
 'view of non-existence': 'vibhavadiṭṭhi',
}
M['2-816'] = {
 'agreeable': 'sātarūpaṃ', 'aversion': 'paṭighānusayo', 'beings': 'sattānaṃ', 'conceit': 'māno', 'dear': 'piyarūpaṃ',
 'disagreeable': 'appiyarūpaṃ', 'doubt': 'vicikicchā', 'existence': 'bhava', 'fallen': 'ānupatitā', 'form': 'rūpaṃ',
 'ignorance': 'avijjā', 'latent': 'anuseti', 'lies': 'anuseti', 'lust': 'rāgānusayo', 'sensual': 'kāma',
 'standing': 'ekaṭṭho', 'tendencies': 'ānusayā', 'tendency': 'anusayo', 'things': 'dhammesu', 'together': 'Tadekaṭṭho',
 'underlying': 'anusayo', 'underlying tendencies': 'ānusayā', 'underlying tendency': 'anusayo',
 'unpleasant': 'asātarūpaṃ', 'views': 'diṭṭhi', 'whatever': 'Yaṃ',
}
M['2-817'] = {
 'beings': 'sattānaṃ', 'conduct': 'caritaṃ', 'demeritorious': 'apuññābhisaṅkhāro',
 'demeritorious formation': 'apuññābhisaṅkhāro', 'formation': 'ābhisaṅkhāro', 'imperturbable': 'āneñjābhisaṅkhāro',
 'imperturbable formation': 'āneñjābhisaṅkhāro', 'limited': 'paritta', 'meritorious': 'Puññābhisaṅkhāro',
 'meritorious formation': 'Puññābhisaṅkhāro', 'plane': 'bhūmako',
}
M['2-818'] = J(INCL, {'inclination': 'adhimutti'})
GROUNDS10 = {'beings': 'sattā', 'defilement': 'kilesa', 'grounds': 'vatthūni', 'grounds of defilement': 'kilesavatthūni',
             'dust': 'rajakkhā', 'eyes': 'akkhā', 'cultivated': 'bahulīkatāni', 'developed': 'bhāvitāni',
             'practised': 'āsevitāni', 'heaped': 'ussadagatāni'}
M['2-819'] = J(GROUNDS10, {
 'conceit': 'māno', 'delusion': 'moho', 'doubt': 'vicikicchā', 'dread': 'anottappaṃ', 'dullness': 'thinaṃ',
 'greed': 'lobho', 'hate': 'doso', 'lack': 'anottappaṃ', 'Lack of moral': 'anottappaṃ', 'lack of moral': 'anottappaṃ',
 'moral': 'anottappaṃ', 'restlessness': 'uddhaccaṃ', 'shamelessness': 'ahirikaṃ', 'ten': 'Dasa',
 'ten grounds': 'Dasa kilesavatthūni', 'views': 'diṭṭhi'})
NEG = {'cultivated': 'abahulīkatāni', 'developed': 'abhāvitāni', 'practised': 'anāsevitāni', 'heaped': 'anussadagatāni'}
M['2-820'] = J(GROUNDS10, NEG, {'ten': 'dasa', 'ten grounds': 'dasa kilesavatthūni'})
M['2-821'] = J(GROUNDS10, NEG, {
 'concentration': 'samādhindriyaṃ', 'confidence': 'saddhindriyaṃ', 'dull': 'mudindriyā', 'dull faculties': 'mudindriyā',
 'faculties': 'indriyāni', 'faculty': 'indriyaṃ', 'faculty of concentration': 'samādhindriyaṃ',
 'faculty of confidence': 'saddhindriyaṃ', 'faculty of energy': 'vīriyindriyaṃ', 'faculty of mindfulness': 'satindriyaṃ',
 'faculty of wisdom': 'paññindriyaṃ', 'mindfulness': 'satindriyaṃ', 'wisdom': 'paññindriyaṃ'})
M['2-822'] = J(GROUNDS10, {'faculties': 'indriyāni', 'sharp': 'tikkhindriyā', 'sharp faculties': 'tikkhindriyā'})
M['2-823'] = {
 'bad': 'dvākārā', 'bad character': 'dvākārā', 'beings': 'sattā', 'character': 'ākārā', 'conduct': 'caritā',
 'dispositions': 'āsayā', 'dull': 'mudindriyā', 'dull faculties': 'mudindriyā', 'dust': 'rajakkhā', 'evil': 'pāpa',
 'eyes': 'akkhā', 'faculties': 'indriyā', 'inclinations': 'ādhimuttikā', 'tendencies': 'ānusayā',
 'underlying': 'ānusayā', 'underlying tendencies': 'ānusayā',
}
M['2-824'] = {
 'beings': 'sattā', 'character': 'ākārā', 'conduct': 'caritā', 'dispositions': 'āsayā', 'dust': 'rajakkhā',
 'eyes': 'akkhā', 'faculties': 'indriyā', 'good character': 'svākārā', 'good conduct': 'kalyāṇacaritā',
 'good inclinations': 'kalyāṇādhimuttikā', 'inclinations': 'ādhimuttikā', 'sharp': 'tikkhindriyā',
 'sharp faculties': 'tikkhindriyā',
}
M['2-825'] = {'bad': 'dvākārā', 'bad character': 'dvākārā', 'beings': 'sattā', 'character': 'ākārā',
              'easy': 'suviññāpayā', 'good character': 'svākārā', 'hard': 'duviññāpayā', 'instruct': 'viññāpayā'}
OBSTR = {
 'beings': 'sattā', 'course': 'niyāmaṃ', 'defilement': 'kilesāvaraṇena', 'entering': 'okkamituṃ', 'fixed': 'niyāmaṃ',
 'obstruction': 'āvaraṇena', 'obstruction of action': 'kammāvaraṇena', 'possess': 'samannāgatā',
 'possess the obstruction': 'āvaraṇena samannāgatā', 'rightness': 'sammattaṃ', 'things': 'dhammesu',
 'wholesome': 'kusalesu', 'wholesome things': 'kusalesu dhammesu',
}
M['2-826'] = J(OBSTR, {'confidence': 'assaddhā', 'desire': 'acchandikā', 'incapable': 'abhabbā', 'wisdom': 'duppaññā'})
M['2-827'] = J(TEN, OBSTR, {'capable': 'bhabbā', 'confidence': 'saddhā', 'desire': 'chandikā', 'faculties': 'indriya',
                           'persons': 'parapuggalānaṃ', 'wisdom': 'paññā', 'therein': 'tattha'})
M['2-828'] = J(TEN, {
 'absorption': 'jhānaṃ', 'absorptions': 'jhānāni', 'attainment': 'samāpatti',
 'attainment within concentration': 'samādhismiṃ samāpatti', 'attainments': 'samāpattīnaṃ', 'attending': 'manasikārā',
 'attending': 'amanasikārā', 'aware': NDE, 'beautiful': 'Subhanteva', 'beyond': 'samatikkamma', 'cessation': 'nirodhaṃ', 'cleansing': 'Vodāna',
 'completely': 'Sabbaso', 'Completely passing': 'Sabbaso / samatikkamma',
 'completely passing': 'Sabbaso / samatikkamma', 'concentration': 'samādhi',
 'concentration within concentration': 'samādhismiṃ samādhi', 'concentrations': 'samādhī', 'consciousness': 'viññāṇa',
 'defilement': 'Saṃkilesa', 'disappearance': 'atthaṅgamā', 'distinction': 'visesa', 'diversity': 'nānatta',
 'dwelling': 'vihāra', 'dwells': 'viharati', 'eighth': 'aṭṭhamo', 'emergence': 'Vuṭṭhāna', 'emerges': 'vuṭṭhāti',
 'emerging': 'vuṭṭhānampi', 'enters': 'upasampajja', 'enters and dwells': 'upasampajja viharati',
 'enters quickly': 'khippaṃ samāpajjati', 'enters slowly': 'dandhaṃ samāpajjati', 'examination': 'vicāro',
 'externally': 'bahiddhā', 'failure': 'vipatti', 'feeling': 'vedayita', 'field': 'āyatanaṃ',
 'field of infinite': 'ākāsānañcāyatanaṃ', 'field of nothingness': 'ākiñcaññāyatanaṃ', 'fifth': 'pañcamo',
 'form': 'rūpa', 'forms': 'rūpāni', 'fourth meditative': 'catutthaṃ jhānaṃ',
 'fourth meditative absorption': 'catutthaṃ jhānaṃ', 'infinite': 'ananto', 'infinite consciousness': 'viññāṇañcāyatanaṃ',
 'infinite space': 'ākāsānañcāyatanaṃ', 'internally': 'Ajjhattaṃ', 'liberation': 'vimokkho', 'liberations': 'vimokkhā',
 'material': 'rūpa', 'material form': 'rūpa', 'meditative': 'jhāna', 'Meditative absorption': 'jhānaṃ',
 'meditative absorption': 'jhānaṃ', 'meditative absorptions': 'jhānāni', 'meditator': 'jhāyī',
 'meditator who enters': 'jhāyī / samāpajjati', 'meditators': 'jhāyī',
 'neither-perception-nor-non-perception': 'nevasaññānāsaññāyatanaṃ', 'nothing': 'natthi kiñci',
 'nothingness': 'ākiñcaññāyatanaṃ', 'passing': 'samatikkamma', 'perceiving': 'saññī', 'perception': 'saññā',
 'perceptions': 'saññānaṃ', 'perceptions of diversity': 'nānattasaññānaṃ', 'perceptions of material': 'rūpasaññānaṃ',
 'perceptions of resistance': 'paṭighasaññānaṃ', 'possessing': 'Rūpī', 'quickly': 'khippaṃ', 'resistance': 'paṭigha',
 'resolved': 'adhimutto', 'seventh': 'sattamo', 'shares in decline': 'hānabhāgiyo',
 'shares in distinction': 'visesabhāgiyo', 'sixth': 'chaṭṭho', 'skilled': 'kusalo', 'slowly': 'dandhaṃ',
 'space': 'ākāso', 'success': 'sampatti', 'successive': 'anupubba', 'takes': 'pacceti', 'thought': 'vitakka',
 'truly': 'samānaṃ'})
M['2-829'] = J(TEN, {
 'appearance': 'vaṇṇo', 'arose': 'udapādiṃ', 'aspects': 'sākāraṃ', 'away': 'cuto', 'birth': 'jātiṃ', 'births': 'jātiyo',
 'clan': 'gotto', 'elsewhere': 'amutra', 'eons': 'kappe', 'expansion': 'vivaṭṭa', 'experiencing': 'paṭisaṃvedī',
 'fifty': 'paññāsampi', 'food': 'āhāro', 'forty': 'cattālīsampi', 'happiness': 'sukha', 'hundred': 'satampi',
 'life': 'āyu', 'lives': 'pubbenivāsaṃ', 'manifold': 'anekavihitaṃ', 'named': 'nāmo', 'pain': 'dukkha',
 'passing': 'cuto', 'past lives': 'pubbenivāsaṃ', 'reborn': 'ūpapanno', 'recollection': 'ānussati',
 'recollects': 'anussarati', 'span': 'pariyanto', 'Tathāgata recollects': 'tathāgato / anussarati', 'ten': 'dasapi',
 'ten births': 'dasapi jātiyo', 'thirty': 'tiṃsampi', 'thousand': 'sahassampi', 'twenty': 'vīsampi',
 'world-contraction': 'saṃvaṭṭa', 'world-expansion': 'vivaṭṭa'})
M['2-830'] = J(TEN, CONDUCT, {
 'actions': 'yathākammūpage', 'away': 'cavamāne', 'beautiful': 'suvaṇṇe', 'beings': 'sattā', 'bodily conduct': 'kāyasucaritena',
 'divine': 'dibbena', 'endowed': 'samannāgatā', 'eye': 'cakkhunā', 'faring': 'ūpage', 'fortunate': 'sugate',
 'human': 'mānusakena', 'indeed': 'vata', 'inferior': 'hīne', 'noble': 'ariyānaṃ', 'ones': NDE, 'passing': 'cavamāne',
 'purified': 'visuddhena', 'rebirth': 'ūpapātaṃ', 'reborn': 'upapannā', 'refined': 'paṇīte', 'revilers': 'upavādakā',
 'surpassing': 'atikkanta', 'ugly': 'dubbaṇṇe', 'undertaking': 'samādānā', 'unfortunate': 'duggate', 'wrong': 'micchā',
 'wrong view': 'micchādiṭṭhikā', 'Wrong view': 'micchādiṭṭhikā',
 # instrumental forms in this segment
 'Bodily misconduct': 'kāyaduccaritena', 'bodily misconduct': 'kāyaduccaritena', 'good bodily': 'kāyasucaritena',
 'good bodily conduct': 'kāyasucaritena', 'verbal conduct': 'vacīsucaritena', 'good verbal': 'vacīsucaritena',
 'good verbal conduct': 'vacīsucaritena', 'verbal misconduct': 'vacīduccaritena', 'mental conduct': 'manosucaritena',
 'good mental': 'manosucaritena', 'good mental conduct': 'manosucaritena', 'mental misconduct': 'manoduccaritena',
 'misconduct': 'duccaritena', 'conduct': 'sucaritena'})
M['2-831'] = J(TEN, {
 'analysis': 'vibhaṅgo', 'destruction': 'khayaṃ', 'direct': 'abhiññā', 'direct knowledge': 'abhiññā',
 'dwells': 'viharatī', 'enters': 'upasampajja', 'enters and dwells': 'upasampajja viharatī', 'finished': 'niṭṭhito',
 'having': NDE, 'himself': 'sayaṃ', 'liberation': 'vimuttiṃ', 'liberation of mind': 'cetovimuttiṃ',
 'life': 'diṭṭheva dhamme', 'mental': 'āsavānaṃ', 'mental taints': 'āsavānaṃ', 'mind': 'ceto', 'realised': 'sacchikatvā',
 'taintless': 'anāsavaṃ', 'taints': 'āsavānaṃ', 'tens': 'Dasakaṃ'})

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
