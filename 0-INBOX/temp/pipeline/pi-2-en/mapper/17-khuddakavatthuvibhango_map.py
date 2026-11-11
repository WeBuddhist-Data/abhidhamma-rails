import pathlib
d = pathlib.Path(__file__).parent
ch = '17-khuddakavatthuvibhango'
NDE = '(no direct equivalent)'


def mg(*ds, **kw):
    r = {}
    for x in ds:
        r.update(x)
    r.update(kw)
    return r


M = {}

# ---------------------------------------------------------------- matrix (mātikā)
M['2-17-0'] = {'analysis': 'vibhaṅgo', 'minor': 'Khuddaka', 'topics': 'vatthu'}
M['2-17-1-0'] = {'matrix': 'mātikā', 'ones': 'Ekaka'}
M['2-832'] = {
 'absorption': 'jhāna', 'affectation': 'siṅgaṃ', 'alms-goer': 'piṇḍapātika', 'beauty': 'vaṇṇa', 'behaviour': 'vutti',
 'belittling': 'nippesikatā', 'beyond': 'ātimāno', 'birth': 'Jāti', 'build': 'pariṇāha', 'chasing': 'nijigīsanatā',
 'Chasing gain': 'lābhaṃ nijigīsanatā', 'clan': 'gotta', 'completeness': 'pāripūri', 'conceit': 'māno',
 'Conceit beyond conceit': 'mānātimāno', 'connected': 'paṭisaṃyutto', 'contentiousness': 'sārambho', 'craft': 'sippa',
 'deportment': 'iriyāpatha', 'desire': 'icchatā', 'despised': 'anavaññāta', 'discontent': 'arati',
 'discordant': 'asabhāga', 'drowsiness': 'sammado', 'dying': 'amara', 'equal': 'sadisassa', 'evil': 'pāpicchatā',
 'evil desire': 'pāpicchatā', 'exaggerated': 'atimāno', 'Exaggerated conceit': 'atimāno', 'excessive': 'atricchatā',
 'excessive desire': 'atricchatā', 'fame': 'yasa', 'figure': 'saṇṭhāna', 'frivolity': 'cāpalyaṃ',
 'great desire': 'mahicchatā', 'Great desire': 'mahicchatā', 'greediness': 'tintiṇaṃ', 'health': 'ārogya',
 'heedlessness': 'pamādo', 'height': 'āroha', 'hinting': 'nemittikatā', 'home': 'janapada', 'honour': 'sakkāra',
 'intoxication': 'mado', 'Intoxication with birth': 'Jātimado', 'intoxication with clan': 'gottamado',
 'intoxication with completeness': 'pāripūrimado', 'learning': 'suta', 'life': 'jīvita', 'meals': 'bhatta',
 'meditative': 'jhāna', 'Meditative absorption': 'jhāna', 'meditative absorption': 'jhāna', 'mind': 'cetaso',
 'obstinacy': 'thambho', 'ones': 'Ekakaṃ', 'oneself': NDE, 'others': 'parānuddayatāpaṭisaṃyutto',
 'over-estimating': 'adhimāno', 'Over-estimating conceit': 'adhimāno', 'quick': 'paṭibhāna',
 'quick understanding': 'paṭibhāna', 'relatives': 'ñāti', 'renown': 'siloka', 'respect': 'garukāra',
 'self-belittling': 'omāno', 'Self-belittling conceit': 'omāno', 'seniority': 'rattaññu', 'sloth': 'tandī',
 'sluggishness': 'līnattaṃ', 'Sluggishness of mind': 'cetaso ca līnattaṃ', 'stretching': 'vijambhitā',
 'Stretching oneself': 'vijambhitā', 'success': 'iddhi', 'sympathy': 'ānuddayatā', 'talk': 'lapanā',
 'thought': 'vitakko', 'thought connected': 'paṭisaṃyutto vitakko', 'Thought connected': 'paṭisaṃyutto vitakko',
 'thoughts': 'vitakko', 'trickery': 'kuhanā', 'understanding': 'paṭibhāna', 'virtue': 'sīla', 'wealth': 'bhoga',
 'wheedling': 'lapanā', 'worse': 'hīnassa', 'wrong': 'micchāmāno', 'Wrong conceit': 'micchāmāno', 'youth': 'yobbana'}
M['2-17-1-1-0'] = {'matrix': 'mātikā', 'twos': 'Duka'}
M['2-833'] = {
 'anger': 'Kodho', 'annihilationist': 'uccheda', 'annihilationist view': 'ucchedadiṭṭhi',
 'clear': 'asampajaññañca', 'clear comprehension': 'asampajaññañca', 'comprehension': 'asampajaññañca',
 'contempt': 'makkho', 'correct': 'dovacassatā', 'craving': 'taṇhā', 'craving for existence': 'bhavataṇhā',
 'crookedness': 'anajjavo', 'deceit': 'māyā', 'domineering': 'paḷāso', 'doors': 'aguttadvāratā',
 'dread': 'anottappañca', 'envy': 'issā', 'eternalist': 'sassata', 'eternalist view': 'sassatadiṭṭhi', 'evil': 'pāpa',
 'Evil friendship': 'pāpamittatā', 'evil friendship': 'pāpamittatā', 'existence': 'bhava', 'external': 'bahiddhā',
 'faculties': 'indriyesu', 'failure': 'vipatti', 'failure in view': 'diṭṭhivipatti', 'fetter': 'saṃyojanañca',
 'finite': 'antavā', 'food': 'bhojane', 'forgetfulness': 'muṭṭhassaccañca', 'friendship': 'mittatā',
 'guarding': 'aguttadvāratā', 'guarding the doors': 'aguttadvāratā', 'hard': 'dovacassatā',
 'hard to correct': 'dovacassatā', 'harshness': 'amaddavo', 'hospitality': 'appaṭisanthāro', 'ignorance': 'avijjā',
 'immoderation': 'asoraccañca', 'impatience': 'akkhanti', 'infinite': 'anantavā', 'internal': 'ajjhatta',
 'knowing': 'amattaññutā', 'knowing moderation': 'amattaññutā', 'lack': 'anottappañca',
 'lack of clear': 'asampajaññañca', 'Lack of clear': 'asampajaññañca', 'lack of hospitality': 'appaṭisanthāro',
 'Lack of moral': 'anottappañca', 'lack of moral': 'anottappañca', 'moderation': 'amattaññutā',
 'moderation in food': 'bhojane amattaññutā', 'moral': 'anottappañca', 'non-existence': 'vibhava',
 'resentment': 'upanāho', 'rough': 'asākhalyañca', 'Rough speech': 'asākhalyañca', 'shamelessness': 'ahirikañca',
 'speculation': 'ānudiṭṭhi', 'speech': 'asākhalyañca', 'stinginess': 'macchariyañca', 'things': NDE,
 'treachery': 'sāṭheyyañca', 'twos': 'Dukaṃ', 'view': 'diṭṭhi', 'view of existence': 'bhavadiṭṭhi',
 'view of non-existence': 'vibhavadiṭṭhi', 'view that things': 'antavādiṭṭhi', 'virtue': 'sīla'}
M['2-17-1-2-0'] = {'matrix': 'mātikā', 'threes': 'Tika'}
M['2-834'] = {
 'attention': 'manasikāro', 'bad': 'dussīlyaṃ', 'bad conduct': 'dussīlyaṃ', 'blemishes': 'aṅgaṇāni',
 'clear': 'asampajaññatā', 'clear comprehension': 'asampajaññatā', 'comprehension': 'asampajaññatā',
 'conduct': 'cariyā', 'confidence': 'assaddhiyaṃ', 'correct': 'dovacassatā', 'corruptions': 'kasāvā',
 'cravings': 'taṇhā', 'cruelty': 'vihesā', 'darknesses': 'tamāni', 'desire': 'icchatā', 'discontent': 'arati',
 'discontentment': 'asantuṭṭhitā', 'disrespect': 'anādariyaṃ', 'distraction': 'vikkhepo',
 'Distraction of mind': 'cetaso vikkhepo', 'diversity': 'nānatta', 'dread': 'anottappaṃ', 'elements': 'dhātuyo',
 'enjoyment': 'assāda', 'evil': 'pāpa', 'Evil friendship': 'pāpamittatā', 'evil friendship': 'pāpamittatā',
 'fault-finding': 'upārambha', 'fault-finding mind': 'upārambhacittatā', 'fears': 'bhayāni',
 'fetters': 'saṃyojanāni', 'fires': 'aggī', 'forgetfulness': 'muṭṭhassaccaṃ', 'friendship': 'mittatā',
 'good teaching': 'saddhammaṃ', 'great desire': 'mahicchatā', 'Great desire': 'mahicchatā',
 'grounds': 'āyatanāni', 'hard': 'dovacassatā', 'hard to correct': 'dovacassatā', 'hear': 'asotukamyatā',
 'heedlessness': 'pamādo', 'impediments': 'kiñcanā', 'kinds': NDE, 'kinds of misconduct': 'duccaritāni',
 'lack': 'asampajaññatā', 'Lack of clear': 'asampajaññatā', 'lack of clear': 'asampajaññatā',
 'Lack of confidence': 'assaddhiyaṃ', 'Lack of moral': 'anottappaṃ', 'lack of moral': 'anottappaṃ',
 'laziness': 'kosajjaṃ', 'mental': 'āsavā', 'mental taints': 'āsavā', 'mind': 'cetaso',
 'misconduct': 'duccaritāni', 'modes': 'vidhā', 'moral': 'anottappaṃ', 'noble': 'ariyānaṃ', 'non-restraint': 'asaṃvaro',
 'ones': 'ariyānaṃ', 'path': 'magga', 'perception': 'saññā', 'Perception of diversity': 'nānattasaññā',
 'perceptions': 'saññā', 'quests': 'esanā', 'restlessness': 'uddhaccaṃ', 'roots': 'mūlāni', 'sectarian': 'titthāyatanāni',
 'self': 'attānudiṭṭhi', 'self-ranking': 'vidhā', 'shamelessness': 'ahirikaṃ', 'sluggishness': 'līnattaṃ',
 'Sluggishness of mind': 'cetaso ca līnattaṃ', 'stains': 'malāni', 'taints': 'āsavā', 'teaching': 'saddhammaṃ',
 'thoughts': 'vitakkā', 'threes': 'Tikaṃ', 'uncharitableness': 'avadaññutā', 'unevennesses': 'visamāni',
 'unrighteous': 'adhamma', 'Unrighteous conduct': 'adhammacariyā', 'unwholesome': 'akusala',
 'unwholesome elements': 'akusaladhātuyo', 'unwholesome perceptions': 'akusalasaññā',
 'unwholesome roots': 'akusalamūlāni', 'unwholesome thoughts': 'akusalavitakkā', 'unwise': 'ayoniso',
 'Unwise attention': 'ayoniso manasikāro', 'view': 'diṭṭhi', 'view of enjoyment': 'assādadiṭṭhi',
 'wishing': 'kamyatā', 'wishing to hear': 'asotukamyatā', 'wrong': 'micchā', 'wrong path': 'kummagga',
 'Wrong view': 'micchādiṭṭhi', 'wrong view': 'micchādiṭṭhi'}
M['2-17-1-3-0'] = {'fours': 'Catukka', 'matrix': 'mātikā'}
M['2-835'] = {
 'arisings': 'uppādā', 'astray': 'agati', 'clinging': 'upādānāni', 'craving': 'taṇhuppādā',
 'distortions': 'vipariyāsā', 'fears': 'bhayāni', 'floods': 'oghā', 'fours': 'Catukkaṃ', 'going': 'gamanāni',
 'ignoble': 'anariya', 'kinds': NDE, 'kinds of clinging': 'upādānāni', 'kinds of misconduct': 'duccaritāni',
 'mental': 'āsavā', 'mental taints': 'āsavā', 'misconduct': 'duccaritāni', 'speech': 'vohārā', 'taints': 'āsavā',
 'ties': 'ganthā', 'views': 'diṭṭhiyo', 'ways': 'gamanāni', 'yokes': 'yogā'}
M['2-17-1-4-0'] = {'fives': 'Pañcaka', 'matrix': 'mātikā'}
M['2-836'] = {
 'actions': 'kammāni', 'attachments': 'saṅgā', 'barrennesses': 'khilā', 'bondages': 'vinibandhā',
 'dangers': 'ādīnavā', 'darts': 'sallā', 'doctrines': 'vādā', 'doctrines of Nibbāna': 'nibbānavādā',
 'fears': 'bhayāni', 'fetters': 'saṃyojanāni', 'fives': 'Pañcakaṃ', 'hindrances': 'nīvaraṇāni', 'hostilities': 'verā',
 'immediate': 'ānantarikāni', 'impatience': 'akkhantiyā', 'kinds': NDE, 'kinds of stinginess': 'macchariyāni',
 'life': 'diṭṭhadhamma', 'mind': 'ceto', 'stinginess': 'macchariyāni', 'views': 'diṭṭhiyo'}
M['2-17-1-5-0'] = {'matrix': 'mātikā', 'Matrix of Sixes': 'Chakkamātikā', 'sixes': 'Chakka'}
M['2-837'] = {
 'classes': 'kāyā', 'craving': 'taṇhā', 'desires-and-lusts': 'chandarāgā', 'dispute': 'vivāda',
 'disrespect': 'agāravā', 'equanimity': 'upekkhā', 'explorations': 'upavicārā', 'grief': 'domanassupavicārā',
 'grounds': 'vatthūni', 'household': 'gehasitāni', 'household equanimity': 'gehasitā upekkhā',
 'household grief': 'gehasitāni domanassāni', 'household joy': 'gehasitāni somanassāni',
 'joy': 'somanassupavicārā', 'kinds': NDE, 'kinds of disrespect': 'agāravā', 'kinds of household': 'gehasitāni',
 'lead to decline': 'parihāniyā', 'opposition': 'virodha', 'roots': 'mūlāni', 'sixes': 'Chakkaṃ', 'things': 'dhammā',
 'things that lead': 'parihāniyā dhammā', 'views': 'diṭṭhiyo'}
M['2-17-1-6-0'] = {'matrix': 'mātikā', 'sevens': 'Sattaka'}
M['2-838'] = {
 'bad': 'asaddhammā', 'conceits': 'mānā', 'fetters': 'saṃyojanāni', 'kinds': NDE, 'kinds of misconduct': 'duccaritāni',
 'misconduct': 'duccaritāni', 'obsessions': 'pariyuṭṭhānāni', 'qualities': 'asaddhammā', 'sevens': 'Sattakaṃ',
 'tendencies': 'anusayā', 'underlying': 'anusayā', 'underlying tendencies': 'anusayā', 'views': 'diṭṭhiyo'}
M['2-17-1-7-0'] = {'eights': 'Aṭṭhaka', 'matrix': 'mātikā'}
M['2-839'] = {
 'defilement': 'kilesa', 'doctrines': 'vādā', 'eights': 'Aṭṭhakaṃ', 'faults': 'dosā', 'grounds': 'vatthūni',
 'grounds of defilement': 'kilesavatthūni', 'grounds of laziness': 'kusītavatthūni', 'ignoble': 'anariya',
 'laziness': 'kusīta', 'mind': 'cittassa', 'neither-percipient-nor-non-percipient': 'nevasaññināsaññi',
 'non-percipient': 'asaññi', 'person': 'purisa', 'resistance': 'paṭighāto', 'speech': 'vohārā', 'ways': 'vohārā',
 'worldly': 'lokadhammesu', 'wrongnesses': 'micchattā'}
M['2-17-1-8-0'] = {'matrix': 'mātikā', 'nines': 'Navaka'}
M['2-840'] = {
 'agitations': 'iñjitāni', 'conceit': 'mānā', 'constructions': 'saṅkhatāni', 'craving': 'taṇhā', 'grounds': 'vatthūni',
 'imaginings': 'maññitāni', 'kinds': 'navavidhā', 'nines': 'Navakaṃ', 'person': 'purisa',
 'proliferations': 'papañcitāni', 'resentment': 'āghāta', 'rooted': 'mūlakā', 'stains': 'malāni', 'things': 'dhammā',
 'things rooted': 'mūlakā dhammā', 'waverings': 'phanditāni'}
M['2-17-1-9-0'] = {'matrix': 'mātikā', 'Matrix of Tens': 'Dasakamātikā', 'tens': 'Dasaka'}
M['2-841'] = {
 'courses': 'pathā', 'defilement': 'kilesa', 'extremist': 'antaggāhikā', 'extremist view': 'antaggāhikā diṭṭhi',
 'fetters': 'saṃyojanāni', 'grounds': 'vatthūni', 'grounds of defilement': 'kilesavatthūni', 'resentment': 'āghāta',
 'ten': 'Dasa', 'ten fetters': 'dasa saṃyojanāni', 'ten grounds': 'dasavatthukā', 'ten wrongnesses': 'dasa micchattā',
 'tens': 'Dasakaṃ', 'unwholesome': 'akusala', 'view': 'diṭṭhi', 'view with ten': 'dasavatthukā micchādiṭṭhi',
 'wrong': 'micchā', 'wrong view': 'micchādiṭṭhi', 'Wrong view': 'micchādiṭṭhi', 'wrongnesses': 'micchattā'}
M['2-842'] = {
 'blessed': 'bhagavatā', 'concerning': 'upādāya', 'craving': 'taṇhā', 'eighteen': 'Aṭṭhārasa',
 'exposition': 'veyyākaraṇe', 'external': 'bāhirassa', 'gathering': 'abhisaññūhitvā', 'grounds': 'gatāni',
 'hundred': 'sataṃ', 'internal': 'ajjhattikassa', 'matrix': 'Mātikā', 'sixty-two': 'dvāsaṭṭhi', 'spoken': 'vuttāni',
 'summing': 'abhisaṅkhipitvā', 'thirty-six': 'chattiṃsa', 'together': 'tadekajjhaṃ', 'views': 'diṭṭhi',
 'wanderings': 'vicaritāni', 'wanderings of craving': 'taṇhāvicaritāni', 'Wanderings of Craving': 'taṇhāvicaritāni'}

# ---------------------------------------------------------------- exposition of the ones
# "the intoxication, being intoxicated ... the mind's desire for a flag"
MADA = {
 'arrogance': 'sampaggāho', 'banner': 'dhajo', 'conceit': 'māno', 'conceiving': 'maññanā', 'desire': 'kamyatā',
 'flag': 'ketu', 'haughtiness': 'unnāmo', 'intoxicated': 'majjanā', 'intoxication': 'mado', 'loftiness': 'unnati',
 'mind': 'cittassa', 'state of conceiving': 'maññitattaṃ', 'state of intoxication': 'majjitattaṃ', 'therein': 'Tattha'}
M['2-17-2-0'] = {'exposition': 'niddeso', 'ones': 'Ekaka'}
M['2-17-2-1-0'] = {'birth': 'Jāti', 'intoxication': 'mado', 'Intoxication with birth': 'Jātimado'}
M['2-843'] = mg(MADA, {'account of birth': 'Jātiṃ paṭicca', 'birth': 'Jātiṃ', 'Intoxication with birth': 'jātimado'})
M['2-17-2-2-0'] = {'clan': 'Gotta', 'intoxication': 'Gottamadādī', 'intoxication with clan': 'Gottamadādī', 'rest': 'ādī'}
M['2-844'] = mg(MADA, {
 'absorption': 'jhānaṃ', 'alms-goer': 'piṇḍapātikattaṃ', 'beauty': 'vaṇṇaṃ', 'build': 'pariṇāhaṃ', 'clan': 'Gottaṃ',
 'completeness': 'pāripūriṃ', 'craft': 'sippaṃ', 'deportment': 'iriyāpathaṃ', 'despised': 'anavaññātaṃ',
 'fame': 'yasaṃ', 'figure': 'saṇṭhānaṃ', 'health': 'ārogyaṃ', 'height': 'ārohaṃ', 'honour': 'sakkāraṃ',
 'intoxication with clan': 'gottamado', 'intoxication with completeness': 'pāripūrimado', 'learning': 'sutaṃ',
 'life': 'jīvitaṃ', 'meditative': 'jhānaṃ', 'meditative absorption': 'jhānaṃ', 'Meditative absorption': 'jhānaṃ',
 'quick': 'paṭibhānaṃ', 'quick understanding': 'paṭibhānaṃ', 'respect': 'garukāraṃ', 'seniority': 'rattaññutaṃ',
 'success': 'iddhiṃ', 'understanding': 'paṭibhānaṃ', 'virtue': 'sīlaṃ', 'wealth': 'bhogaṃ', 'youth': 'yobbanaṃ'})
M['2-17-2-3-0'] = {'intoxication': 'Mado'}
M['2-845'] = dict(MADA)
M['2-17-2-4-0'] = {'heedlessness': 'Pamādo'}
M['2-846'] = {
 'acting': 'kiriyatā', 'acting inconstantly': 'anaṭṭhitakiriyatā', 'behaviour': 'vuttitā', 'bodily': 'Kāya',
 'bodily misconduct': 'Kāyaduccarite', 'Bodily misconduct': 'Kāyaduccarite', 'desire': 'chandatā',
 'heedless': 'pamajjanā', 'heedlessness': 'pamādo', 'inconstantly': 'anaṭṭhita', 'kind': 'evarūpo',
 'letting': 'vossaggo', 'Letting the mind': 'cittassa vossaggo', 'loose': 'vossaggo', 'mental': 'mano',
 'mental misconduct': 'manoduccarite', 'mind': 'cittassa', 'mind loose': 'cittassa vossaggo',
 'misconduct': 'duccarite', 'non-application': 'ananuyogo', 'non-cultivation': 'abahulīkammaṃ',
 'non-development': 'abhāvanā', 'non-practice': 'anāsevanā', 'non-resolution': 'anadhiṭṭhānaṃ',
 'perseverance': 'sātacca', 'pleasure': 'kāma', 'putting': 'nikkhitta', 'repeatedly': 'ānuppadānaṃ',
 'respect': 'sakkacca', 'responsibility': 'dhuratā', 'sense': 'kāma', 'sense pleasure': 'kāma', 'sluggish': 'olīna',
 'strands': 'guṇesu', 'strands of sense': 'kāmaguṇesu', 'therein': 'Tattha', 'things': 'dhammānaṃ', 'verbal': 'vacī',
 'verbal misconduct': 'vacīduccarite', 'whatever': 'yo', 'wholesome': 'kusalānaṃ',
 'wholesome things': 'kusalānaṃ vā dhammānaṃ'}
M['2-17-2-5-0'] = {'obstinacy': 'Thambho'}
M['2-847'] = {
 'hardness': 'kakkhaḷiyaṃ', 'harshness': 'phārusiyaṃ', 'mind': 'cittatā', 'obstinacy': 'thambho',
 'obstinate': 'thambhanā', 'rigidity': 'ujucittatā', 'therein': 'Tattha', 'unpliability': 'amudutā'}
M['2-17-2-6-0'] = {'contentiousness': 'Sārambho'}
M['2-848'] = {
 'contentious': 'sārambhanā', 'contentiousness': 'sārambho', 'counter-contentious': 'paṭisārambhanā',
 'counter-contentiousness': 'paṭisārambho', 'therein': 'Tattha'}
M['2-17-2-7-0'] = {'desire': 'icchatā', 'excessive': 'Atricchatā', 'excessive desire': 'Atricchatā'}
WANT = {
 'alms-food': 'piṇḍapāta', 'desire': 'icchā', 'desirous': 'icchāgatā', 'discontented': 'asantuṭṭhassa',
 'dwelling': 'senāsana', 'dwelling place': 'senāsana', 'kind': 'evarūpā', 'lust': 'rāgo', 'medicinal': 'bhesajja',
 'mind': 'cittassa', 'passion': 'sārāgo', 'place': 'senāsana', 'pleasure': 'kāma', 'robes': 'cīvara', 'sense': 'kāma',
 'sense pleasure': 'kāma', 'sick': 'gilāna', 'strands': 'guṇehi', 'strands of sense': 'kāmaguṇehi',
 'supports': 'paccaya', 'therein': 'Tattha', 'wanting': 'bhiyyokamyatā', 'whatever': 'Itarītara'}
M['2-849'] = mg(WANT, {'excessive': 'atricchatā', 'excessive desire': 'atricchatā'})
M['2-17-2-8-0'] = {'desire': 'icchatā', 'great desire': 'Mahicchatā', 'Great desire': 'Mahicchatā'}
M['2-850'] = mg(WANT, {'Great desire': 'mahicchatā', 'great desire': 'mahicchatā'})
M['2-17-2-9-0'] = {'desire': 'icchatā', 'evil': 'Pāpicchatā', 'evil desire': 'Pāpicchatā'}
M['2-851'] = {
 'bad': 'dussīlo', 'bad conduct': 'dussīlo', 'concentrated': 'samāhitoti', 'conduct': 'dussīlo',
 'confidence': 'assaddho', 'delighting': 'ārāmo', 'desire': 'icchā', 'desirous': 'icchāgatā',
 'destroyed': 'akhīṇāsavo', 'energetic': 'āraddhavīriyoti', 'established': 'upaṭṭhitassatīti', 'evil': 'pāpicchatā',
 'evil desire': 'pāpicchatā', 'forgetful': 'muṭṭhassatī', 'having': NDE, 'kind': 'evarūpā', 'know': 'jānātū',
 'lazy': 'kusīto', 'learned': 'bahussutoti', 'learning': 'appassuto', 'lust': 'rāgo', 'mental': 'āsavo',
 'mental taints': 'āsavo', 'mind': 'cittassa', 'mindfulness': 'upaṭṭhitassatīti', 'passion': 'sārāgo',
 'people': 'jano', 'secluded': 'pavivittoti', 'someone': 'ekacco', 'taints': 'āsavo', 'therein': 'Tattha',
 'unconcentrated': 'asamāhito', 'virtuous': 'sīlavāti', 'whatever': 'yā', 'wisdom': 'duppañño', 'wise': 'paññavāti',
 'wishes': 'icchati'}
M['2-17-2-10-0'] = {'affectation': 'Siṅgaṃ'}
M['2-852'] = {
 'affectation': 'siṅgaṃ', 'affected': 'siṅgāratā', 'artfulness': 'cāturiyaṃ', 'cleverness': 'cāturatā',
 'elegance': 'parikkhattatā', 'studied': 'parikkhattatā', 'therein': 'Tattha'}
M['2-17-2-11-0'] = {'greediness': 'Tintiṇaṃ'}
M['2-853'] = {
 'covetous': 'loluppāyanā', 'covetousness': 'loluppaṃ', 'desire': 'pucchañjikatā', 'greediness': 'tintiṇaṃ',
 'greedy': 'tintiṇāyanā', 'itching': 'pucchañjikatā', 'nice': 'sādhu', 'therein': 'Tattha', 'wish': 'kamyatā'}
M['2-17-2-12-0'] = {'frivolity': 'Cāpalyaṃ'}
M['2-854'] = {
 'adorning': 'maṇḍanā', 'beautifying': 'vibhūsanā', 'body': 'kāyassa', 'bowl': 'patta', 'delighting': 'giddhikatā',
 'dwelling': 'senāsana', 'dwelling place': 'senāsana', 'fickleness': 'capalatā', 'frivolity': 'cāpalyaṃ',
 'outward': 'bāhirānaṃ', 'place': 'senāsana', 'playing': 'keḷanā', 'putrid': 'pūti', 'requisites': 'parikkhārānaṃ',
 'robes': 'Cīvara', 'therein': 'Tattha'}
M['2-17-2-13-0'] = {'behaviour': 'vutti', 'discordant': 'Asabhāga'}
M['2-855'] = {
 'behaviour': 'vutti', 'brother': 'bhātari', 'buddha': 'buddhe', 'contrary': 'vippaṭikūla', 'deference': 'appatissavatā',
 'delight': 'sātatā', 'disciples': 'sāvakesu', 'discordant': 'asabhāga', 'disrespect': 'anādariyaṃ',
 'disrespectfulness': 'anādariyatā', 'elder': 'jeṭṭhe', 'father': 'pitari', 'grasping': 'ggāhitā',
 'lack': 'agāravatā', 'lack of deference': 'appatissavatā', 'lack of reverence': 'agāravatā', 'mother': 'Mātari',
 'opposition': 'vipaccanīka', 'others': 'aññataraññataresu', 'place': 'ṭhāniyesu', 'preceptor': 'upajjhāye',
 'respect': 'garu', 'reverence': 'agāravatā', 'stand': 'ṭhāniyesu', 'teachers': 'ācariyesu', 'therein': 'Tattha',
 'towards': NDE}
M['2-17-2-14-0'] = {'discontent': 'Arati'}
M['2-856'] = {
 'anxiety': 'paritassitā', 'delighting': 'anabhiramaṇā', 'discontent': 'arati', 'discontented': 'aratitā',
 'dissatisfaction': 'anabhirati', 'dwelling': 'senāsanesu', 'dwelling places': 'senāsanesu', 'places': 'senāsanesu',
 'remote': 'Pantesu', 'restlessness': 'ukkaṇṭhitā', 'therein': 'Tattha', 'things': 'dhammesu',
 'wholesome': 'kusalesu', 'wholesome things': 'kusalesu dhammesu'}
M['2-17-2-15-0'] = {'sloth': 'Tandī'}
M['2-857'] = {
 'laziness': 'ālasyaṃ', 'lazy': 'ālasyāyanā', 'mental': 'tandimanakatā', 'sloth': 'tandī', 'slothful': 'tandiyanā',
 'sluggishness': 'tandimanakatā', 'therein': 'Tattha'}
M['2-17-2-16-0'] = {'oneself': NDE, 'stretching': 'Vijambhitā', 'Stretching oneself': 'Vijambhitā'}
M['2-858'] = {
 'bending': 'ānamanā', 'body': 'kāyassa', 'forward': 'ānamanā', 'oneself': NDE, 'restlessness': 'byādhiyakaṃ',
 'sideways': 'vinamanā', 'stretching': 'jambhanā', 'Stretching oneself': 'vijambhitā', 'therein': 'Tattha',
 'together': 'sannamanā'}
M['2-17-2-17-0'] = {'drowsiness': 'sammado', 'meals': 'Bhatta'}
M['2-859'] = {
 'body': 'kāya', 'burning': 'pariḷāho', 'drowsiness': 'sammado', 'eaten': 'bhuttāvissa', 'faintness': 'mucchā',
 'food': 'bhatta', 'heaviness': 'duṭṭhullaṃ', 'meals': 'bhatta', 'therein': 'Tattha', 'weariness': 'kilamatho'}
M['2-17-2-18-0'] = {'mind': 'Cetaso', 'sluggishness': 'līnattaṃ', 'Sluggishness of mind': 'Cetaso ca līnattaṃ'}
M['2-860'] = {
 'dull': 'thīyanā', 'dullness': 'thinaṃ', 'lack': 'akalyatā', 'mind': 'cittassa', 'readiness': 'akalyatā',
 'sagging': 'olīyanā', 'sloth': 'līnaṃ', 'slothful': 'līyanā', 'slothfulness': 'līyitattaṃ', 'sluggishness': 'līnattaṃ',
 'Sluggishness of mind': 'cetaso ca līnattaṃ', 'slumping': 'sallīyanā', 'therein': 'Tattha',
 'unworkableness': 'akammaññatā'}
# "for one relying on gain, honour and renown, of evil desires, driven by desire" (genitive)
GAIN = {
 'desire': 'icchā', 'desires': 'pāpicchassa', 'driven': 'pakatassa', 'driven by desire': 'icchāpakatassa',
 'evil': 'pāpicchassa', 'evil desires': 'pāpicchassa', 'honour': 'sakkāra', 'relying': 'sannissitassa',
 'relying on gain': 'Lābhasakkārasilokasannissitassa', 'renown': 'siloka', 'therein': 'Tattha'}
M['2-17-2-19-0'] = {'trickery': 'Kuhanā'}
M['2-861'] = mg(GAIN, {
 'arranging': 'ṭhapanā', 'composing': 'saṇṭhapanā', 'deportment': 'iriyāpathassa', 'frowning': 'bhākuṭitā',
 'look': 'bhākuṭiyaṃ', 'reckoned': 'saṅkhātena', 'requisites': 'paccaya', 'roundabout': 'sāmantajappitena',
 'setting': 'aṭhapanā', 'talk': 'jappitena', 'trickery': 'kuhanā', 'tricky': 'kuhāyanā'})
M['2-17-2-20-0'] = {'talk': 'Lapanā', 'wheedling': 'Lapanā'}
M['2-862'] = mg(GAIN, {
 'addressing': 'ālapanā', 'along': 'sallapanā', 'children': 'pāribhaṭayatā', 'coaxing': 'ukkācanā',
 'constant': 'anuppiyabhāṇitā', 'excessive': 'samunnahanā', 'fawning': 'cāṭukamyatā', 'flattering': 'unnahanā',
 'fondling': 'pāribhaṭayatā', 'half-truthful': 'muggasūpyatā', 'others': 'paresaṃ', 'pleasant': 'anuppiyabhāṇitā',
 'round': 'samullapanā', 'talk': 'lapanā', 'talking': 'lapanā', 'wheedling': 'lapanā'})
M['2-17-2-21-0'] = {'hinting': 'Nemittikatā'}
M['2-863'] = mg(GAIN, {
 'hinting': 'nemittikatā', 'indirect': 'parikathā', 'others': 'paresaṃ', 'roundabout': 'sāmantajappā',
 'sign': 'nimittaṃ', 'signs': 'nimittakammaṃ', 'suggestion': 'obhāso', 'suggestions': 'obhāsakammaṃ',
 'talk': 'jappā'})
M['2-17-2-22-0'] = {'belittling': 'Nippesikatā'}
M['2-864'] = mg(GAIN, {
 'abusing': 'akkosanā', 'backbiting': 'parapiṭṭhimaṃsikatā', 'belittling': 'nippesikatā', 'blaming': 'garahaṇā',
 'carrying': 'hārikā', 'criticism': 'avaṇṇa', 'defaming': 'sampāpanā', 'deriding': 'ukkhepanā',
 'discrediting': 'pāpanā', 'disparaging': 'vambhanā', 'mocking': 'khipanā', 'others': 'paresaṃ',
 'ridiculing': 'samukkhepanā', 'scoffing': 'saṅkhipanā'})
M['2-17-2-23-0'] = {'chasing': 'nijigīsanatā', 'Chasing gain': 'lābhaṃ nijigīsanatā'}
M['2-865'] = {
 'brings': 'āharati', 'carries': 'harati', 'chasing': 'nijigīsanatā', 'Chasing gain': 'lābhaṃ nijigīsanatā',
 'desire': 'icchā', 'desires': 'pāpiccho', 'driven': 'pakato', 'driven by desire': 'icchāpakato', 'evil': 'pāpiccho',
 'evil desires': 'pāpiccho', 'honour': 'sakkāra', 'kind': 'evarūpā', 'relying': 'sannissito',
 'relying on gain': 'Lābhasakkārasilokasannissito', 'renown': 'siloka', 'searching': 'esanā', 'therein': 'Tattha',
 'whatever': 'yā'}

# conceit "I am better / equal / worse"
GROUND = {
 'account of birth': 'jātiyā', 'beauty': 'pokkharatāya', 'beauty of complexion': 'vaṇṇapokkharatāya', 'birth': 'jātiyā',
 'branch': 'ṭṭhānena', 'branch of science': 'vijjāṭṭhānena', 'clan': 'gottena', 'complexion': 'vaṇṇa',
 'craft': 'sippāyatanena', 'family': 'kolaputtiyena', 'field': 'āyatanena', 'field of craft': 'sippāyatanena',
 'field of work': 'kammāyatanena', 'good family': 'kolaputtiyena', 'ground': 'vatthunā', 'kind': 'evarūpo',
 'learning': 'sutena', 'quick': 'paṭibhānena', 'quick understanding': 'paṭibhānena', 'science': 'vijjāṭṭhānena',
 'someone': 'ekacco', 'study': 'ajjhenena', 'therein': 'Tattha', 'understanding': 'paṭibhānena', 'wealth': 'dhanena',
 'whatever': 'yo'}
CONCEIT = mg(MADA, {'nurses': 'jappeti', 'nurses conceit': 'mānaṃ jappeti', 'conceit on account': 'jātiyā / mānaṃ'})
SELFBEL = {
 'belittling': 'omaññanā', 'belittling oneself': 'omaññanā', 'conceit': 'māno', 'despising': 'hīḷanā',
 'looking': 'ohīḷanā', 'nurses': 'jappeti', 'nurses self-belittling': 'omānaṃ jappeti', 'oneself': NDE,
 'self-belittling': 'omāno', 'self-contempt': 'attuññā', 'self-disparagement': 'attaparibhavo',
 'self-scorn': 'attavaññā', 'state of belittling': 'omaññitattaṃ'}
REL = {'himself': 'attānaṃ', 'others': 'parehi', 'regards': 'dahati', 'relying': 'nissāya', 'whatever': 'Yo'}
M['2-17-2-24-0'] = {'conceit': 'māno'}
M['2-866'] = mg(GROUND, CONCEIT)
M['2-17-2-25-0'] = {'conceit': 'māno', 'equal': 'Sadisohamasmīti'}
M['2-867'] = mg(GROUND, CONCEIT, equal='sadisohamasmīti')
M['2-17-2-26-0'] = {'conceit': 'māno', 'worse': 'Hīnohamasmīti'}
M['2-868'] = mg(GROUND, SELFBEL, worse='hīnohamasmīti')
M['2-17-2-27-0'] = {'conceit': 'māno'}
M['2-869'] = mg(GROUND, CONCEIT, REL)
M['2-17-2-28-0'] = {'conceit': 'māno', 'equal': 'sadisohamasmīti'}
M['2-870'] = mg(GROUND, CONCEIT, REL, equal='sadisohamasmīti')
M['2-17-2-29-0'] = {'conceit': 'māno', 'worse': 'hīnohamasmīti'}
M['2-871'] = mg(GROUND, SELFBEL, REL, worse='hīnohamasmīti')
M['2-17-2-30-0'] = {'conceit': 'māno', 'equal': 'Sadisassa'}
M['2-872'] = mg(GROUND, CONCEIT, REL, {'equal': 'sadisassa', 'equal on account': 'sadiso / jātiyā'})
M['2-17-2-31-0'] = {'conceit': 'māno', 'equal': 'Sadisassa'}
M['2-873'] = mg(GROUND, CONCEIT, REL, {'equal': 'sadisassa', 'equal on account': 'sadiso / jātiyā'})
M['2-17-2-32-0'] = {'conceit': 'māno', 'equal': 'Sadisassa', 'worse': 'hīnohamasmīti'}
M['2-874'] = mg(GROUND, SELFBEL, REL, {'equal': 'sadisassa', 'equal on account': 'sadiso / jātiyā',
                                       'worse': 'hīnohamasmīti'})
M['2-17-2-33-0'] = {'conceit': 'māno', 'worse': 'Hīnassa'}
M['2-875'] = mg(GROUND, CONCEIT, REL, {'worse': 'hīnassa', 'worse on account': 'hīno / jātiyā'})
M['2-17-2-34-0'] = {'conceit': 'māno', 'equal': 'sadisohamasmīti', 'worse': 'Hīnassa'}
M['2-876'] = mg(GROUND, CONCEIT, REL, {'equal': 'sadisohamasmīti', 'worse': 'hīnassa',
                                       'worse on account': 'hīno / jātiyā'})
M['2-17-2-35-0'] = {'conceit': 'māno', 'worse': 'Hīnassa'}
M['2-877'] = mg(GROUND, SELFBEL, REL, {'equal': 'sadisaṃ', 'worse': 'hīnassa', 'worse on account': 'hīno / jātiyā'})
M['2-17-2-36-0'] = {'conceit': 'Māno'}
M['2-878'] = dict(MADA)
M['2-17-2-37-0'] = {'conceit': 'māno', 'exaggerated': 'Atimāno', 'Exaggerated conceit': 'Atimāno'}
M['2-879'] = mg(GROUND, MADA, {'despises': 'atimaññati', 'exaggerated': 'atimāno', 'Exaggerated conceit': 'atimāno',
                               'others': 'parehi', 'whatever': 'Yo'})
M['2-17-2-38-0'] = {'beyond': 'ātimāno', 'conceit': 'Mānātimāno', 'Conceit beyond conceit': 'Mānātimāno'}
M['2-880'] = mg(GROUND, MADA, REL, {'beyond': 'ātimāno', 'Conceit beyond conceit': 'mānātimāno', 'equal': 'sadisaṃ'})
M['2-17-2-39-0'] = {'conceit': 'Omāno', 'self-belittling': 'Omāno', 'Self-belittling conceit': 'Omāno'}
M['2-881'] = mg(GROUND, SELFBEL, {'Self-belittling conceit': 'omāno', 'whatever': 'Yo'})
M['2-17-2-40-0'] = {'conceit': 'Adhimāno', 'over-estimating': 'Adhimāno', 'Over-estimating conceit': 'Adhimāno'}
M['2-882'] = mg(MADA, {
 'attained': 'adhigata', 'done': 'kata', 'kind': 'evarūpo', 'over-estimating': 'adhimāno',
 'Over-estimating conceit': 'adhimāno', 'perceiving': 'saññitā', 'realised': 'sacchikata', 'whatever': 'yo'})
M['2-17-2-41-0'] = {'conceit': 'Asmimāno'}
M['2-883'] = mg(MADA, {
 'consciousness': 'viññāṇaṃ', 'desire': 'chando', 'feeling': 'vedanā', 'form': 'Rūpaṃ', 'formations': 'saṅkhārā',
 'kind': 'evarūpo', 'material': 'Rūpaṃ', 'material form': 'Rūpaṃ', 'perception': 'saññā', 'regard': NDE,
 'tendency': 'anusayo', 'underlying': 'anusayo', 'underlying tendency': 'anusayo', 'whatever': 'yo'})
M['2-17-2-42-0'] = {'conceit': 'Micchāmāno', 'wrong': 'Micchāmāno', 'Wrong conceit': 'Micchāmāno'}
M['2-884'] = mg(GROUND, CONCEIT, {
 'conceit on account': 'pāpakena / mānaṃ', 'evil': 'pāpakena', 'evil field': 'pāpakena vā kammāyatanena',
 'observance': 'vatena', 'view': 'diṭṭhiyā', 'virtue': 'sīlena', 'virtue-and-observance': 'sīlabbatena',
 'wrong': 'micchāmāno', 'Wrong conceit': 'micchāmāno'})
# thoughts (vitakka) connected with the household life
THINK = {
 'concerning': 'ārabbha', 'connected': 'gehasito', 'household': 'geha', 'household life': 'gehasito',
 'intention': 'saṅkappo', 'intention connected': 'gehasito / saṅkappo', 'life': 'gehasito', 'therein': 'Tattha',
 'thinking': 'takko', 'thought': 'vitakko', 'thoughts': 'vitakko', 'wrong': 'micchā',
 'wrong intention': 'micchāsaṅkappo', 'wrong intention connected': 'gehasito / micchāsaṅkappo'}
M['2-17-2-43-0'] = {'relatives': 'Ñāti', 'thoughts': 'vitakko'}
M['2-885'] = mg(THINK, relatives='Ñātake')
M['2-17-2-44-0'] = {'home': 'Janapada', 'thoughts': 'vitakko'}
M['2-886'] = mg(THINK, home='Janapadaṃ')
M['2-17-2-45-0'] = {'dying': 'Amara', 'thoughts': 'vitakko'}
M['2-887'] = mg(THINK, {'austerities': 'Dukkara', 'dying': 'amara', 'practice': 'kāritā', 'resort': 'gata',
                        'resort to views': 'diṭṭhigata', 'views': 'diṭṭhi'})
THC = {'connected': 'paṭisaṃyutto', 'thought': 'vitakko', 'Thought connected': 'paṭisaṃyutto vitakko',
       'thought connected': 'paṭisaṃyutto vitakko'}
M['2-17-2-46-0'] = mg(THC, {'others': 'Parānuddayatāpaṭisaṃyutto', 'sympathy': 'ānuddayatā'})
M['2-888'] = mg(THINK, THC, {
 'arise': 'uppannesu', 'duties': 'karaṇīyesu', 'dwells': 'viharati', 'effort': 'yogaṃ', 'happy': 'sukhitesu',
 'himself': 'attanā', 'householders': 'gihīhi', 'mixed': 'saṃsaṭṭho', 'others': 'parānuddayatāpaṭisaṃyutto',
 'pained': 'dukkhito', 'rejoicing': 'sahanandī', 'someone': 'ekacco', 'sorrowing': 'sahasokī',
 'sympathy': 'ānuddayatā', 'takes': 'āpajjati', 'tasks': 'kicca'})
M['2-17-2-47-0'] = mg(THC, rest='ādi')
M['2-889'] = mg(THINK, THC, {'honour': 'sakkāra', 'renown': 'siloka'})
M['2-17-2-48-0'] = mg(THC, despised='Anavaññatti')
M['2-890'] = mg(GROUND, THINK, THC, {
 'despise': 'avajāniṃsūti', 'despised': 'anavaññatti', 'ones': 'Ekakaṃ', 'others': 'pare', 'thinks': NDE})

# ---------------------------------------------------------------- exposition of the twos
M['2-17-3-0'] = {'exposition': 'niddeso', 'twos': 'Duka'}
M['2-17-3-1-0'] = {'anger': 'Kodho', 'resentment': 'upanāho'}
M['2-891'] = {
 'afterwards': 'aparakālaṃ', 'anger': 'kodho', 'angry': 'kujjhanā', 'carried': 'anuppabandhanā',
 'continuing': 'anusaṃsandanā', 'dissatisfaction': 'anattamanatā', 'fierceness': 'caṇḍikkaṃ', 'fixing': 'saṇṭhapanā',
 'hate': 'doso', 'hating': 'dussanā', 'hostility': 'paṭivirodho', 'keeping': 'aṭṭhapanā', 'kind': 'evarūpo',
 'maintaining': 'ṭhapanā', 'malice': 'byāpatti', 'malicious': 'byāpajjanā', 'mind': 'cittassa', 'opposition': 'virodho',
 'resenting': 'upanayhanā', 'resentment': 'upanāho', 'rudeness': 'asuropo', 'therein': 'tattha', 'whatever': 'Yo'}
M['2-17-3-2-0'] = {'contempt': 'Makkho', 'domineering': 'paḷāso'}
M['2-892'] = {
 'act': 'niṭṭhuriyakammaṃ', 'contempt': 'makkho', 'contemptuous': 'makkhāyanā', 'disdain': 'niṭṭhuriyaṃ',
 'dispute': 'vivāda', 'domineering': 'paḷāso', 'refusing': 'appaṭinissaggo', 'side': 'yugaggāho',
 'taking': 'paḷāsāhāro', 'therein': 'tattha'}
M['2-17-3-3-0'] = {'envy': 'Issā', 'stinginess': 'macchariyañca'}
M['2-893'] = {
 'dwellings': 'āvāsa', 'envious': 'issāyanā', 'envy': 'issā', 'esteem': 'mānana', 'families': 'kula',
 'grip': 'aggahitattaṃ', 'honour': 'sakkāra', 'jealous': 'usūyanā', 'jealousy': 'usūyā', 'kind': 'evarūpaṃ',
 'kinds': NDE, 'kinds of stinginess': 'macchariyāni', 'meanness': 'vevicchaṃ', 'mind': 'cittassa',
 'miserliness': 'kadariyaṃ', 'others': 'para', 'praise': 'vaṇṇa', 'respect': 'garukāra', 'salutation': 'vandana',
 'stinginess': 'macchariyaṃ', 'stingy': 'maccharāyanā', 'teaching': 'dhamma', 'therein': 'tattha',
 'tight-fistedness': 'kaṭukañcukatā', 'ungenerous': 'aggahitattaṃ', 'veneration': 'pūjanāsu', 'whatever': 'Yaṃ'}
M['2-17-3-4-0'] = {'deceit': 'Māyā', 'treachery': 'sāṭheyyañca'}
M['2-894'] = {
 'act': 'kiriyā', 'beyond': 'accāsarā', 'body': 'kāyena', 'bounds': 'accāsarā', 'cheating': 'vañcanā',
 'conceal': 'paṭicchādanahetuṃ', 'concealing': 'parigūhanā', 'covered': 'vocchādanā', 'covering': 'chādanā',
 'crookedness': 'kakkariyaṃ', 'deceit': 'māyā', 'deceitful': 'māyāvitā', 'distracting': 'vikiraṇā', 'done': 'caritvā',
 'elegance': 'parikkhattatā', 'evading': 'pariharaṇā', 'evil': 'pāpikaṃ', 'forms': 'paṇidahati', 'fraud': 'nikati',
 'going': 'accāsarā', 'having': NDE, 'hiding': 'gūhanā', 'intends': 'saṅkappeti', 'keeping': 'vocchādanā',
 'kind': 'evarūpā', 'know': 'jaññā', 'laying': 'anuttānīkammaṃ', 'mind': 'manasā', 'misconduct': 'duccaritaṃ',
 'order': 'paṭicchādanahetuṃ', 'plain': 'anāvikammaṃ', 'roughness': 'kakkaratā', 'someone': 'ekacco',
 'speaks': 'bhāsati', 'speech': 'vācāya', 'strives': 'parakkamati', 'studied': 'parikkhattatā', 'therein': 'tattha',
 'thoroughly': 'parisaṭho', 'treacherous': 'saṭho', 'treacherousness': 'saṭhaṃ', 'treachery': 'sāṭheyyaṃ',
 'whatever': 'Yā', 'wish': 'icchaṃ', 'wishes': 'icchati', 'words': 'vācaṃ'}
IGN = {
 'barrier': 'laṅgī', 'delusion': 'moho', 'ignorance': 'avijjā', 'knowledge': 'aññāṇaṃ', 'lack': 'aññāṇaṃ',
 'lack of knowledge': 'aññāṇaṃ', 'lack of vision': 'adassanaṃ', 'root': 'mūlaṃ', 'unwholesome': 'akusala',
 'unwholesome root': 'akusalamūlaṃ', 'vision': 'adassanaṃ', 'therein': 'tattha'}
EXIST = {
 'affection': 'sineho', 'burning': 'pariḷāho', 'craving': 'taṇhā', 'delight': 'nandī', 'desire': 'chando',
 'existence': 'bhava', 'fast': 'ajjhosānaṃ', 'infatuation': 'mucchā', 'lust': 'rāgo', 'regard': NDE}
M['2-17-3-5-0'] = {'craving': 'taṇhā', 'craving for existence': 'bhavataṇhā', 'existence': 'bhava',
                   'ignorance': 'Avijjā'}
M['2-895'] = mg(IGN, EXIST, {'craving for existence': 'bhavataṇhā'})
VIEWG = {
 'distorted': 'vipariyāsa', 'distorted grip': 'vipariyāsaggāho', 'grip': 'ggāho', 'kind': 'evarūpā', 'resort': 'gataṃ',
 'resort to views': 'diṭṭhigataṃ', 'self': 'attā', 'therein': 'tattha', 'view': 'diṭṭhi', 'views': 'diṭṭhi',
 'whatever': 'yā'}
M['2-17-3-6-0'] = {'existence': 'Bhava', 'non-existence': 'vibhava', 'view': 'diṭṭhi', 'view of existence': 'Bhavadiṭṭhi',
                   'view of non-existence': 'vibhavadiṭṭhi'}
M['2-896'] = mg(VIEWG, {'exist': 'Bhavissati', 'existence': 'bhava', 'non-existence': 'vibhava',
                        'view of existence': 'bhavadiṭṭhi', 'view of non-existence': 'vibhavadiṭṭhi'})
M['2-17-3-7-0'] = {'annihilationist': 'uccheda', 'annihilationist view': 'ucchedadiṭṭhi', 'eternalist': 'Sassata',
                   'eternalist view': 'Sassatadiṭṭhi', 'view': 'diṭṭhi'}
M['2-897'] = mg(VIEWG, {'annihilationist': 'uccheda', 'annihilationist view': 'ucchedadiṭṭhi', 'eternal': 'Sassato',
                        'eternalist': 'sassata', 'eternalist view': 'sassatadiṭṭhi'})
M['2-17-3-8-0'] = {'finite': 'Antavā', 'finite view': 'Antavādiṭṭhi', 'infinite': 'anantavā',
                   'infinite view': 'anantavādiṭṭhi', 'view': 'diṭṭhi'}
M['2-898'] = mg(VIEWG, {'finite': 'Antavā', 'infinite': 'Anantavā', 'things': NDE, 'view that things': 'antavādiṭṭhi'})
M['2-17-3-9-0'] = {'speculation': 'ānudiṭṭhi'}
M['2-899'] = mg(VIEWG, {'arises': 'uppajjati', 'concerning': 'ārabbha', 'speculation': 'ānudiṭṭhi',
                        'view that arises': 'uppajjati diṭṭhi'})
M['2-17-3-10-0'] = {'dread': 'anottappañca', 'lack': 'anottappañca', 'lack of moral': 'anottappañca',
                    'Lack of moral': 'anottappañca', 'moral': 'anottappañca', 'shamelessness': 'Ahirikañca'}
M['2-900'] = {
 'ashamed': 'hirīyati', 'dread': 'ottappati', 'dreading': 'ottappati', 'evil': 'pāpakānaṃ', 'lack': 'anottappaṃ',
 'lack of moral': 'anottappaṃ', 'Lack of moral': 'anottappaṃ', 'moral': 'anottappaṃ', 'shamelessness': 'ahirikaṃ',
 'taking': 'samāpattiyā', 'therein': 'tattha', 'things': 'dhammānaṃ', 'unwholesome': 'akusalānaṃ',
 'unwholesome things': 'akusalānaṃ dhammānaṃ'}
M['2-17-3-11-0'] = {'correct': 'Dovacassatā', 'evil': 'pāpa', 'evil friendship': 'pāpamittatā',
                    'Evil friendship': 'pāpamittatā', 'friendship': 'mittatā', 'hard': 'Dovacassatā',
                    'hard to correct': 'Dovacassatā'}
M['2-901'] = {
 'accordance': 'Sahadhammike', 'addressed': 'vuccamāne', 'associating': 'bhajanā', 'bad': 'dussīlā',
 'bad conduct': 'dussīlā', 'conduct': 'dussīlā', 'confidence': 'assaddhā', 'contrary': 'vippaṭikula',
 'correct': 'dovacassatā', 'correcting': 'dovacassiyaṃ', 'deference': 'appatissavatā', 'delight': 'sātatā',
 'devotion': 'bhatti', 'difficulty': 'dovacassiyaṃ', 'disrespect': 'anādariyaṃ', 'disrespectfulness': 'anādaratā',
 'evil': 'pāpa', 'Evil friendship': 'pāpamittatā', 'evil friendship': 'pāpamittatā', 'frequenting': 'nisevanā',
 'friendship': 'mittatā', 'fully': 'sambhajanā', 'grasping': 'ggāhitā', 'hard': 'dovacassatā',
 'hard to correct': 'dovacassatā', 'inclined': 'sampavaṅkatā', 'lack': 'agāravatā',
 'lack of deference': 'appatissavatā', 'lack of reverence': 'agāravatā', 'learning': 'appassutā',
 'opposition': 'vipaccanīka', 'persons': 'puggalā', 'resorting': 'sevanā', 'reverence': 'agāravatā',
 'speak': 'dovacassāyaṃ', 'stingy': 'maccharino', 'teaching': 'Sahadhammike', 'therein': 'tattha', 'towards': NDE,
 'wisdom': 'duppaññā'}
M['2-17-3-12-0'] = {'crookedness': 'Anajjavo', 'harshness': 'amaddavo'}
M['2-902'] = {
 'crooked': 'anajjavatā', 'crookedness': 'anajjavo', 'deviousness': 'jimhatā', 'hardness': 'kakkhaḷiyaṃ',
 'harshness': 'amaddavatā', 'mind': 'cittatā', 'rigidity': 'kakkhaḷatā', 'roughness': 'phārusiyaṃ',
 'stiffness': 'kaṭhinatā', 'therein': 'tattha', 'twistedness': 'vaṅkatā', 'unpliability': 'amudutā',
 'unyieldingness': 'ujucittatā', 'windingness': 'kuṭilatā'}
M['2-17-3-13-0'] = {'immoderation': 'asoraccañca', 'impatience': 'Akkhanti'}
M['2-903'] = {
 'bad': 'dussīlyaṃ', 'bad conduct': 'dussīlyaṃ', 'body': 'Kāyiko', 'conduct': 'dussīlyaṃ',
 'dissatisfaction': 'anattamanatā', 'enduring': 'anadhivāsanatā', 'fierceness': 'caṇḍikkaṃ',
 'immoderation': 'asoraccaṃ', 'impatience': 'akkhanti', 'impatient': 'akkhamanatā', 'mind': 'cittassa',
 'rudeness': 'asuropo', 'speech': 'vācasiko', 'therein': 'tattha', 'transgression': 'vītikkamo'}
M['2-17-3-14-0'] = {'hospitality': 'appaṭisanthāro', 'lack': 'appaṭisanthāro', 'lack of hospitality': 'appaṭisanthāro',
                    'rough': 'Asākhalyañca', 'Rough speech': 'Asākhalyañca', 'speech': 'Asākhalyañca'}
M['2-904'] = {
 'anger': 'kodha', 'bitter': 'kaṭukā', 'bordering': 'sāmantā', 'concentration': 'samādhi',
 'conducive': 'saṃvattanikā', 'harshness': 'pharusavācatā', 'hospitality': 'paṭisanthārā', 'kinds': NDE,
 'lack': 'appaṭisanthāro', 'lack of hospitality': 'appaṭisanthāro', 'material': 'āmisa',
 'offensive': 'ābhisajjanī', 'others': 'para', 'prickly': 'kaṇḍakā', 'rough': 'kakkasā',
 'Rough speech': 'asākhalyaṃ', 'shows': 'appaṭisanthārako', 'someone': 'ekacco', 'speaker': 'bhāsitā',
 'speech': 'vācā', 'teaching': 'dhamma', 'therein': 'tattha', 'things': NDE, 'ungentleness': 'asaṇhavācatā',
 'unkindness': 'asakhilavācatā', 'whatever': 'Yā'}
M['2-17-3-15-0'] = {
 'doors': 'aguttadvāratā', 'faculties': 'Indriyesu', 'food': 'bhojane', 'guarding': 'aguttadvāratā',
 'guarding the doors': 'aguttadvāratā', 'knowing': 'amattaññutā', 'knowing moderation': 'amattaññutā',
 'moderation': 'amattaññutā', 'moderation in food': 'bhojane amattaññutā'}
M['2-905'] = mg(M['2-17-3-15-0'], {
 'adornment': 'maṇḍanāya', 'amusement': 'davāya', 'beautification': 'vibhūsanāya', 'body': 'kāyena',
 'contentment': 'asantuṭṭhitā', 'covetousness': 'abhijjhā', 'covetousness and grief': 'abhijjhādomanassā',
 'dwelt': 'viharantaṃ', 'ear': 'Sotena', 'evil': 'pāpakā', 'eye': 'cakkhunā', 'eye faculty': 'cakkhundriyaṃ',
 'faculties': 'indriyānaṃ', 'faculty': 'indriyaṃ', 'faculty unrestrained': 'indriyaṃ asaṃvutaṃ',
 'flow': 'anvāssaveyyuṃ', 'food': 'āhāraṃ', 'grasps': 'ggāhī', 'grief': 'domanassā', 'guard': 'rakkhati',
 'guarding': 'agutti', 'having': NDE, 'heard': 'sutvā', 'intoxication': 'madāya', 'known': 'viññāya',
 'lack': 'agutti', 'mental': 'dhammaṃ', 'mental object': 'dhammaṃ', 'mind': 'manasā', 'mind faculty': 'manindriyaṃ',
 'mind faculty unrestrained': 'manindriyaṃ asaṃvutaṃ', 'nose': 'ghānena', 'object': 'dhammaṃ',
 'practise': 'paṭipajjati', 'protection': 'agopanā', 'reflection': 'appaṭisaṅkhā', 'regard': NDE,
 'restraint': 'saṃvarāya', 'sight': 'rūpaṃ', 'signs': 'nimitta', 'smell': 'gandhaṃ', 'smelled': 'ghāyitvā',
 'someone': 'ekacco', 'sound': 'saddaṃ', 'takes': 'āhāreti', 'tangible': 'phoṭṭhabbaṃ',
 'tangible thing': 'phoṭṭhabbaṃ', 'taste': 'rasaṃ', 'tasted': 'sāyitvā', 'therein': 'tattha', 'thing': 'phoṭṭhabbaṃ',
 'things': 'dhammā', 'tongue': 'jivhāya', 'touched': 'phusitvā', 'undertake': 'āpajjati',
 'undertake restraint': 'saṃvaraṃ āpajjati', 'unrestrained': 'asaṃvutaṃ', 'unwholesome': 'akusalā',
 'unwholesome things': 'akusalā dhammā', 'unwisely': 'ayoniso', 'watching': 'anārakkho'})
M['2-17-3-16-0'] = {
 'clear': 'asampajaññañca', 'clear comprehension': 'asampajaññañca', 'comprehension': 'asampajaññañca',
 'forgetfulness': 'Muṭṭhassaccañca', 'lack': 'asampajaññañca', 'lack of clear': 'asampajaññañca',
 'Lack of clear': 'asampajaññañca'}
M['2-906'] = mg(IGN, {
 'absence': 'assati', 'away': 'pilāpanatā', 'bearing': 'adhāraṇatā', 'clear': 'asampajaññaṃ',
 'clear comprehension': 'asampajaññaṃ', 'comprehension': 'asampajaññaṃ', 'floating': 'pilāpanatā',
 'forgetfulness': 'muṭṭhassaccaṃ', 'forgetting': 'sammusanatā', 'lack': 'asampajaññaṃ',
 'lack of clear': 'asampajaññaṃ', 'Lack of clear': 'asampajaññaṃ', 'mind': NDE, 'mindfulness': 'assati',
 'recollection': 'ananussati', 'remembering': 'appaṭissati'})
M['2-17-3-17-0'] = {'failure': 'vipatti', 'failure in view': 'diṭṭhivipatti', 'view': 'diṭṭhi', 'virtue': 'Sīla'}
M['2-907'] = mg(VIEWG, {
 'ascetics': NDE, 'bad': 'dussīlyaṃ', 'bad conduct': 'dussīlyaṃ', 'body': 'kāyiko', 'brahmins': NDE,
 'conduct': 'dussīlyaṃ', 'declare': 'pavedentī', 'direct': 'abhiññā', 'direct knowledge': 'abhiññā',
 'failure': 'vipatti', 'failure in view': 'diṭṭhivipatti', 'having': NDE, 'knowledge': 'abhiññā', 'nothing': 'Natthi',
 'practice': NDE, 'realised': 'sacchikatvā', 'right': NDE, 'speech': 'vācasiko', 'themselves': 'sayaṃ',
 'transgression': 'vītikkamo', 'virtue': 'sīla', 'wrong': 'micchā', 'wrong view': 'micchādiṭṭhi',
 'Wrong view': 'micchādiṭṭhi'})
M['2-17-3-18-0'] = {'external': 'bahiddhā', 'fetter': 'saṃyojanañca', 'internal': 'Ajjhatta'}
M['2-908'] = {'external': 'bahiddhā', 'fetter': 'saṃyojanaṃ', 'fetters': 'saṃyojanāni', 'internal': 'ajjhatta',
              'therein': 'tattha', 'twos': 'Dukaṃ'}

# ---------------------------------------------------------------- exposition of the threes
M['2-17-4-0'] = {'exposition': 'niddeso', 'threes': 'Tika'}
M['2-17-4-1-0'] = {'roots': 'mūlāni', 'unwholesome': 'akusala', 'unwholesome roots': 'akusalamūlāni'}
M['2-909'] = mg(IGN, {
 'act': 'āsīsanā', 'affection': 'sineho', 'allure': 'ejā', 'anger': 'kopo', 'angered': 'pakopo',
 'arisen': 'samuppannesu', 'arises': 'jāyati', 'aspiration': 'paṇidhi', 'attachment': 'saṅgo', 'attraction': 'anurodho',
 'begetter': 'janikā', 'bond': 'bandhanaṃ', 'cessation': 'nirodha', 'cessation of suffering': 'dukkhanirodhe',
 'children': 'puttāsā', 'clinging': 'upādānaṃ', 'companion': 'dutiyā', 'compliance': 'anunayo',
 'conditionality': 'idappaccayatā', 'corruption': 'upakkileso', 'covering': 'chadanaṃ', 'covetousness': 'abhijjhā',
 'craving': 'taṇhā', 'craving for cessation': 'nirodhataṇhā', 'craving for existence': 'bhavataṇhā',
 'Craving for material': 'rūpataṇhā', 'craving for material': 'rūpataṇhā',
 'craving for non-existence': 'vibhavataṇhā', 'craving for sense': 'kāmataṇhā', 'creeper': 'latā', 'dear': 'piyassa',
 'deception': 'māyā', 'delight': 'nandī', 'delight-and-lust': 'nandirāgo', 'dependently': 'paṭicca', 'desire': 'jappā',
 'disliked': 'appiyassa', 'displeasing': 'amanāpassa', 'dissatisfaction': 'anattamanatā', 'doing': 'carati',
 'done': 'acarī', 'envy': 'pihanā', 'excessive': 'abhijappā', 'existence': 'bhava', 'fast': 'ajjhosānaṃ',
 'fierceness': 'caṇḍikkaṃ', 'flood': 'ogho', 'forest': 'vanaṃ', 'form': 'rūpa', 'generator': 'sañjananī',
 'greed': 'lobho', 'greediness': 'loluppaṃ', 'greedy': 'loluppāyanā', 'groundlessly': 'aṭṭhāne', 'harm': 'anatthaṃ',
 'hate': 'doso', 'hating': 'padoso', 'hatred': 'manopadoso', 'hindrance': 'nīvaraṇaṃ', 'hook': 'baḷisaṃ',
 'hostility': 'paṭivirodho', 'immaterial': 'arūpa', 'infatuation': 'mucchā', 'intimacy': 'santhavo',
 'itching': 'pucchañjikatā', 'jungle': 'vanatho', 'kind': 'evarūpo', 'kinship': 'paṭibandhu', 'knowing': 'aññāṇaṃ',
 'leads': 'netti', 'leash': 'gaddulaṃ', 'life': 'jīvitāsā', 'longing': 'nikanti', 'lust': 'rāgo', 'malice': 'byāpatti',
 'malicious': 'byāpajjanā', 'material': 'rūpa', 'material form': 'rūpa', 'meanness': 'vevicchaṃ', 'mental': 'dhamma',
 'mental objects': 'dhamma', 'mind': 'cittassa', 'mire': 'paṅko', 'muttering': 'jappā', 'netter': 'jālinī',
 'nice': 'sādhu', 'non-existence': 'vibhava', 'objects': 'dhamma', 'obsession': 'pariyuṭṭhānaṃ',
 'obstruction': 'āvaraṇaṃ', 'ocean': 'samuddo', 'opposition': 'virodho', 'origin': 'pabhavo',
 'origin of suffering': 'dukkhappabhavo', 'passion': 'sārāgo', 'pleasing': 'manāpassa', 'pleasures': 'kāma',
 'regard': 'apekkhā', 'repugnance': 'paṭighāto', 'resentment': 'āghāto', 'Resentment arises': 'āghāto jāyati',
 'resistance': 'paṭighaṃ', 'river': 'saritā', 'roots': 'mūlāni', 'rudeness': 'asuropo', 'seamstress': 'sibbinī',
 'sense': 'kāma', 'sense pleasures': 'kāma', 'sights': 'rūpāsā', 'smells': 'gandhāsā', 'snare': 'pāso',
 'sounds': 'saddāsā', 'source': 'nidānaṃ', 'specific': 'idappaccayatā', 'spreading': 'visaṭā', 'stream': 'sotaṃ',
 'suffering': 'dukkha', 'tangible': 'phoṭṭhabbāsā', 'tangible things': 'phoṭṭhabbāsā', 'tastes': 'rasāsā',
 'tendency': 'anusayo', 'things': 'dhammesu', 'thorough': 'parigedho', 'tie': 'gantho', 'toiler': 'āyūhanī',
 'underlying': 'anusayo', 'underlying tendency': 'anusayo', 'uneven': 'visama', 'unrighteous': 'adhamma',
 'unwholesome roots': 'akusalamūlāni', 'vine': 'visattikā', 'wealth': 'dhanāsā', 'whatever': 'Yo',
 'wish': 'kamyatā', 'wishing': 'āsā', 'wrath': 'kodho', 'wrathful': 'kujjhanā', 'wrathfulness': 'kujjhitattaṃ',
 'yoke': 'yogo'})
VIT = {
 'connected': 'paṭisaṃyutto', 'connected with sense': 'Kāmapaṭisaṃyutto', 'cruelty': 'vihiṃsā', 'ill': 'byāpāda',
 'intention': 'saṅkappo', 'intention connected': 'paṭisaṃyutto / saṅkappo', 'pleasure': 'Kāma', 'sense': 'Kāma',
 'sense pleasure': 'Kāma', 'therein': 'Tattha', 'thinking': 'takko', 'thought': 'vitakko',
 'thought of cruelty': 'vihiṃsāvitakko', 'thought of ill': 'byāpādavitakko', 'thought of sense': 'Kāmavitakko',
 'unwholesome': 'akusala', 'wrong': 'micchā', 'wrong intention': 'micchāsaṅkappo',
 'wrong intention connected': 'paṭisaṃyutto / micchāsaṅkappo'}
M['2-17-4-2-0'] = {'thoughts': 'vitakkā', 'unwholesome': 'akusala', 'unwholesome thoughts': 'akusalavitakkā'}
M['2-910'] = mg(VIT, {'thoughts': 'vitakkā', 'unwholesome thoughts': 'akusalavitakkā'})
M['2-17-4-3-0'] = {'perceptions': 'saññā', 'unwholesome': 'akusala', 'unwholesome perceptions': 'akusalasaññā'}
M['2-911'] = {
 'connected': 'paṭisaṃyuttā', 'connected with sense': 'Kāmapaṭisaṃyuttā', 'cruelty': 'vihiṃsā', 'having': NDE,
 'ill': 'byāpāda', 'perceived': 'sañjānitattaṃ', 'perceiving': 'sañjānanā', 'perception': 'saññā',
 'perception of sense': 'Kāmasaññā', 'perceptions': 'saññā', 'pleasure': 'Kāma', 'sense': 'Kāma',
 'sense pleasure': 'Kāma', 'therein': 'Tattha', 'unwholesome': 'akusala', 'unwholesome perceptions': 'akusalasaññā'}
M['2-17-4-4-0'] = {'elements': 'dhātuyo', 'unwholesome': 'akusala', 'unwholesome elements': 'akusaladhātuyo'}
M['2-912'] = mg(VIT, {
 'element': 'dhātu', 'element of cruelty': 'vihiṃsādhātu', 'element of ill': 'byāpādadhātu',
 'element of sense': 'Kāmadhātu', 'elements': 'dhātuyo', 'unwholesome elements': 'akusaladhātuyo'})
M['2-17-4-5-0'] = {'kinds': NDE, 'kinds of misconduct': 'duccaritāni', 'misconduct': 'duccaritāni'}
M['2-913'] = {
 'beings': 'Pāṇātipāto', 'bodily': 'Kāya', 'bodily action': 'kāyakammaṃ', 'bodily misconduct': 'Kāyaduccaritaṃ',
 'Bodily misconduct': 'Kāyaduccaritaṃ', 'chatter': 'samphappalāpo', 'covetousness': 'Abhijjhā',
 'divisive': 'pisuṇā', 'false': 'Musā', 'false speech': 'Musāvādo', 'harsh': 'pharusā', 'idle': 'samphappalāpo',
 'ill': 'byāpādo', 'intention': 'sañcetanā', 'killing': 'ātipāto', 'killing living': 'Pāṇātipāto', 'kinds': NDE,
 'kinds of misconduct': 'duccaritāni', 'living': 'Pāṇātipāto', 'mental': 'mano', 'mental action': 'manokammaṃ',
 'mental misconduct': 'manoduccaritaṃ', 'misconduct': 'duccaritāni', 'sexual': 'kāmesu', 'speech': 'vācā',
 'taking': 'ādānaṃ', 'therein': 'Tattha', 'unwholesome': 'Akusalaṃ', 'Unwholesome bodily': 'Akusalaṃ kāyakammaṃ',
 'unwholesome bodily': 'Akusalaṃ kāyakammaṃ', 'unwholesome bodily action': 'Akusalaṃ kāyakammaṃ',
 'Unwholesome bodily action': 'Akusalaṃ kāyakammaṃ', 'unwholesome mental': 'akusalaṃ manokammaṃ',
 'unwholesome mental action': 'akusalaṃ manokammaṃ', 'unwholesome verbal': 'akusalaṃ vacīkammaṃ', 'verbal': 'vacī',
 'verbal action': 'vacīkammaṃ', 'verbal misconduct': 'vacīduccaritaṃ', 'view': 'diṭṭhi', 'wrong': 'micchā',
 'wrong view': 'micchādiṭṭhi', 'Wrong view': 'micchādiṭṭhi'}
M['2-17-4-6-0'] = {'mental': 'āsavā', 'mental taints': 'āsavā', 'taints': 'āsavā'}
M['2-914'] = mg(IGN, EXIST, {
 'craving for sense': 'kāmataṇhā', 'knowing': 'aññāṇaṃ', 'mental': 'āsavā', 'mental taints': 'āsavā',
 'pleasure': 'kāma', 'pleasures': 'kāmesu', 'sense': 'kāma', 'sense pleasure': 'kāma', 'sense pleasures': 'kāmesu',
 'suffering': 'Dukkhe', 'taint': 'āsavo', 'taint of existence': 'bhavāsavo', 'taint of ignorance': 'avijjāsavo',
 'taint of sense': 'Kāmāsavo', 'taints': 'āsavā', 'therein': 'Tattha'})
M['2-17-4-7-0'] = {'fetters': 'saṃyojanāni'}
M['2-915'] = mg(VIEWG, {
 'arisen': 'samuppannesu', 'ascetics': 'samaṇa', 'body': 'Sakkāya', 'brahmins': 'brāhmaṇānaṃ', 'comes': NDE,
 'conditionality': 'idappaccayatā', 'confusion': 'manovilekho', 'consciousness': 'viññāṇaṃ', 'dependently': 'paṭicca',
 'doubt': 'vicikicchā', 'doubting': 'kaṅkhāyanā', 'doubts': 'kaṅkhati', 'feeling': 'Vedanaṃ', 'fetters': 'saṃyojanāni',
 'form': 'rūpaṃ', 'formations': 'saṅkhāre', 'grasping': 'parāmāso', 'material': 'rūpaṃ', 'material form': 'rūpaṃ',
 'mental': 'mano', 'mind': 'cittassa', 'noble': 'ariyānaṃ', 'observances': 'vatena', 'ones': 'ariyānaṃ',
 'order': 'saṅghe', 'ordinary': 'puthujjano', 'ordinary person': 'puthujjano', 'outside': 'bahiddhā',
 'people': 'purisānaṃ', 'perception': 'saññaṃ', 'perplexed': 'vicikicchati', 'person': 'puthujjano',
 'possessing': 'vantaṃ', 'purity': 'suddhi', 'regard': 'adassāvī', 'regards': 'samanupassati',
 'regards material form': 'rūpaṃ attato samanupassati', 'rigidity': 'thambhitattaṃ', 'self': 'attato',
 'specific': 'idappaccayatā', 'teacher': 'Satthari', 'teaching': 'dhammassa', 'therein': 'Tattha',
 'things': 'dhammesu', 'training': 'sikkhāya', 'unlearned': 'assutavā', 'unskilled': 'akovido',
 'untrained': 'avinīto', 'virtue': 'sīlena', 'virtue-and-observances': 'sīlabbatena', 'whatever': 'Yā',
 'wrong': 'parāmāso', 'wrong grasping': 'parāmāso'})
CRAV = {
 'connected': 'paṭisaṃyutto', 'craving': 'taṇhā', 'cravings': 'taṇhā', 'element': 'dhātu', 'form': 'Rūpa',
 'immaterial': 'arūpa', 'lust': 'rāgo', 'material': 'Rūpa', 'material form': 'Rūpa', 'mind': 'cittassa',
 'mind connected': 'paṭisaṃyutto / cittassa', 'passion': 'sārāgo', 'therein': 'Tattha'}
M['2-17-4-8-0'] = {'cravings': 'taṇhā'}
M['2-916'] = mg(CRAV, {
 'accompanied': 'sahagato', 'annihilationist': 'Uccheda', 'annihilationist view': 'Ucchedadiṭṭhi',
 'craving for existence': 'bhavataṇhā', 'craving for non-existence': 'vibhavataṇhā', 'craving for sense': 'Kāmataṇhā',
 'element of sense': 'Kāmadhātu', 'existence': 'bhava', 'mind accompanied': 'sahagato / cittassa',
 'non-existence': 'vibhava', 'pleasure': 'Kāma', 'pleasures': 'Kāma', 'remaining': 'Avasesā', 'sense': 'Kāma',
 'sense pleasure': 'Kāma', 'sense pleasures': 'Kāma', 'view': 'diṭṭhi', 'view of existence': 'Bhavadiṭṭhi'})
M['2-17-4-9-0'] = {'cravings': 'taṇhā'}
M['2-917'] = mg(CRAV, {
 'Craving for material': 'rūpataṇhā', 'craving for material': 'rūpataṇhā', 'craving for sense': 'Kāmataṇhā',
 'element of sense': 'Kāmadhātu', 'pleasure': 'Kāma', 'pleasures': 'Kāma', 'sense': 'Kāma', 'sense pleasure': 'Kāma',
 'sense pleasures': 'Kāma'})
M['2-17-4-10-0'] = {'cravings': 'taṇhā'}
M['2-918'] = mg(CRAV, {
 'accompanied': 'sahagato', 'annihilationist': 'Uccheda', 'annihilationist view': 'Ucchedadiṭṭhi',
 'cessation': 'nirodha', 'craving for cessation': 'nirodhataṇhā', 'Craving for material': 'Rūpataṇhā',
 'craving for material': 'Rūpataṇhā', 'mind accompanied': 'sahagato / cittassa', 'view': 'diṭṭhi'})

M['2-17-4-11-0'] = {'quests': 'esanā'}
M['2-919'] = mg(VIEWG, {
 'bodily': 'kāya', 'bodily action': 'kāyakammaṃ', 'death': 'maraṇā', 'desire': 'chando', 'eternal': 'Sassato',
 'exist': 'hoti', 'exist after death': 'hoti / paraṃ maraṇā', 'existence': 'bhava', 'exists': 'hoti',
 'extremist': 'antaggāhikā', 'extremist view': 'antaggāhikā diṭṭhi', 'fast': 'ajjhosānaṃ',
 'holy': 'brahmacariyesanā', 'holy life': 'brahmacariyesanā', 'life': 'brahmacariyesanā', 'lust': 'rāgo',
 'mental': 'mano', 'mental action': 'manokammaṃ', 'pleasures': 'kāmesu', 'quest': 'esanā',
 'quest for existence': 'bhavesanā', 'quest for sense': 'Kāmesanā', 'quests': 'esanā', 'regard': NDE,
 'sense': 'kāmesu', 'sense pleasures': 'kāmesu', 'stand': 'ekaṭṭhaṃ', 'therein': 'Tattha', 'together': 'tadekaṭṭhaṃ',
 'unwholesome': 'akusalaṃ', 'Unwholesome bodily': 'akusalaṃ kāyakammaṃ',
 'unwholesome bodily': 'akusalaṃ kāyakammaṃ', 'unwholesome bodily action': 'akusalaṃ kāyakammaṃ',
 'Unwholesome bodily action': 'akusalaṃ kāyakammaṃ', 'verbal': 'vacī', 'verbal action': 'vacīkammaṃ'})
M['2-17-4-12-0'] = {'modes': 'vidhā', 'self-ranking': 'vidhā'}
M['2-920'] = {'equal': 'sadisohamasmī', 'mode': 'vidhā', 'modes': 'vidhā', 'self-ranking': 'vidhā',
              'therein': 'Tattha', 'worse': 'hīnohamasmī'}
M['2-17-4-13-0'] = {'fears': 'bhayāni'}
M['2-921'] = {
 'account of birth': 'Jātiṃ paṭicca', 'aging': 'jarā', 'alarm': 'utrāso', 'alarm of mind': 'cetaso utrāso',
 'birth': 'Jāti', 'death': 'maraṇa', 'fear': 'bhayaṃ', 'fearfulness': 'bhayānakaṃ', 'fears': 'bhayāni',
 'horripilation': 'lomahaṃso', 'mind': 'cetaso', 'terror': 'chambhitattaṃ', 'therein': 'Tattha'}
M['2-17-4-14-0'] = {'darknesses': 'tamāni'}
M['2-922'] = {
 'concerning': 'ārabbha', 'confidence': 'sampasīdati', 'darknesses': 'tamāni', 'doubts': 'kaṅkhati',
 'perplexed': 'vicikicchati', 'resolve': 'nādhimuccati', 'settle': 'sampasīdati', 'therein': 'Tattha'}
M['2-17-4-15-0'] = {'grounds': 'āyatanāni', 'sectarian': 'titthāyatanāni'}
M['2-923'] = {
 'ascetic': 'samaṇo', 'brahmin': 'brāhmaṇo', 'cause': 'ahetu', 'caused': 'hetū', 'condition': 'appaccayā',
 'creation': 'nimmāna', 'done': 'kata', 'experiences': 'paṭisaṃvedeti', 'grounds': 'āyatanāni',
 'holds': 'evaṃdiṭṭhī', 'holds this view': 'evaṃdiṭṭhī', 'painful': 'dukkhaṃ',
 'painful nor pleasant': 'adukkhamasukhaṃ', 'person': 'purisapuggalo', 'pleasant': 'sukhaṃ',
 'sectarian': 'titthāyatanāni', 'speaks': 'evaṃvādī', 'supreme': 'issara', 'therein': 'Tattha', 'view': 'diṭṭhī',
 'whatever': 'yaṃ kiñcāyaṃ'}
LHD = {'delusion': 'moho', 'hate': 'doso', 'lust': 'Rāgo', 'therein': 'Tattha'}
M['2-17-4-16-0'] = {'impediments': 'kiñcanā'}
M['2-924'] = mg(LHD, {'impediment': 'kiñcanaṃ', 'impediments': 'kiñcanā'})
M['2-17-4-17-0'] = {'blemishes': 'aṅgaṇāni'}
M['2-U1'] = mg(LHD, {'blemish': 'aṅgaṇaṃ', 'blemishes': 'aṅgaṇāni'})
M['2-17-4-18-0'] = {'stains': 'malāni'}
M['2-U2'] = mg(LHD, {'stain': 'malaṃ', 'stains': 'malāni'})
M['2-17-4-19-0'] = {'unevennesses': 'visamāni'}
M['2-U3'] = mg(LHD, {'unevenness': 'visamaṃ', 'unevennesses': 'visamāni'})
M['2-17-4-20-0'] = {'unevennesses': 'visamāni'}
M['2-U4'] = {'bodily': 'Kāya', 'mental': 'mano', 'therein': 'Tattha', 'unevenness': 'visamaṃ',
             'unevennesses': 'visamāni', 'verbal': 'vacī'}
M['2-17-4-21-0'] = {'fires': 'aggī'}
M['2-U5'] = {'delusion': 'mohaggi', 'fire': 'aggi', 'fires': 'aggī', 'hate': 'dosaggi', 'lust': 'Rāgaggi',
             'therein': 'Tattha'}
M['2-17-4-22-0'] = {'corruptions': 'kasāvā'}
M['2-U6'] = {'corruption': 'kasāvo', 'corruptions': 'kasāvā', 'delusion': 'moha', 'hate': 'dosa', 'lust': 'Rāga',
             'therein': 'Tattha'}
M['2-17-4-23-0'] = {'corruptions': 'kasāvā'}
M['2-U7'] = {'bodily': 'Kāya', 'corruption': 'kasāvo', 'corruptions': 'kasāvā', 'mental': 'mano', 'therein': 'Tattha',
             'verbal': 'vacī'}
M['2-17-4-24-0'] = {'enjoyment': 'assāda', 'view': 'diṭṭhi', 'view of enjoyment': 'assādadiṭṭhi'}
M['2-925'] = {
 'ascetic': 'samaṇo', 'brahmin': 'brāhmaṇo', 'enjoyment': 'assāda', 'fault': 'doso', 'holds': 'evaṃdiṭṭhī',
 'holds this view': 'evaṃdiṭṭhī', 'pleasures': 'kāmesu', 'plunges': 'pātabyataṃ āpajjati', 'sense': 'kāmesu',
 'sense pleasures': 'kāmesu', 'speaks': 'evaṃvādī', 'therein': 'Tattha', 'view': 'diṭṭhi',
 'view of enjoyment': 'assādadiṭṭhi'}
M['2-17-4-25-0'] = {'self': 'attānudiṭṭhi', 'view': 'ānudiṭṭhi'}
M['2-U8'] = mg(VIEWG, {
 'consciousness': 'viññāṇaṃ', 'feeling': 'Vedanaṃ', 'form': 'rūpaṃ', 'formations': 'saṅkhāre', 'kind': 'evarūpā',
 'material': 'rūpaṃ', 'material form': 'rūpaṃ', 'noble': 'ariyānaṃ', 'ones': 'ariyānaṃ', 'ordinary': 'puthujjano',
 'ordinary person': 'puthujjano', 'people': 'purisānaṃ', 'perception': 'saññaṃ', 'person': 'puthujjano',
 'possessing': 'vantaṃ', 'regard': 'adassāvī', 'regards': 'samanupassati',
 'regards material form': 'rūpaṃ attato samanupassati', 'self': 'attānudiṭṭhi', 'teaching': 'dhammassa',
 'therein': 'Tattha', 'unlearned': 'assutavā', 'unskilled': 'akovido', 'untrained': 'avinīto', 'view': 'ānudiṭṭhi',
 'whatever': 'Yā'})
M['2-17-4-26-0'] = {'view': 'diṭṭhi', 'wrong': 'micchā', 'wrong view': 'micchādiṭṭhi', 'Wrong view': 'micchādiṭṭhi'}
M['2-U9'] = mg(VIEWG, {
 'annihilationist': 'uccheda', 'annihilationist view': 'ucchedadiṭṭhi', 'body': 'sakkāya', 'declare': 'pavedentī',
 'direct': 'abhiññā', 'direct knowledge': 'abhiññā', 'enjoyment': 'assāda', 'eternalist': 'Sassata',
 'eternalist view': 'Sassatadiṭṭhi', 'having': NDE, 'knowledge': 'abhiññā', 'nothing': 'Natthi',
 'realised': 'sacchikatvā', 'self': 'attānudiṭṭhi', 'themselves': 'sayaṃ', 'therein': 'Tattha',
 'view of enjoyment': 'assādadiṭṭhi', 'wrong': 'micchā', 'wrong view': 'micchādiṭṭhi', 'Wrong view': 'micchādiṭṭhi'})
M['2-17-4-27-0'] = {'discontent': 'arati'}
M['2-926'] = dict(M['2-856'])
M['2-17-4-28-0'] = {'cruelty': 'vihesā'}
M['2-U10'] = {
 'beings': 'satte', 'clod': 'leḍḍunā', 'cruelty': 'vihesā', 'doing': NDE, 'enraging': 'virosanā', 'hand': 'pāṇinā',
 'harassing': 'viheṭhanā', 'harming': 'heṭhanā', 'harms': 'viheṭheti', 'hurting': 'hiṃsanā', 'injuring': 'vihiṃsanā',
 'kind': 'evarūpā', 'knife': 'satthena', 'others': 'parūpaghāto', 'provoking': 'rosanā', 'rope': 'rajjuyā',
 'someone': 'ekacco', 'stick': 'daṇḍena', 'therein': 'Tattha', 'thing': 'aññataraññatarena',
 'violence': 'ūpaghāto', 'whatever': 'yā'}
M['2-17-4-29-0'] = {'conduct': 'cariyā', 'unrighteous': 'adhamma', 'Unrighteous conduct': 'adhammacariyā'}
M['2-U11'] = {
 'body': 'Kāyena', 'conduct': 'cariyā', 'mind': 'manasā', 'speech': 'vācāya', 'therein': 'Tattha', 'uneven': 'visama',
 'uneven conduct': 'visamacariyā', 'unrighteous': 'adhamma', 'Unrighteous conduct': 'adhammacariyā'}
HARD = {'correct': 'dovacassatā', 'hard': 'dovacassatā', 'hard to correct': 'dovacassatā'}
EVILF = {'evil': 'pāpa', 'Evil friendship': 'pāpamittatā', 'evil friendship': 'pāpamittatā', 'friendship': 'mittatā'}
M['2-17-4-30-0'] = dict(HARD)
M['2-927'] = mg(M['2-901'], therein='Tattha')
M['2-17-4-31-0'] = dict(EVILF)
M['2-U12'] = mg(M['2-901'], therein='Tattha')
M['2-17-4-32-0'] = {'diversity': 'nānatta', 'perception': 'saññā', 'Perception of diversity': 'nānattasaññā'}
M['2-U13'] = {
 'cruelty': 'vihiṃsā', 'diversity': 'nānatta', 'ill': 'byāpāda', 'perception': 'saññā',
 'Perception of diversity': 'nānattasaññā', 'perception of sense': 'Kāmasaññā', 'pleasure': 'Kāma', 'sense': 'Kāma',
 'sense pleasure': 'Kāma', 'therein': 'Tattha', 'unwholesome': 'akusalā', 'Unwholesome perception': 'akusalā saññā',
 'unwholesome perception': 'akusalā saññā'}
RESTL = {
 'agitation': 'bhantattaṃ', 'calm': 'avūpasamo', 'distraction': 'vikkhepo', 'lack': 'avūpasamo',
 'lack of calm': 'avūpasamo', 'mental': 'cetaso', 'mental distraction': 'cetaso vikkhepo', 'mind': 'cittassa',
 'restlessness': 'uddhaccaṃ', 'therein': 'Tattha'}
M['2-17-4-33-0'] = {'restlessness': 'uddhaccaṃ'}
M['2-928'] = dict(RESTL)
M['2-17-4-34-0'] = {'laziness': 'kosajjaṃ'}
# the later heedlessness/laziness definitions read 'kusalānaṃ dhammānaṃ' (no vā)
HEED2 = mg(M['2-846'], {'wholesome things': 'kusalānaṃ dhammānaṃ'})
M['2-U14'] = mg(HEED2, laziness='kosajjaṃ')
M['2-17-4-35-0'] = {'heedlessness': 'pamādo'}
M['2-U15'] = dict(HEED2)
M['2-17-4-36-0'] = {'discontentment': 'asantuṭṭhitā'}
M['2-929'] = mg(WANT, discontentment='asantuṭṭhitā')
CLEAR_T = {'clear': 'asampajaññatā', 'clear comprehension': 'asampajaññatā', 'comprehension': 'asampajaññatā',
           'lack': 'asampajaññatā', 'lack of clear': 'asampajaññatā', 'Lack of clear': 'asampajaññatā'}
M['2-17-4-37-0'] = dict(CLEAR_T)
M['2-U16'] = mg(IGN, CLEAR_T, therein='Tattha')
M['2-17-4-38-0'] = {'desire': 'icchatā', 'great desire': 'mahicchatā', 'Great desire': 'mahicchatā'}
M['2-U17'] = dict(M['2-850'])
M['2-17-4-39-0'] = {'shamelessness': 'ahirikaṃ'}
M['2-930'] = mg(M['2-900'], therein='Tattha')
M['2-17-4-40-0'] = {'dread': 'anottappaṃ', 'lack': 'anottappaṃ', 'lack of moral': 'anottappaṃ',
                    'Lack of moral': 'anottappaṃ', 'moral': 'anottappaṃ'}
M['2-U18'] = mg(M['2-900'], therein='Tattha')
M['2-17-4-41-0'] = {'heedlessness': 'pamādo'}
M['2-U19'] = dict(HEED2)
M['2-17-4-42-0'] = {'disrespect': 'anādariyaṃ'}
M['2-931'] = {
 'absence': 'anaddāyanā', 'consideration': 'acittīkāro', 'deference': 'appatissavatā', 'disrespect': 'anādariyaṃ',
 'disrespectfulness': 'anādaratā', 'having': NDE, 'lack': 'agāravatā', 'lack of deference': 'appatissavatā',
 'lack of reverence': 'agāravatā', 'regard': 'anaddā', 'reverence': 'agāravatā', 'therein': 'Tattha',
 'virtue': 'asīlyaṃ'}
M['2-17-4-43-0'] = dict(HARD)
M['2-U20'] = dict(M['2-927'])
M['2-17-4-44-0'] = dict(EVILF)
M['2-U21'] = mg(M['2-U12'], attending='paṭisevanā')
M['2-17-4-45-0'] = {'confidence': 'assaddhiyaṃ', 'lack': 'assaddhiyaṃ', 'Lack of confidence': 'assaddhiyaṃ'}
M['2-932'] = {
 'absence': 'assaddahanā', 'buddha': 'buddhaṃ', 'confidence': 'saddahati', 'kind': 'evarūpaṃ', 'lack': 'assaddhiyaṃ',
 'Lack of confidence': 'assaddhiyaṃ', 'order': 'saṅghaṃ', 'reliance': 'anokappanā', 'someone': 'ekacco',
 'teaching': 'dhammaṃ', 'therein': 'Tattha', 'trusting': 'assaddahanā', 'whatever': 'yaṃ'}
M['2-17-4-46-0'] = {'uncharitableness': 'avadaññutā'}
M['2-U22'] = mg(M['2-893'], therein='Tattha', uncharitableness='avadaññutā')
M['2-17-4-47-0'] = {'laziness': 'kosajjaṃ'}
M['2-U23'] = dict(M['2-U14'])
M['2-17-4-48-0'] = {'restlessness': 'uddhaccaṃ'}
M['2-933'] = mg(RESTL, agitation='bhavantattaṃ')
M['2-17-4-49-0'] = {'non-restraint': 'asaṃvaro'}
M['2-U24'] = mg(M['2-905'], {'non-restraint': 'asaṃvaro', 'therein': 'Tattha'})
CONDUCT = {'bad': 'dussīlyaṃ', 'bad conduct': 'dussīlyaṃ', 'conduct': 'dussīlyaṃ'}
M['2-17-4-50-0'] = dict(CONDUCT)
M['2-U25'] = mg(CONDUCT, {'body': 'Kāyiko', 'speech': 'vācasiko', 'therein': 'Tattha', 'transgression': 'vītikkamo'})
M['2-17-4-51-0'] = {'noble': 'ariyānaṃ', 'ones': 'ariyānaṃ', 'wishing': 'kamyatā'}
M['2-934'] = {
 'behold': 'adaṭṭhukamyatā', 'buddhas': 'buddhā', 'disciples': 'sāvakā', 'noble': 'ariyānaṃ', 'ones': 'ariyānaṃ',
 'therein': 'Tattha', 'together': 'asamāgantukamyatā', 'wishing': 'kamyatā'}
GOOD = {'good teaching': 'saddhammaṃ', 'hear': 'asotukamyatā', 'teaching': 'saddhammaṃ', 'wishing': 'kamyatā',
        'wishing to hear': 'asotukamyatā'}
M['2-17-4-52-0'] = dict(GOOD)
M['2-U26'] = mg(GOOD, {
 'awakening': 'bojjhaṅgā', 'Awakening Factors': 'bojjhaṅgā', 'awakening factors': 'bojjhaṅgā', 'bases': 'pādā',
 'bases of success': 'iddhipādā', 'Bases of Success': 'iddhipādā', 'efforts': 'padhānā', 'eightfold': 'aṭṭhaṅgiko',
 'eightfold path': 'aṭṭhaṅgiko maggo', 'factors': 'bojjhaṅgā', 'faculties': 'indriyāni', 'foundations': 'paṭṭhānā',
 'foundations of mindfulness': 'satipaṭṭhānā', 'learn': 'anuggahetukamyatā', 'listen': 'asavanakamyatā',
 'mindfulness': 'sati', 'noble': 'ariyo', 'path': 'maggo', 'powers': 'balāni', 'retain': 'adhāretukamyatā',
 'right': 'sammappadhānā', 'success': 'iddhi', 'therein': 'Tattha'})
M['2-17-4-53-0'] = {'fault-finding': 'upārambha', 'fault-finding mind': 'upārambhacittatā', 'mind': 'cittatā'}
M['2-U27'] = {
 'constant': 'anupārambho', 'constantly': 'anupārambhanā', 'contempt': 'uññā', 'disparagement': 'paribhavo',
 'fault': 'upārambho', 'fault-finder': 'upārambhanā', 'fault-finding': 'upārambho',
 'fault-finding mind': 'upārambhacittatā', 'finding': 'anupārambhanā', 'mind': 'cittatā', 'points': 'randha',
 'scorn': 'avaññā', 'therein': 'Tattha', 'weak': 'randha'}
M['2-17-4-54-0'] = {'forgetfulness': 'muṭṭhassaccaṃ'}
M['2-935'] = {
 'absence': 'assati', 'away': 'pilāpanatā', 'bearing': 'adhāraṇatā', 'floating': 'pilāpanatā',
 'forgetfulness': 'muṭṭhassaccaṃ', 'forgetting': 'sammusanatā', 'mind': NDE, 'mindfulness': 'assati',
 'recollection': 'ananussati', 'remembering': 'appaṭissati', 'therein': 'Tattha'}
CLEAR_M = {'clear': 'asampajaññaṃ', 'clear comprehension': 'asampajaññaṃ', 'comprehension': 'asampajaññaṃ',
           'lack': 'asampajaññaṃ', 'lack of clear': 'asampajaññaṃ', 'Lack of clear': 'asampajaññaṃ'}
M['2-17-4-55-0'] = dict(CLEAR_M)
M['2-U28'] = mg(IGN, CLEAR_M, therein='Tattha')
M['2-17-4-56-0'] = {'distraction': 'vikkhepo', 'Distraction of mind': 'cetaso vikkhepo', 'mind': 'cetaso'}
M['2-U29'] = mg(RESTL, {'Distraction of mind': 'cetaso vikkhepo'})
M['2-17-4-57-0'] = {'attention': 'manasikāro', 'unwise': 'ayoniso', 'Unwise attention': 'ayoniso manasikāro'}
M['2-936'] = {
 'attention': 'manasikāro', 'attention taking': 'manasikāro', 'attractive': 'subha', 'bringing-to-mind': 'samannāhāro',
 'contrary': 'vippaṭikulena', 'engagement': 'ābhogo', 'impermanent': 'Anicce', 'mind': 'cittassa', 'painful': 'dukkhe',
 'permanent': 'nicca', 'pleasant': 'sukha', 'repeated': 'anāvaṭṭanā', 'self': 'attā', 'taking': NDE,
 'therein': 'Tattha', 'truth': 'sacca', 'turning': 'āvaṭṭanā', 'unattractive': 'asubhe', 'unwise': 'ayoniso',
 'Unwise attention': 'ayoniso manasikāro', 'Unwise attention taking': 'ayoniso manasikāro'}

M['2-17-4-58-0'] = {'path': 'magga', 'wrong': 'kummagga', 'wrong path': 'kummagga'}
M['2-U30'] = {
 'associating': 'bhajanā', 'concentration': 'samādhi', 'devotion': 'bhatti', 'effort': 'vāyāmo',
 'frequenting': 'nisevanā', 'fully': 'sambhajanā', 'inclined': 'taṃsampavaṅkatā', 'intention': 'saṅkappo',
 'livelihood': 'ājīvo', 'mindfulness': 'sati', 'path': 'magga', 'resorting': 'sevanā', 'speech': 'vācā',
 'therein': 'Tattha', 'towards': NDE, 'view': 'diṭṭhi', 'wrong': 'kummagga', 'wrong intention': 'micchāsaṅkappo',
 'wrong path': 'kummaggo', 'wrong view': 'Micchādiṭṭhi', 'Wrong view': 'Micchādiṭṭhi'}
M['2-17-4-59-0'] = {'mind': 'cetaso', 'sluggishness': 'līnattaṃ', 'Sluggishness of mind': 'cetaso ca līnattaṃ'}
M['2-U31'] = mg(M['2-860'], {'dull': 'thiyanā', 'threes': 'Tikaṃ'})

# ---------------------------------------------------------------- exposition of the fours
M['2-17-5-0'] = {'exposition': 'niddeso', 'fours': 'Catukka'}
M['2-17-5-1-0'] = {'mental': 'āsavā', 'mental taints': 'āsavā', 'taints': 'āsavā'}
M['2-937'] = {
 'existence': 'bhavāsavo', 'ignorance': 'avijjāsavo', 'mental': 'āsavā', 'mental taints': 'āsavā',
 'pleasure': 'Kāmāsavo', 'sense': 'Kāmāsavo', 'sense pleasure': 'Kāmāsavo', 'taint': 'āsavo',
 'taint of existence': 'bhavāsavo', 'taint of ignorance': 'avijjāsavo', 'taint of sense': 'Kāmāsavo',
 'taint of views': 'diṭṭhāsavo', 'taints': 'āsavā', 'therein': 'Tattha', 'views': 'diṭṭhāsavo'}
M['2-17-5-2-0'] = {'pleasure': 'kāmāsavo', 'sense': 'kāmāsavo', 'sense pleasure': 'kāmāsavo', 'taint': 'āsavo',
                   'taint of sense': 'kāmāsavo'}
M['2-U32'] = mg(EXIST, {
 'craving for sense': 'kāmataṇhā', 'pleasure': 'kāma', 'pleasures': 'kāmesu', 'sense': 'kāma', 'sense pleasure': 'kāma',
 'sense pleasures': 'kāmesu', 'taint': 'āsavo', 'taint of sense': 'kāmāsavo', 'therein': 'Tattha'})
M['2-17-5-3-0'] = {'existence': 'bhavāsavo', 'taint': 'āsavo', 'taint of existence': 'bhavāsavo'}
M['2-U33'] = {'desire': 'chando', 'existence': 'bhava', 'fast': 'ajjhosānaṃ', 'regard': NDE, 'taint': 'āsavo',
              'taint of existence': 'bhavāsavo', 'therein': 'Tattha'}
M['2-17-5-4-0'] = {'taint': 'āsavo', 'taint of views': 'diṭṭhāsavo', 'views': 'diṭṭhāsavo'}
M['2-U34'] = mg(VIEWG, {
 'body': 'sarīra', 'death': 'maraṇā', 'eternal': 'Sassato', 'exist': 'hoti', 'exist after death': 'hoti / paraṃ maraṇā',
 'exists': 'hoti', 'finite': 'antavā', 'infinite': 'anantavā', 'soul': 'jīvaṃ', 'taint': 'āsavo',
 'taint of views': 'diṭṭhāsavo', 'Tathāgata exists': 'hoti tathāgato', 'therein': 'Tattha', 'thing': NDE,
 'views': 'diṭṭhāsavo', 'whatever': 'Yā', 'wrong': 'micchā', 'wrong view': 'micchādiṭṭhi',
 'Wrong view': 'micchādiṭṭhi'})
M['2-17-5-5-0'] = {'ignorance': 'avijjāsavo', 'taint': 'āsavo', 'taint of ignorance': 'avijjāsavo'}
M['2-U35'] = mg(IGN, {
 'arisen': 'samuppannesu', 'cessation': 'nirodhe', 'cessation of suffering': 'dukkhanirodhe',
 'conditionality': 'idappaccayatā', 'dependently': 'paṭicca', 'ignorance': 'avijjāsavo', 'kind': 'evarūpaṃ',
 'knowing': 'aññāṇaṃ', 'mental': 'āsavā', 'mental taints': 'āsavā', 'origin': 'samudaye',
 'origin of suffering': 'dukkhasamudaye', 'specific': 'idappaccayatā', 'suffering': 'Dukkhe', 'taint': 'āsavo',
 'taint of ignorance': 'avijjāsavo', 'taints': 'āsavā', 'therein': 'Tattha', 'things': 'dhammesu', 'whatever': 'Yaṃ'})
M['2-17-5-6-0'] = {'rest': 'ādī', 'ties': 'ganthādī'}
M['2-938'] = {
 'clinging': 'upādānāni', 'clinging to rules': 'sīlabbatupādānaṃ', 'Clinging to sense': 'Kāmupādānaṃ',
 'clinging to views': 'diṭṭhupādānaṃ', 'doctrine': 'attavādupādānaṃ', 'floods': 'oghā', 'kinds': NDE,
 'kinds of clinging': 'upādānāni', 'observances': 'sīlabbatupādānaṃ', 'pleasures': 'Kāmupādānaṃ',
 'rules': 'sīlabbatupādānaṃ', 'rules and observances': 'sīlabbatupādānaṃ', 'self': 'attavādupādānaṃ',
 'sense': 'Kāmupādānaṃ', 'sense pleasures': 'Kāmupādānaṃ', 'therein': 'Tattha', 'ties': 'ganthā',
 'views': 'diṭṭhupādānaṃ', 'yokes': 'yogā'}
M['2-17-5-7-0'] = {'clinging': 'upādānaṃ', 'Clinging to sense': 'kāmupādānaṃ', 'pleasures': 'kāmupādānaṃ',
                   'sense': 'kāmupādānaṃ', 'sense pleasures': 'kāmupādānaṃ'}
M['2-U36'] = {'clinging': 'upādānaṃ', 'Clinging to sense': 'kāmupādānaṃ', 'desire': 'chando', 'fast': 'ajjhosānaṃ',
              'pleasures': 'kāmesu', 'regard': NDE, 'sense': 'kāmesu', 'sense pleasures': 'kāmesu',
              'therein': 'Tattha'}
M['2-17-5-8-0'] = {'clinging': 'upādānaṃ', 'clinging to views': 'diṭṭhupādānaṃ', 'views': 'diṭṭhupādānaṃ'}
M['2-U37'] = mg(VIEWG, {
 'aside': 'Ṭhapetvā', 'clinging': 'upādānaṃ', 'clinging to rules': 'sīlabbatupādānañca',
 'clinging to views': 'diṭṭhupādānaṃ', 'declare': 'pavedentī', 'direct': 'abhiññā', 'direct knowledge': 'abhiññā',
 'doctrine': 'attavādupādānañca', 'having': NDE, 'knowledge': 'abhiññā', 'nothing': 'Natthi',
 'observances': 'sīlabbatupādānañca', 'realised': 'sacchikatvā', 'rules': 'sīlabbatupādānañca',
 'rules and observances': 'sīlabbatupādānañca', 'self': 'attavādupādānañca', 'setting': 'Ṭhapetvā',
 'themselves': 'sayaṃ', 'therein': 'Tattha', 'views': 'diṭṭhupādānaṃ', 'whatever': 'Yā', 'wrong': 'micchā',
 'wrong view': 'micchādiṭṭhi', 'Wrong view': 'micchādiṭṭhi'})
RULES = {'clinging': 'upādānaṃ', 'clinging to rules': 'sīlabbatupādānaṃ', 'observances': 'sīlabbatupādānaṃ',
         'rules': 'sīlabbatupādānaṃ', 'rules and observances': 'sīlabbatupādānaṃ'}
M['2-17-5-9-0'] = dict(RULES)
M['2-U38'] = mg(VIEWG, RULES, {
 'ascetics': 'samaṇa', 'brahmins': 'brāhmaṇānaṃ', 'comes': NDE, 'outside': 'bahiddhā', 'purity': 'suddhi',
 'teaching': NDE, 'therein': 'Tattha', 'virtue': 'sīlena', 'virtue-and-observances': 'sīlabbatena', 'whatever': 'Yā'})
M['2-17-5-10-0'] = {'clinging': 'upādānaṃ', 'doctrine': 'attavādupādānaṃ', 'self': 'attavādupādānaṃ'}
M['2-U39'] = mg(M['2-U8'], {
 'clinging': 'upādānaṃ', 'doctrine': 'attavādupādānaṃ', 'kinds': NDE, 'kinds of clinging': 'upādānāni',
 'self': 'attavādupādānaṃ', 'view': 'diṭṭhi'})
M['2-17-5-11-0'] = {'arisings': 'uppādā', 'craving': 'taṇhuppādā'}
M['2-939'] = {
 'alms-food': 'piṇḍapāta', 'arises': 'uppajjati', 'arisings': 'uppādā', 'craving': 'taṇhā', 'dwelling': 'senāsana',
 'dwelling place': 'senāsana', 'monk': 'bhikkhuno', 'place': 'senāsana', 'robes': 'Cīvara', 'therein': 'Tattha'}
M['2-17-5-12-0'] = {'astray': 'agati', 'going': 'gamanāni', 'ways': 'gamanāni'}
M['2-U40'] = {
 'astray': 'āgatiṃ', 'course': 'agatigamanaṃ', 'delusion': 'mohāgatiṃ', 'desire': 'Chandāgatiṃ', 'evasion': 'vāri',
 'faction': 'vagga', 'fear': 'bhayāgatiṃ', 'goes': 'gacchati', 'going': 'gamanāni', 'hate': 'dosāgatiṃ',
 'kind': 'evarūpā', 'therein': 'Tattha', 'ways': 'gamanāni', 'whatever': 'Yā', 'wrong': 'agatigamanaṃ'}
M['2-17-5-13-0'] = {'distortions': 'vipariyāsā'}
M['2-U41'] = {
 'attractive': 'subha', 'distortion': 'vipariyāso', 'distortion of mind': 'cittavipariyāso',
 'distortion of perception': 'saññāvipariyāso', 'distortion of view': 'diṭṭhivipariyāso', 'distortions': 'vipariyāsā',
 'impermanent': 'Anicce', 'mind': 'citta', 'painful': 'dukkhe', 'perception': 'saññā', 'permanent': 'nicca',
 'pleasant': 'sukha', 'self': 'attā', 'taking': NDE, 'therein': 'Tattha', 'unattractive': 'asubhe', 'view': 'diṭṭhi'}
VOHARA = {'ignoble': 'anariya', 'speech': 'vohārā', 'ways': 'vohārā'}
M['2-17-5-14-0'] = dict(VOHARA)
M['2-U42'] = mg(VOHARA, {'heard': 'suta', 'known': 'viññāta', 'sensed': 'muta', 'therein': 'Tattha'})
M['2-17-5-15-0'] = dict(VOHARA)
M['2-U43'] = dict(M['2-U42'])
M['2-17-5-16-0'] = {'kinds': NDE, 'kinds of misconduct': 'duccaritāni', 'misconduct': 'duccaritāni'}
M['2-U44'] = {
 'beings': 'Pāṇātipāto', 'false': 'musā', 'false speech': 'musāvādo', 'killing': 'ātipāto',
 'killing living': 'Pāṇātipāto', 'kinds': NDE, 'kinds of misconduct': 'duccaritāni', 'living': 'Pāṇātipāto',
 'misconduct': 'duccaritāni', 'sexual': 'kāmesu', 'speech': 'vādo', 'taking': 'ādānaṃ', 'therein': 'Tattha'}
M['2-17-5-17-0'] = dict(M['2-17-5-16-0'])
M['2-U45'] = {
 'chatter': 'samphappalāpo', 'divisive': 'pisuṇā', 'false': 'Musā', 'false speech': 'Musāvādo', 'harsh': 'pharusā',
 'idle': 'samphappalāpo', 'kinds': NDE, 'kinds of misconduct': 'duccaritāni', 'misconduct': 'duccaritāni',
 'speech': 'vācā', 'therein': 'Tattha'}
M['2-17-5-18-0'] = {'fears': 'bhayāni'}
M['2-U46'] = {'aging': 'jarā', 'birth': 'Jāti', 'death': 'maraṇa', 'fear': 'bhayaṃ', 'fears': 'bhayāni',
              'sickness': 'byādhi', 'therein': 'Tattha'}
M['2-17-5-19-0'] = {'fears': 'bhayāni'}
M['2-U47'] = {
 'bad': 'duggati', 'bad destination': 'duggati', 'crocodiles': 'kumbhīla', 'destination': 'duggati', 'fear': 'bhayaṃ',
 'fears': 'bhayāni', 'fire': 'aggi', 'kings': 'Rāja', 'others': 'parānuvādabhayaṃ', 'punishment': 'daṇḍa',
 'reproach': 'ānuvāda', 'self-reproach': 'Attānuvāda', 'sharks': 'susukā', 'therein': 'Tattha', 'thieves': 'cora',
 'water': 'udaka', 'waves': 'Ūmi', 'whirlpools': 'āvaṭṭa'}
M['2-17-5-20-0'] = {'views': 'diṭṭhiyo'}
M['2-U48'] = {
 'arisen': 'samuppannaṃ', 'arises': 'uppajjati', 'chance': 'adhicca', 'established': 'thetato', 'fours': 'Catukkaṃ',
 'happiness': 'sukha', 'Happiness and suffering': 'sukhadukkha', 'oneself': 'Sayaṅkataṃ', 'suffering': 'dukkha',
 'therein': 'Tattha', 'true': 'saccato', 'true and established': 'saccato thetato', 'view': 'diṭṭhi',
 'view arises': 'diṭṭhi uppajjati', 'views': 'diṭṭhiyo'}

# ---------------------------------------------------------------- exposition of the fives
M['2-17-6-0'] = {'exposition': 'niddeso', 'fives': 'Pañcaka'}
M['2-17-6-1-0'] = {'fetters': 'saṃyojanāni'}
M['2-940'] = {
 'body': 'Sakkāya', 'desire': 'chando', 'doubt': 'vicikicchā', 'fetters': 'saṃyojanāni', 'grasping': 'parāmāso',
 'ill': 'byāpādo', 'observances': 'sīlabbata', 'self': 'Sakkāya', 'sense': 'kāma', 'sense desire': 'kāmacchando',
 'therein': 'Tattha', 'view': 'diṭṭhi', 'virtue': 'sīla', 'wrong': 'parāmāso', 'wrong grasping': 'parāmāso'}
M['2-17-6-2-0'] = {'fetters': 'saṃyojanāni'}
M['2-U49'] = {
 'conceit': 'māno', 'fetters': 'saṃyojanāni', 'form': 'Rūpa', 'ignorance': 'avijjā', 'immaterial': 'arūpa',
 'lust': 'rāgo', 'material': 'Rūpa', 'material form': 'Rūpa', 'restlessness': 'uddhaccaṃ', 'therein': 'Tattha'}
M['2-17-6-3-0'] = {'kinds': NDE, 'kinds of stinginess': 'macchariyāni', 'stinginess': 'macchariyāni'}
M['2-U50'] = {
 'dwellings': 'Āvāsa', 'families': 'kula', 'kinds': NDE, 'kinds of stinginess': 'macchariyāni', 'praise': 'vaṇṇa',
 'stinginess': 'macchariyāni', 'teaching': 'dhamma', 'therein': 'Tattha'}

LHD5 = {'delusion': 'moha', 'hate': 'dosa', 'lust': 'Rāga', 'therein': 'Tattha', 'conceit': 'māna', 'views': 'diṭṭhi'}
M['2-17-6-4-0'] = {'attachments': 'saṅgā'}
M['2-U51'] = mg(LHD5, {'attachment': 'saṅgo', 'attachments': 'saṅgā'})
M['2-17-6-5-0'] = {'darts': 'sallā'}
M['2-U52'] = mg(LHD5, {'dart': 'sallaṃ', 'darts': 'sallā'})
M['2-17-6-6-0'] = {'barrennesses': 'khilā', 'mind': 'ceto'}
M['2-941'] = {
 'angry': 'kupito', 'barren': 'khilajāto', 'barrennesses': 'khilā', 'companions': 'sabrahmacārīsu',
 'confidence': 'sampasīdati', 'displeased': 'anattamano', 'doubts': 'kaṅkhati', 'holy': 'sabrahmacārīsu',
 'holy life': 'sabrahmacārīsu', 'life': 'sabrahmacārīsu', 'mind': 'ceto', 'order': 'saṅghe',
 'perplexed': 'vicikicchati', 'resolve': 'nādhimuccati', 'settle': 'sampasīdati', 'struck-down': 'āhatacitto',
 'teacher': 'Satthari', 'teaching': 'dhamme', 'therein': 'Tattha', 'training': 'sikkhāya'}
M['2-17-6-7-0'] = {'bondages': 'vinibandhā', 'mind': 'cetaso'}
M['2-U53'] = {
 'affection': 'avigatapemo', 'aspiring': 'paṇidhāya', 'austerity': 'tapena', 'belly': 'udarāvadehakaṃ',
 'body': 'kāye', 'bondages': 'vinibandhā', 'burning': 'avigatapariḷāho', 'craving': 'avigatataṇho',
 'desire': 'avigatacchando', 'devoted': 'anuyutto', 'dwells': 'viharati', 'eaten': 'bhuñjitvā', 'form': 'rūpe',
 'god': 'devo', 'gods': 'deva', 'having': NDE, 'holy': 'brahmacariyaṃ', 'holy life': 'brahmacariyaṃ',
 'life': 'brahmacariyaṃ', 'lives': 'carati', 'lolling': 'passasukhaṃ', 'lust': 'avītarāgo', 'lying': 'seyyasukhaṃ',
 'material': 'rūpe', 'material form': 'rūpe', 'mind': 'cetaso', 'observance': 'vatena', 'order': 'nikāyaṃ',
 'pleasure': 'sukhaṃ', 'pleasures': 'Kāme', 'sense': 'Kāme', 'sense pleasures': 'Kāme', 'sleep': 'middhasukhaṃ',
 'therein': 'Tattha', 'thirst': 'avigatapipāso', 'virtue': 'sīlena'}
M['2-17-6-8-0'] = {'hindrances': 'nīvaraṇāni'}
M['2-U54'] = {
 'desire': 'chanda', 'doubt': 'vicikicchā', 'drowsiness': 'middha', 'dullness': 'thina',
 'dullness and drowsiness': 'thinamiddha', 'hindrance': 'nīvaraṇaṃ', 'hindrances': 'nīvaraṇāni', 'ill': 'byāpāda',
 'remorse': 'kukkucca', 'restlessness': 'uddhacca', 'restlessness and remorse': 'uddhaccakukkucca', 'sense': 'Kāma',
 'sense desire': 'Kāmacchanda', 'therein': 'Tattha'}
M['2-17-6-9-0'] = {'actions': 'kammāni', 'immediate': 'ānantarikāni'}
M['2-U55'] = {
 'actions': 'kammāni', 'arahant': 'arahanto', 'blood': 'lohitaṃ', 'deprived': 'voropitā', 'father': 'pitā',
 'hatred': 'duṭṭhena', 'immediate': 'ānantarikāni', 'life': 'jīvitā', 'mind': 'cittena', 'mother': 'Mātā',
 'order': 'saṅgho', 'shed': 'uppāditaṃ', 'therein': 'Tattha'}
M['2-17-6-10-0'] = {'views': 'diṭṭhiyo'}
M['2-U56'] = {
 'cutting': 'ucchedaṃ', 'death': 'maraṇā', 'declare': 'abhivadanti',
 'declare Nibbāna': 'diṭṭhadhammanibbānaṃ / abhivadanti', 'destruction': 'vināsaṃ', 'existing': 'sato',
 'life': 'diṭṭhadhamma', 'non-existence': 'vibhavaṃ', 'non-percipient': 'asaññī', 'percipient': 'Saññī',
 'percipient nor non-percipient': 'nevasaññīnāsaññī', 'proclaim': 'paññāpenti', 'self': 'attā', 'therein': 'Tattha',
 'unimpaired': 'arogo', 'unimpaired after death': 'arogo paraṃ maraṇā', 'views': 'diṭṭhiyo'}
M['2-17-6-11-0'] = {'hostilities': 'verā'}
M['2-942'] = {
 'beings': 'Pāṇātipāto', 'cause': 'ṭṭhānā', 'false': 'musā', 'false speech': 'musāvādo', 'heedlessness': 'pamāda',
 'hostilities': 'verā', 'intoxicants': 'majja', 'killing': 'ātipāto', 'killing living': 'Pāṇātipāto',
 'living': 'Pāṇātipāto', 'misconduct': 'micchācāro', 'sexual': 'kāmesu', 'speech': 'vādo', 'spirits': 'meraya',
 'taking': 'ādānaṃ', 'therein': 'Tattha', 'wine': 'surā'}
M['2-U57'] = {'illness': 'roga', 'relatives': 'Ñāti', 'therein': 'Tattha', 'view': 'diṭṭhi', 'virtue': 'sīla',
              'wealth': 'bhoga'}
M['2-17-6-13-0'] = {'dangers': 'ādīnavā', 'impatience': 'akkhantiyā'}
M['2-U58'] = {
 'bad': 'duggatiṃ', 'bad destination': 'duggatiṃ', 'body': 'kāyassa',
 'body after death': 'kāyassa bhedā paraṃ maraṇā', 'breakup': 'bhedā', 'confused': 'sammūḷho',
 'dangers': 'ādīnavā', 'death': 'maraṇā', 'destination': 'duggatiṃ', 'dies': 'kālaṅkaroti', 'disliked': 'appiyo',
 'displeasing': 'amanāpo', 'faults': 'vajja', 'hell': 'nirayaṃ', 'hostility': 'vera', 'impatience': 'akkhantiyā',
 'people': 'janassa', 'place': 'vinipātaṃ', 'reborn': 'upapajjati', 'ruin': 'vinipātaṃ', 'therein': 'Tattha'}
M['2-17-6-14-0'] = {'fears': 'bhayāni'}
M['2-U59'] = {
 'assemblies': 'parisa', 'bad': 'duggati', 'bad destination': 'duggati', 'death': 'maraṇa', 'destination': 'duggati',
 'disrepute': 'asiloka', 'fear': 'bhayaṃ', 'fears': 'bhayāni', 'livelihood': 'Ājīvaka', 'therein': 'Tattha',
 'timidity': 'sārajja'}
M['2-17-6-15-0'] = {'doctrines': 'vādā', 'doctrines of Nibbāna': 'nibbānavādā', 'life': 'diṭṭhadhamma'}
M['2-943'] = {
 'abandoning': 'pahānā', 'abandoning of happiness': 'sukhassa ca pahānā', 'absorption': 'jhānaṃ',
 'alteration': 'aññathābhāvā', 'amuses': 'paricāreti', 'arise': 'uppajjanti', 'ascetic': 'samaṇo', 'away': 'virāgā',
 'brahmin': 'brāhmaṇo', 'declare': 'paññapenti', 'declare the highest': 'paramadiṭṭhadhammanibbānaṃ paññapenti',
 'despair': 'upāyāsā', 'doctrines': 'vādā', 'doctrines of Nibbāna': 'nibbānavādā', 'dwells': 'viharati',
 'elation': 'uppilāvitaṃ', 'engagement': 'ābhogo', 'enters': 'upasampajja', 'enters and dwells': 'upasampajja viharati',
 'examination': 'vicāritaṃ', 'exist': 'natthīti', 'existing': 'sato', 'extent': 'ettāvatā',
 'extent reached': 'ettāvatā / paramadiṭṭhadhammanibbānappatto', 'fading': 'virāgā', 'fives': 'Pañcakaṃ',
 'fourth meditative': 'catutthaṃ jhānaṃ', 'fourth meditative absorption': 'catutthaṃ jhānaṃ',
 'furnished': 'samappito', 'grief': 'sokaparidevadukkhadomanassupāyāsā', 'gross': 'oḷārikaṃ', 'happiness': 'sukha',
 'highest': 'parama', 'highest Nibbāna': 'paramadiṭṭhadhammanibbāna', 'holds': 'evaṃdiṭṭhi',
 'holds this view': 'evaṃdiṭṭhi', 'impermanent': 'aniccā', 'itself': NDE, 'joy': 'pīti', 'lamentation': 'parideva',
 'life': 'diṭṭhadhamma', 'meditative': 'jhānaṃ', 'meditative absorption': 'jhānaṃ', 'Meditative absorption': 'jhānaṃ',
 'mental': 'cetaso', 'mind': 'cetaso', 'pain': 'dukkha', 'painful': 'dukkhā', 'pleasure': 'kāma', 'pleasures': 'Kāmā',
 'provided': 'samaṅgībhūto', 'reached the highest': 'paramadiṭṭhadhammanibbānappatto', 'reckoned': 'akkhāyati',
 'secluded': 'vivicceva', 'secluded from sense': 'vivicceva kāmehi', 'self': 'attā', 'sense': 'kāma',
 'sense pleasure': 'kāma', 'sense pleasures': 'Kāmā', 'sir': 'bho', 'sorrow': 'soka', 'speak': 'vadesi',
 'speaks': 'evaṃvādī', 'stilling': 'vūpasamā', 'stilling of thought': 'vitakkavicārānaṃ vūpasamā',
 'strands': 'guṇehi', 'strands of sense': 'kāmaguṇehi', 'subject to change': 'vipariṇāmadhammā', 'therein': 'Tattha',
 'thought': 'vitakkitaṃ', 'thought and examination': 'vitakkitaṃ vicāritaṃ', 'view': 'diṭṭhi', 'whatever': 'Yadeva',
 'why': 'kissa hetu'}

# ---------------------------------------------------------------- exposition of the sixes
M['2-17-7-0'] = {'exposition': 'niddeso', 'sixes': 'Chakka'}
M['2-17-7-1-0'] = {'dispute': 'vivāda', 'roots': 'mūlāni'}
M['2-944'] = {
 'anger': 'Kodho', 'contempt': 'makkho', 'desire': 'icchatā', 'dispute': 'vivāda', 'envy': 'issā',
 'evil': 'pāpicchatā', 'evil desire': 'pāpicchatā', 'roots': 'mūlāni', 'therein': 'Tattha', 'treachery': 'sāṭheyyaṃ',
 'view': 'sandiṭṭhi'}
SIXOBJ = {
 'mental': 'dhammesu', 'mental objects': 'dhammesu', 'objects': 'dhammesu', 'sights': 'rūpesu', 'smells': 'gandhesu',
 'sounds': 'saddesu', 'tangible': 'phoṭṭhabbesu', 'tangible things': 'phoṭṭhabbesu', 'tastes': 'rasesu',
 'therein': 'Tattha', 'things': 'phoṭṭhabbesu'}
M['2-17-7-2-0'] = {'desires-and-lusts': 'chandarāgā'}
M['2-U60'] = mg(SIXOBJ, {
 'connected': 'gehasitā', 'desires-and-lusts': 'chandarāgā', 'household': 'gehasitā', 'household life': 'gehasitā',
 'life': 'gehasitā', 'lust': 'rāgo', 'mind': 'cittassa', 'passion': 'sārāgo', 'pleasing': 'Manāpiyesu',
 'things': 'dhammā'})
M['2-17-7-3-0'] = {'grounds': 'vatthūni', 'opposition': 'virodha'}
M['2-U61'] = mg(SIXOBJ, {
 'concerning': NDE, 'displeasing': 'Amanāpiyesu', 'dissatisfaction': 'anattamanatā', 'fierceness': 'caṇḍikkaṃ',
 'grounds': 'vatthūni', 'mind': 'cittassa', 'opposition': 'virodha', 'repugnance': 'paṭighāto',
 'resentment': 'āghāto', 'rudeness': 'asuropo'})
M['2-17-7-4-0'] = {'classes': 'kāyā', 'craving': 'taṇhā'}
M['2-U62'] = {
 'classes': 'kāyā', 'craving': 'taṇhā', 'mental': 'dhamma', 'mental objects': 'dhamma', 'objects': 'dhamma',
 'sights': 'Rūpa', 'smells': 'gandha', 'sounds': 'sadda', 'tangible': 'phoṭṭhabba', 'tangible things': 'phoṭṭhabba',
 'tastes': 'rasa', 'therein': 'Tattha', 'things': 'phoṭṭhabba'}
M['2-17-7-5-0'] = {'disrespect': 'agāravā', 'kinds': NDE, 'kinds of disrespect': 'agāravā'}
M['2-945'] = {
 'deference': 'appatisso', 'disrespect': 'agāravā', 'dwells': 'viharati', 'dwells without respect': 'agāravo viharati',
 'heedfulness': 'appamāde', 'hospitality': 'paṭisanthāre', 'kinds': NDE, 'kinds of disrespect': 'agāravā',
 'order': 'saṅghe', 'respect': 'agāravo', 'teacher': 'Satthari', 'teaching': 'dhamme', 'therein': 'Tattha',
 'training': 'sikkhāya'}
DECL = {'lead to decline': 'parihāniyā', 'things': 'dhammā', 'things that lead': 'parihāniyā dhammā'}
M['2-17-7-6-0'] = dict(DECL)
M['2-U63'] = mg(DECL, {
 'activity': 'Kammārāmatā', 'delight': 'ārāmatā', 'mingling': 'saṃsaggārāmatā', 'proliferation': 'papañcārāmatā',
 'sleep': 'niddārāmatā', 'talk': 'bhassārāmatā', 'therein': 'Tattha'})
M['2-17-7-7-0'] = dict(DECL)
M['2-946'] = mg(DECL, HARD, EVILF, {
 'activity': 'Kammārāmatā', 'delight': 'ārāmatā', 'sleep': 'niddārāmatā', 'talk': 'bhassārāmatā', 'therein': 'Tattha'})
SENSE6 = {
 'body': 'kāyena', 'ear': 'sotena', 'explorations': 'upavicārā', 'explores': 'upavicarati', 'eye': 'Cakkhunā',
 'having': NDE, 'heard': 'sutvā', 'known': 'viññāya', 'mental': 'dhammaṃ', 'mental object': 'dhammaṃ',
 'mind': 'manasā', 'nose': 'ghānena', 'object': 'dhammaṃ', 'sight': 'rūpaṃ', 'smell': 'gandhaṃ',
 'smelled': 'ghāyitvā', 'sound': 'saddaṃ', 'tangible': 'phoṭṭhabbaṃ', 'tangible thing': 'phoṭṭhabbaṃ',
 'taste': 'rasaṃ', 'tasted': 'sāyitvā', 'therein': 'Tattha', 'thing': 'phoṭṭhabbaṃ', 'tongue': 'jivhāya',
 'touched': 'phusitvā'}
M['2-17-7-8-0'] = {'explorations': 'upavicārā', 'joy': 'somanassupavicārā'}
M['2-U64'] = mg(SENSE6, joy='somanassa')
M['2-17-7-9-0'] = {'explorations': 'upavicārā', 'grief': 'domanassupavicārā'}
M['2-U65'] = mg(SENSE6, grief='domanassa')
M['2-17-7-10-0'] = {'equanimity': 'upekkhupavicārā', 'explorations': 'upavicārā'}
M['2-U66'] = mg(SENSE6, {'basis for equanimity': 'upekkhāṭṭhāniyaṃ', 'equanimity': 'upekkhā'})
HOUSE = {
 'born': 'cetosamphassajaṃ', 'born of mind-contact': 'cetosamphassajaṃ', 'concerning': NDE, 'connected': 'gehasitaṃ',
 'experience': 'vedayitaṃ', 'experience born': 'cetosamphassajaṃ / vedayitaṃ', 'feeling': 'vedanā',
 'Feeling born': 'cetosamphassajā / vedanā', 'feeling born': 'cetosamphassajā / vedanā',
 'household life': 'gehasitaṃ', 'kinds': NDE, 'life': 'gehasitaṃ', 'mental': 'cetasikaṃ',
 'mind-contact': 'cetosamphassa', 'mental objects': 'dhammesu', 'objects': 'dhammesu', 'sights': 'rūpesu',
 'smells': 'gandhesu', 'sounds': 'saddesu', 'tangible': 'phoṭṭhabbesu', 'tangible things': 'phoṭṭhabbesu',
 'tastes': 'rasesu', 'therein': 'Tattha', 'things': 'phoṭṭhabbesu'}
M['2-17-7-11-0'] = {'household': 'gehasitāni', 'household joy': 'gehasitāni somanassāni', 'joy': 'somanassāni',
                    'kinds': NDE, 'kinds of household': 'gehasitāni'}
M['2-947'] = mg(HOUSE, M['2-17-7-11-0'], {
 'comfort': 'sātaṃ', 'comfortable': 'sātaṃ', 'comfortable happy': 'sātaṃ sukhaṃ',
 'comfortable happy experience': 'sātaṃ sukhaṃ vedayitaṃ', 'comfortable happy feeling': 'sātā sukhā vedanā',
 'happiness': 'sukhaṃ', 'happy': 'sukhaṃ', 'happy experience': 'sukhaṃ vedayitaṃ',
 'happy experience born': 'cetosamphassajaṃ / sukhaṃ vedayitaṃ', 'happy feeling': 'sukhā vedanā',
 'happy feeling born': 'cetosamphassajā / sukhā vedanā', 'mental comfort': 'cetasikaṃ sātaṃ',
 'Mental comfort': 'cetasikaṃ sātaṃ', 'mental comfort connected': 'gehasitaṃ cetasikaṃ sātaṃ',
 'mental happiness': 'cetasikaṃ sukhaṃ', 'pleasing': 'Manāpiyesu'})
M['2-17-7-12-0'] = {'grief': 'domanassāni', 'household': 'gehasitāni', 'household grief': 'gehasitāni domanassāni',
                    'kinds': NDE, 'kinds of household': 'gehasitāni'}
M['2-U67'] = mg(HOUSE, M['2-17-7-12-0'], {
 'discomfort': 'asātaṃ', 'displeasing': 'Amanāpiyesu', 'mental discomfort': 'cetasikaṃ asātaṃ',
 'mental discomfort connected': 'gehasitaṃ cetasikaṃ asātaṃ', 'mental pain': 'cetasikaṃ dukkhaṃ', 'pain': 'dukkhaṃ',
 'painful': 'dukkhaṃ', 'painful experience': 'dukkhaṃ vedayitaṃ',
 'painful experience born': 'cetosamphassajaṃ / dukkhaṃ vedayitaṃ', 'painful feeling': 'dukkhā vedanā',
 'painful feeling born': 'cetosamphassajā / dukkhā vedanā', 'uncomfortable': 'asātaṃ',
 'uncomfortable painful': 'asātaṃ dukkhaṃ', 'uncomfortable painful experience': 'asātaṃ dukkhaṃ vedayitaṃ',
 'uncomfortable painful feeling': 'asātā dukkhā vedanā'})
M['2-17-7-13-0'] = {'equanimity': 'upekkhā', 'household': 'gehasitā', 'household equanimity': 'gehasitā upekkhā',
                    'kinds': NDE, 'kinds of household': 'gehasitā'}
M['2-U68'] = mg(HOUSE, M['2-17-7-13-0'], {
 'basis for equanimity': 'Upekkhāṭṭhāniyesu', 'comfortable': 'sātaṃ', 'experience connected': 'gehasitaṃ cetasikaṃ',
 'mental experience': 'cetasikaṃ', 'mental experience connected': 'gehasitaṃ cetasikaṃ',
 'neither-painful-nor-pleasant': 'adukkhamasukhaṃ', 'pleasant feeling': 'adukkhamasukhā vedanā',
 'uncomfortable': 'nāsātaṃ'})
M['2-17-7-14-0'] = {'views': 'diṭṭhiyo'}
M['2-948'] = {
 'actions': 'kammānaṃ', 'arises': 'uppajjati', 'born': 'jāto', 'else': NDE, 'established': 'thetato',
 'eternal': 'sassato', 'evil': 'pāpakānaṃ', 'exist': 'nāhosi', 'experiences': 'paccanubhoti', 'feels': 'vedeyyo',
 'holds': 'evaṃdiṭṭhi', 'like': 'evaṃdiṭṭhi', 'mine': 'me', 'non-self': 'anattānaṃ', 'perceive': 'sañjānāmī',
 'permanent': 'nicco', 'self': 'attā', 'sixes': 'Chakkaṃ', 'speaks': 'vado', 'stable': 'dhuvo',
 'subject to change': 'avipariṇāmadhammo', 'therein': 'Tattha', 'true': 'saccato',
 'true and established': 'saccato thetato', 'view': 'diṭṭhi', 'view arises': 'diṭṭhi uppajjati', 'views': 'diṭṭhiyo'}

# ---------------------------------------------------------------- exposition of the sevens
M['2-17-8-0'] = {'exposition': 'niddeso', 'sevens': 'Sattaka'}
M['2-17-8-1-0'] = {'tendencies': 'ānusayā', 'underlying': 'ānusayā', 'underlying tendencies': 'ānusayā'}
M['2-949'] = {
 'aversion': 'paṭighānusayo', 'conceit': 'mānānusayo', 'doubt': 'vicikicchānusayo', 'existence': 'bhava',
 'ignorance': 'avijjānusayo', 'lust': 'Kāmarāgānusayo', 'sensual': 'Kāma', 'tendencies': 'ānusayā',
 'tendency': 'ānusayo', 'therein': 'Tattha', 'underlying': 'ānusayā', 'underlying tendencies': 'ānusayā',
 'underlying tendency': 'ānusayo', 'views': 'diṭṭhānusayo'}
SEVENF = {'aversion': 'paṭigha', 'conceit': 'māna', 'doubt': 'vicikicchā', 'existence': 'bhava', 'ignorance': 'avijjā',
          'lust': 'rāga', 'sensual': 'Kāma', 'therein': 'Tattha', 'views': 'diṭṭhi'}
M['2-17-8-2-0'] = {'fetters': 'saṃyojanāni'}
M['2-U69'] = mg(SEVENF, {'fetter': 'saṃyojanaṃ', 'fetters': 'saṃyojanāni'})
M['2-17-8-3-0'] = {'obsessions': 'pariyuṭṭhānāni'}
M['2-U70'] = mg(SEVENF, {'obsession': 'pariyuṭṭhānaṃ', 'obsessions': 'pariyuṭṭhānāni'})
M['2-17-8-4-0'] = {'bad': 'asaddhammā', 'qualities': 'asaddhammā'}
M['2-950'] = {
 'bad': 'asaddhammā', 'confidence': 'Assaddho', 'dread': 'anottappī', 'forgetful': 'muṭṭhassatī', 'lazy': 'kusīto',
 'learning': 'appassuto', 'moral': 'anottappī', 'qualities': 'asaddhammā', 'shameless': 'ahiriko',
 'therein': 'Tattha', 'wisdom': 'duppañño'}
M['2-17-8-5-0'] = {'kinds': NDE, 'kinds of misconduct': 'duccaritāni', 'misconduct': 'duccaritāni'}
M['2-U71'] = {
 'beings': 'Pāṇātipāto', 'chatter': 'samphappalāpo', 'divisive': 'pisuṇā', 'false': 'musā', 'false speech': 'musāvādo',
 'harsh': 'pharusā', 'idle': 'samphappalāpo', 'killing': 'ātipāto', 'killing living': 'Pāṇātipāto', 'kinds': NDE,
 'kinds of misconduct': 'duccaritāni', 'living': 'Pāṇātipāto', 'misconduct': 'duccaritāni', 'sexual': 'kāmesu',
 'speech': 'vācā', 'taking': 'ādānaṃ', 'therein': 'Tattha'}
M['2-17-8-6-0'] = {'conceits': 'mānā'}
M['2-U72'] = {
 'beyond': 'ātimāno', 'conceit': 'Māno', 'Conceit beyond conceit': 'mānātimāno', 'conceits': 'mānā',
 'exaggerated': 'atimāno', 'Exaggerated conceit': 'atimāno', 'over-estimating': 'adhimāno',
 'Over-estimating conceit': 'adhimāno', 'self-belittling': 'omāno', 'Self-belittling conceit': 'omāno',
 'therein': 'Tattha', 'wrong': 'micchāmāno', 'Wrong conceit': 'micchāmāno'}
M['2-17-8-7-0'] = {'views': 'diṭṭhiyo'}
M['2-951'] = {
 'ascetic': 'samaṇo', 'attending': 'amanasikārā', 'aware': NDE, 'belonging': 'kāmāvacaro', 'beyond': 'samatikkamā',
 'body': 'kāyassa', 'brahmin': 'brāhmaṇo', 'breakup': 'bhedā', 'complete': 'sabbaṅgapaccaṅgī', 'completely': 'sammā',
 'completely cut': 'sammā samucchinno', 'Completely passing': 'sabbaso / samatikkamā',
 'completely passing': 'sabbaso / samatikkamā', 'consciousness': 'viññāṇa', 'cutting': 'ucchedaṃ',
 'death': 'maraṇā', 'declare': 'paññapenti', 'declare the cutting': 'ucchedaṃ / paññapenti',
 'destroyed': 'vinassati', 'destruction': 'vināsaṃ', 'disappearance': 'atthaṅgamā', 'diversity': 'nānatta',
 'divine': 'dibbo', 'elements': 'bhūtiko', 'exist': 'hoti', 'exist after death': 'hoti paraṃ maraṇā',
 'existing': 'sato', 'extent': 'ettāvatā', 'extent completely': 'ettāvatā sammā',
 'extent completely cut': 'ettāvatā sammā samucchinno', 'faculties': 'indriyo', 'father': 'pettika',
 'feeding': 'bhakkho', 'field': 'āyatanaṃ', 'field of infinite': 'ākāsānañcāyatanaṃ',
 'field of nothingness': 'ākiñcaññāyatanaṃ', 'food': 'kabaḷīkāra', 'form': 'rūpī', 'great elements': 'mahābhūtiko',
 'having': 'rūpī', 'holds': 'evaṃdiṭṭhi', 'holds this view': 'evaṃdiṭṭhi', 'infinite': 'ananto',
 'infinite consciousness': 'viññāṇañcāyatanaṃ', 'infinite space': 'ākāsānañcāyatanaṃ', 'know': 'jānāsi',
 'lacking': 'ahīnindriyo', 'limbs': 'sabbaṅgapaccaṅgī', 'material': 'rūpī', 'material form': 'rūpī',
 'mind': 'manomayo', 'mother': 'mātā', 'neither-perception-nor-non-perception': 'nevasaññānāsaññāyatanūpago',
 'non-existence': 'vibhavaṃ', 'nothing': 'natthi kiñcīti', 'nothingness': 'ākiñcaññāyatanūpago', 'passing': 'samatikkamā',
 'perceptions': 'saññānaṃ', 'perceptions of diversity': 'nānattasaññānaṃ', 'perceptions of material': 'rūpasaññānaṃ',
 'perceptions of resistance': 'paṭighasaññānaṃ', 'produced': 'sambhavo', 'reached the field': 'āyatanūpago',
 'resistance': 'paṭigha', 'self': 'attā', 'sense': 'kāmāvacaro', 'sense sphere': 'kāmāvacaro', 'sevens': 'Sattakaṃ',
 'sir': 'bho', 'solid': 'kabaḷīkāra', 'space': 'ākāso', 'speak': 'vadesi', 'speaks': 'evaṃvādī',
 'sphere': 'āvacaro', 'therein': 'tattha', 'view': 'diṭṭhi', 'views': 'diṭṭhiyo'}

# ---------------------------------------------------------------- exposition of the eights
M['2-17-9-0'] = {'eights': 'Aṭṭhaka', 'exposition': 'niddeso'}
M['2-17-9-1-0'] = {'defilement': 'kilesa', 'grounds': 'vatthūni', 'grounds of defilement': 'kilesavatthūni'}
KILESA8 = {
 'conceit': 'māno', 'defilement': 'kilesa', 'delusion': 'moho', 'doubt': 'vicikicchā', 'dullness': 'thinaṃ',
 'greed': 'Lobho', 'grounds': 'vatthūni', 'grounds of defilement': 'kilesavatthūni', 'hate': 'doso',
 'restlessness': 'uddhaccaṃ', 'therein': 'Tattha', 'views': 'diṭṭhi'}
M['2-952'] = dict(KILESA8)
M['2-17-9-2-0'] = {'grounds': 'vatthūni', 'grounds of laziness': 'kusītavatthūni', 'laziness': 'kusīta'}
M['2-953'] = {
 'alms': 'piṇḍāya', 'arisen': 'uppanno', 'attaining': 'adhigamāya', 'attaining the unattained': 'anadhigatassa adhigamāya',
 'beans': 'māsācitaṃ', 'body': 'kāyo', 'coarse': 'lūkhassa', 'doing': 'karontassa', 'done': 'kataṃ', 'eighth': 'aṭṭhamaṃ',
 'energy for reaching': 'vīriyaṃ / pattiyā', 'enough': 'kappo', 'fifth': 'pañcamaṃ', 'fill': 'pāripūriṃ',
 'fine': 'paṇītassa', 'food': 'bhojanassa', 'gets': 'labhati', 'got': 'alatthaṃ', 'ground': 'vatthu',
 'ground of laziness': 'kusītavatthu', 'grounds': 'vatthūni', 'grounds of laziness': 'kusītavatthūni',
 'heavy': 'kilanto', 'illness': 'ābādho', 'initiate': 'ārabhati', 'initiate energy': 'vīriyaṃ ārabhati',
 'journey': 'maggo', 'laziness': 'kusīta', 'let': 'Handāhaṃ', 'lie': 'nipajjāmī', 'lies': 'nipajjati', 'like': NDE,
 'load': 'māsācitaṃ', 'monk': 'bhikkhunā', 'needed': 'yāvadatthaṃ', 'needs': 'yāvadatthaṃ', 'reaching': 'pattiyā',
 'reaching the unreached': 'appattassa pattiyā', 'realising': 'sacchikiriyāya',
 'realising the unrealised': 'asacchikatassa sacchikiriyāya', 'reason': 'kappo', 'recovered': 'vuṭṭhito',
 'seventh': 'sattamaṃ', 'sickness': 'gelaññā', 'sixth': 'chaṭṭhaṃ', 'slight': 'appamattako', 'soaked': 'māsācitaṃ',
 'therein': 'Tattha', 'thinks': 'Tassa evaṃ hoti', 'tired': 'kilamissati', 'town': 'nigamaṃ',
 'unattained': 'anadhigatassa', 'unreached': 'appattassa', 'unrealised': 'asacchikatassa',
 'unworkable': 'akammañño', 'village': 'gāmaṃ', 'walking': 'caranto', 'walking for alms': 'piṇḍāya caranto',
 'weak': 'dubbalo'}
M['2-17-9-3-0'] = {'mind': 'cittassa', 'resistance': 'paṭighāto', 'worldly': 'lokadhammesu'}
M['2-954'] = {
 'blame': 'nindāya', 'disrepute': 'ayase', 'fame': 'yase', 'happiness': 'sukhe', 'mind': 'cittassa',
 'opposition': 'paṭivirodho', 'passion': 'sārāgo', 'praise': 'pasaṃsāya', 'resistance': 'paṭighāto',
 'suffering': 'dukkhe', 'therein': 'Tattha', 'worldly': 'lokadhammesu'}
M['2-17-9-4-0'] = dict(VOHARA)
M['2-955'] = dict(M['2-U42'])
M['2-17-9-5-0'] = {'wrongnesses': 'micchattā'}
WRONG8 = {
 'concentration': 'samādhi', 'effort': 'vāyāmo', 'intention': 'saṅkappo', 'livelihood': 'ājīvo',
 'mindfulness': 'sati', 'speech': 'vācā', 'therein': 'Tattha', 'view': 'diṭṭhi', 'wrong': 'Micchā',
 'wrong intention': 'micchāsaṅkappo', 'Wrong view': 'Micchādiṭṭhi', 'wrong view': 'Micchādiṭṭhi',
 'wrongnesses': 'micchattā'}
M['2-956'] = dict(WRONG8)
M['2-17-9-6-0'] = {'faults': 'dosā', 'person': 'purisa'}
M['2-957'] = {
 'amends': 'paṭikarohī', 'anger': 'kopañca', 'answers': 'paṭicarati', 'arms': 'bāhā', 'aside': 'apanāmeti',
 'bearing': 'sāpattikova', 'busy': 'byāvaṭā', 'charge a monk': 'bhikkhuṃ / codenti', 'charged': 'codiyamāno',
 'charges': 'codakaṃyeva', 'committed': 'āpanno', 'displays': 'pātukaroti', 'displeasure': 'appaccayañca',
 'disregarding': 'anādiyitvā', 'eighth': 'aṭṭhamo', 'evades': 'nibbeṭheti', 'extremely': 'atibāḷhaṃ',
 'fault': 'doso', 'faults': 'dosā', 'fifth': 'pañcamo', 'fool': 'bālassa', 'forgetfulness': 'assatiyāva',
 'goes': 'pakkamati', 'hate': 'dosañca', 'having': NDE, 'incompetent': 'abyattassa', 'leads': 'apanāmeti',
 'life': 'hīnāyāvattissāmī', 'like': NDE, 'likes': 'yenakāmaṃ', 'midst': 'majjhe', 'monk': 'bhikkhu',
 'monks': 'bhikkhū', 'monks charge': 'bhikkhū / codenti', 'offence': 'āpattiyā', 'ones': 'āyasmanto',
 'order': 'saṅghaṃ', 'person': 'purisa', 'really': 'nāma', 'remaining': 'tuṇhībhūto', 'remember': 'sarāmi',
 'renounce': 'paccakkhāya', 'renounced': 'paccakkhāya', 'return': 'āvattissāmī', 'returned': 'āvattitvā',
 'satisfied': 'attamanā', 'seventh': 'sattamo', 'sheer': NDE, 'silent': 'tuṇhībhūto', 'sixth': 'chaṭṭho',
 'snaps': 'paṭippharati', 'something': 'bhaṇitabbaṃ', 'speaks': 'bhaṇati', 'such-and-such': 'itthannāmaṃ',
 'talk': 'bhaṇitena', 'therein': 'Tattha', 'thing': 'aññenāññaṃ', 'throws': 'paccāropeti', 'training': 'sikkhaṃ',
 'venerable': 'āyasmanto', 'vexes': 'viheseti', 'waving': 'vikkhepakaṃ', 'wherever': 'yenakāmaṃ',
 'why': 'kiṃ nu kho'}
DOCTR = {
 'death': 'maraṇā', 'declare': 'paññapenti', 'doctrines': 'vādā', 'finite': 'antavā', 'form': 'Rūpī',
 'immaterial': 'arūpī', 'infinite': 'anantavā', 'infinite and unimpaired': 'anantavā / arogo', 'material': 'Rūpī',
 'material form': 'Rūpī', 'self': 'attā', 'therein': 'Tattha', 'unimpaired': 'arogo',
 'unimpaired after death': 'arogo paraṃ maraṇā'}
M['2-17-9-7-0'] = {'doctrines': 'vādā', 'non-percipient': 'asaññī'}
M['2-958'] = mg(DOCTR, {'declare it non-percipient': 'asaññīti naṃ paññapenti', 'non-percipient': 'asaññī'})
M['2-17-9-8-0'] = {'doctrines': 'vādā', 'neither-percipient-nor-non-percipient': 'nevasaññīnāsaññī'}
M['2-959'] = mg(DOCTR, {
 'eights': 'Aṭṭhakaṃ', 'neither-percipient-nor-non-percipient': 'nevasaññīnāsaññī', 'non-percipient': 'nāsaññī',
 'percipient': 'saññī', 'percipient nor non-percipient': 'saññīnāsaññī'})

# ---------------------------------------------------------------- exposition of the nines
M['2-17-10-0'] = {'exposition': 'niddeso', 'nines': 'Navaka'}
M['2-17-10-1-0'] = {'grounds': 'vatthūni', 'resentment': 'āghāta'}
GRUDGE = {
 'arises': 'jāyati', 'dear': 'piyassa', 'disliked': 'appiyassa', 'displeasing': 'amanāpassa', 'doing': 'carati',
 'done': 'acarī', 'grounds': 'vatthūni', 'harm': 'Anatthaṃ', 'pleasing': 'manāpassa', 'resentment': 'āghāto',
 'Resentment arises': 'āghāto jāyati', 'therein': 'Tattha'}
M['2-960'] = dict(GRUDGE)
M['2-17-10-2-0'] = {'person': 'purisa', 'stains': 'malāni'}
M['2-961'] = {
 'anger': 'Kodho', 'contempt': 'makkho', 'deceit': 'māyā', 'desire': 'icchatā', 'envy': 'issā', 'evil': 'pāpicchatā',
 'evil desire': 'pāpicchatā', 'false': 'musā', 'false speech': 'musāvādo', 'person': 'purisa', 'speech': 'vādo',
 'stains': 'malāni', 'stinginess': 'macchariyaṃ', 'therein': 'Tattha', 'treachery': 'sāṭheyyaṃ', 'view': 'diṭṭhi',
 'wrong': 'micchā', 'wrong view': 'micchādiṭṭhi', 'Wrong view': 'micchādiṭṭhi'}
M['2-17-10-3-0'] = {'conceit': 'mānā', 'kinds': 'Navavidhā'}
M['2-962'] = {'conceit': 'māno', 'equal': 'sadisohamasmī', 'kinds': 'navavidhā', 'therein': 'Tattha',
              'worse': 'hīnohamasmī'}
M['2-17-10-4-0'] = {'craving': 'taṇhā', 'rooted': 'mūlakā', 'things': 'dhammā', 'things rooted': 'mūlakā dhammā'}
M['2-963'] = {
 'accusations': 'tuvaṃtuvaṃ', 'contention': 'viggaha', 'craving': 'Taṇhaṃ', 'deciding': 'vinicchayo',
 'desire-and-lust': 'chandarāgo', 'disputes': 'vivāda', 'divisive': 'pesuñña', 'evil': 'pāpakā', 'false': 'musā',
 'false speech': 'musāvādā', 'fast': 'ajjhosānaṃ', 'guarding': 'ārakkho', 'occasion': 'ādhikaraṇaṃ',
 'possession': 'pariggaho', 'quarrels': 'kalaha', 'rooted': 'mūlakā', 'speech': 'vādā', 'sticks': 'daṇḍādāna',
 'stinginess': 'macchariyaṃ', 'taking': 'ādāna', 'therein': 'Tattha', 'things': 'dhammā',
 'things rooted': 'mūlakā dhammā', 'unwholesome': 'akusalā', 'unwholesome things': 'akusalā dhammā',
 'weapons': 'satthādāna'}
PERC = {'form': 'rūpī', 'immaterial': 'arūpī', 'material': 'rūpī', 'material form': 'rūpī', 'non-percipient': 'asaññī',
        'percipient': 'saññī', 'percipient nor non-percipient': 'saññīnāsaññī', 'therein': 'Tattha'}
M['2-17-10-5-0'] = {'agitations': 'iñjitāni'}
M['2-964'] = mg(PERC, {'agitation': 'iñjitametaṃ', 'agitations': 'iñjitāni'})
M['2-17-10-6-0'] = {'imaginings': 'maññitādīni', 'rest': 'ādīni'}
M['2-965'] = mg(PERC, {
 'construction': 'saṅkhatametaṃ', 'constructions': 'saṅkhatāni', 'imaginings': 'maññitāni', 'nines': 'Navakaṃ',
 'proliferations': 'papañcitāni', 'waverings': 'phanditāni'})

# ---------------------------------------------------------------- exposition of the tens
M['2-17-11-0'] = {'exposition': 'niddeso', 'tens': 'Dasaka'}
M['2-17-11-1-0'] = {'defilement': 'kilesa', 'grounds': 'vatthūni', 'grounds of defilement': 'kilesavatthūni',
                    'ten': 'Dasa', 'ten grounds': 'Dasa / vatthūni'}
M['2-966'] = mg(KILESA8, {
 'dread': 'anottappaṃ', 'lack': 'anottappaṃ', 'Lack of moral': 'anottappaṃ', 'lack of moral': 'anottappaṃ',
 'moral': 'anottappaṃ', 'shamelessness': 'ahirikaṃ', 'ten': 'dasa', 'ten grounds': 'dasa / vatthūni'})
M['2-17-11-2-0'] = {'grounds': 'vatthūni', 'resentment': 'āghāta', 'ten': 'Dasa', 'ten grounds': 'Dasa / vatthūni'}
M['2-967'] = mg(GRUDGE, {'groundlessly': 'aṭṭhāne', 'ten': 'dasa', 'ten grounds': 'dasa / vatthūni'})
M['2-17-11-3-0'] = {'courses': 'pathā', 'ten': 'Dasa', 'unwholesome': 'akusala'}
M['2-968'] = {
 'beings': 'Pāṇātipāto', 'chatter': 'samphappalāpo', 'courses': 'pathā', 'covetousness': 'abhijjhā',
 'divisive': 'pisuṇā', 'false': 'musā', 'false speech': 'musāvādo', 'harsh': 'pharusā', 'idle': 'samphappalāpo',
 'ill': 'byāpādo', 'killing': 'ātipāto', 'killing living': 'Pāṇātipāto', 'living': 'Pāṇātipāto',
 'misconduct': 'micchācāro', 'sexual': 'kāmesu', 'speech': 'vācā', 'taking': 'ādānaṃ', 'ten': 'dasa',
 'therein': 'Tattha', 'unwholesome': 'akusala', 'view': 'diṭṭhi', 'wrong': 'micchā', 'wrong view': 'micchādiṭṭhi',
 'Wrong view': 'micchādiṭṭhi'}
M['2-17-11-4-0'] = {'fetters': 'saṃyojanāni', 'ten': 'Dasa', 'ten fetters': 'Dasa saṃyojanāni'}
M['2-969'] = mg(SEVENF, {
 'envy': 'issā', 'fetter': 'saṃyojanaṃ', 'fetters': 'saṃyojanāni', 'grasping': 'parāmāsa', 'observances': 'sīlabbata',
 'stinginess': 'macchariya', 'ten': 'dasa', 'ten fetters': 'dasa saṃyojanāni', 'virtue': 'sīla',
 'wrong': 'parāmāsa', 'wrong grasping': 'parāmāsa'})
M['2-17-11-5-0'] = {'ten': 'Dasa', 'ten wrongnesses': 'Dasa micchattā', 'wrongnesses': 'micchattā'}
M['2-970'] = mg(WRONG8, {'knowledge': 'ñāṇaṃ', 'liberation': 'vimutti', 'ten': 'dasa',
                         'ten wrongnesses': 'dasa micchattā'})
M['2-17-11-6-0'] = {
 'grounds': 'vatthukā', 'ten': 'Dasa', 'ten grounds': 'Dasavatthukā', 'view': 'diṭṭhi',
 'view with ten': 'Dasavatthukā micchādiṭṭhi', 'wrong': 'micchā', 'Wrong view': 'micchādiṭṭhi',
 'wrong view': 'micchādiṭṭhi'}
M['2-971'] = {
 'actions': 'kammānaṃ', 'ascetics': 'samaṇa', 'badly-done': 'dukkaṭānaṃ', 'beings': 'sattā', 'brahmins': 'brāhmaṇā',
 'conduct': 'sammaggatā', 'declare': 'pavedentīti', 'direct': 'abhiññā', 'direct knowledge': 'abhiññā',
 'father': 'pitā', 'fruit': 'phalaṃ', 'grounds': 'vatthukā', 'having': NDE, 'knowledge': 'abhiññā', 'mother': 'mātā',
 'nothing': 'Natthi', 'practice': 'paṭipannā', 'realised': 'sacchikatvā', 'reborn': 'opapātikā', 'right': 'sammā',
 'sacrificed': 'hutaṃ', 'spontaneously': 'opapātikā', 'spontaneously reborn': 'opapātikā', 'ten': 'dasa',
 'ten grounds': 'dasavatthukā', 'themselves': 'sayaṃ', 'therein': 'Tattha', 'view': 'diṭṭhi',
 'view with ten': 'dasavatthukā micchādiṭṭhi', 'well-done': 'sukata', 'wrong': 'micchā',
 'wrong view': 'micchādiṭṭhi', 'Wrong view': 'micchādiṭṭhi'}
M['2-17-11-7-0'] = {
 'extremist': 'antaggāhikā', 'extremist view': 'antaggāhikā diṭṭhi', 'grounds': 'vatthukā', 'ten': 'Dasa',
 'ten grounds': 'Dasavatthukā', 'view': 'diṭṭhi', 'view with ten': 'Dasavatthukā antaggāhikā diṭṭhi'}
M['2-972'] = {
 'body': 'sarīra', 'death': 'maraṇā', 'eternal': 'Sassato', 'exist': 'hoti', 'exist after death': 'hoti / paraṃ maraṇā',
 'exists': 'hoti', 'extremist': 'antaggāhikā', 'extremist view': 'antaggāhikā diṭṭhi', 'finite': 'antavā',
 'grounds': 'vatthukā', 'infinite': 'anantavā', 'soul': 'jīvaṃ', 'Tathāgata exists': 'hoti tathāgato', 'ten': 'dasa',
 'ten grounds': 'dasavatthukā', 'tens': 'Dasakaṃ', 'therein': 'Tattha', 'thing': NDE, 'view': 'diṭṭhi',
 'view with ten': 'dasavatthukā antaggāhikā diṭṭhi'}

# ---------------------------------------------------------------- wanderings of craving
M['2-17-12-0'] = {'craving': 'Taṇhā', 'exposition': 'niddeso', 'wanderings': 'vicarita',
                  'wanderings of craving': 'Taṇhāvicarita', 'Wanderings of Craving': 'Taṇhāvicarita'}
M['2-17-12-1-0'] = {'concerning': 'upādāya', 'internal': 'Ajjhattikassa'}
WAND = {
 'concerning': 'upādāya', 'craving': 'taṇhā', 'eighteen': 'aṭṭhārasa', 'lasting': 'asasmīti',
 'otherwise': 'aññathāsmīti', 'perishing': 'sātasmīti', 'therein': 'Tattha', 'wanderings': 'vicaritāni',
 'wanderings of craving': 'taṇhāvicaritāni', 'Wanderings of Craving': 'taṇhāvicaritāni'}
M['2-973'] = mg(WAND, internal='ajjhattikassa')
WAND2 = mg(WAND, {
 'brahmin': 'brāhmaṇo', 'comparing': 'upanidhāya', 'Comparing oneself': 'upanidhāya', 'conceit': 'mānaṃ',
 'consciousness': 'viññāṇaṃ', 'desire': 'chandaṃ', 'destroyed': 'vinassissāmi', 'eternal': 'sassatosmi',
 'exists': 'sati', 'feeling': 'vedanaṃ', 'form': 'rūpaṃ', 'formations': 'saṅkhāre', 'god': 'devo', 'having': NDE,
 'householder': 'gahaṭṭho', 'human': 'manusso', 'immaterial': 'arūpī', 'internal': 'ajjhattikassa',
 'material': 'rūpaṃ', 'material form': 'rūpaṃ', 'merchant': 'vesso', 'noble': 'khattiyo', 'non-percipient': 'asaññī',
 'obtains': 'paṭilabhati', 'obtains the conceit': 'mānaṃ paṭilabhati', 'obtains the desire': 'chandaṃ paṭilabhati',
 'obtains the view': 'diṭṭhiṃ paṭilabhati', 'oneself': NDE, 'perception': 'saññaṃ', 'percipient': 'saññī',
 'percipient nor non-percipient': 'nevasaññīnāsaññī', 'permanent': 'niccosmi', 'person': 'Parapuggalaṃ',
 'proliferations': 'papañcitāni', 'renunciant': 'pabbajito', 'stable': 'dhuvosmi',
 'subject to change': 'avipariṇāmadhammosmīti', 'thing': 'dhammaṃ', 'thinks': NDE, 'view': 'diṭṭhiṃ',
 'worker': 'suddo'})
M['2-974'] = mg(WAND2, {'discarded': 'anavakāriṃ', 'discarded some thing': 'Kañci dhammaṃ anavakāriṃ'})
M['2-17-12-2-0'] = {'concerning': 'upādāya', 'external': 'Bāhirassa'}
M['2-975'] = mg(WAND, external='bāhirassa')
M['2-976'] = mg(WAND2, {
 'external': 'bāhirassa', 'gathering': 'abhisaññūhitvā', 'hundred': 'sataṃ', 'summing': 'abhisaṅkhipitvā',
 'thirty-six': 'chattiṃsa', 'together': 'tadekajjhaṃ'})
M['2-977'] = {
 'analysis': 'vibhaṅgo', 'annihilationist': 'uccheda', 'blessed': 'bhagavatā', 'chance': 'adhicca', 'doctrines': 'vādā',
 'doctrines of Nibbāna': 'nibbānavādā', 'endless': 'amarā', 'equivocation': 'vikkhepikā', 'eternalist': 'sassata',
 'exposition': 'veyyākaraṇe', 'finished': 'niṭṭhito', 'finite': 'antānantikā', 'grounds': 'gatāni',
 'infinite': 'ānantikā', 'life': 'diṭṭhadhamma', 'minor': 'Khuddaka',
 'neither-percipient-nor-non-percipient': 'nevasaññīnāsaññī', 'non-percipient': 'asaññī',
 'origination': 'samuppannikā', 'partly-eternalist': 'ekaccasassatikā', 'percipient': 'saññī', 'sixteen': 'soḷasa',
 'sixty-two': 'dvāsaṭṭhi', 'spoken': 'vuttāni', 'therein': 'Tattha', 'topics': 'vatthu', 'views': 'diṭṭhi'}

out, missing = [], []
for line in (d / f'{ch}.keywords.md').read_text(encoding='utf-8').splitlines():
    sid, kws = line.split('] ', 1)
    sid = sid[1:]
    m = M.get(sid, {})
    pairs = []
    for k in kws.split(', '):
        k = k.strip()
        if k not in m:
            missing.append((sid, k)); pairs.append(f'???={k}')
        else:
            pairs.append(f'{m[k]}={k}')
    out.append(f'[{sid}] ' + ', '.join(pairs))
(d / f'{ch}.mapped.md').write_text('\n'.join(out) + '\n', encoding='utf-8')
done = [s for s in M]
print('written', len(out), 'segments mapped', len(done))
print('missing in mapped segments', [x for x in missing if x[0] in M])
