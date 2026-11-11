"""English->Pāli keyword map for pi-2 chapter 6 (Paṭiccasamuppādavibhaṅga).

Each English keyword has an ordered list of Pāli candidates; the first one found in THAT
segment's Pāli is used, written as it appears there (case preserved).
Candidate syntax:  'x'  = whole word or phrase
                   '^x' = leading part of a word (clean cut of a compound)
                   'x$' = trailing part of a word (keeps a merged long vowel, e.g. āyatanaṃ)
                   '~x' = anywhere inside a word (medial part of a compound)
                   'a / b' = non-adjacent parts, each searched separately
Per-segment overrides (M) were set after reading the segments.
"""
import pathlib, re
d = pathlib.Path(__file__).parent
root = d.parents[4]
ch = '6-paticcasamuppadavibhango'
NDE = '(no direct equivalent)'
L = r'[^\W\d_]'

segs, buf = {}, []
for line in (root / 'AI_translation' / 'pali' / 'pi-2_split_chapters' / f'{ch}.md').read_text(encoding='utf-8').splitlines():
    buf.append(line)
    m = re.search(r'\^([\w-]+)\s*$', line)
    if m:
        segs[m.group(1)] = '\n'.join(buf); buf = []

def find1(text, p):
    if p.startswith('^'):
        pat = rf'(?<!{L}){re.escape(p[1:])}(?={L})'
    elif p.endswith('$'):
        pat = rf'(?<={L}){re.escape(p[:-1])}(?!{L})'
    elif p.startswith('~'):
        pat = re.escape(p[1:])
    else:
        pat = rf'(?<!{L}){re.escape(p)}(?!{L})'
    m = re.search(pat, text, re.IGNORECASE)
    return m.group(0) if m else None

def find(text, cand):
    out = []
    for p in cand.split(' / '):
        v = find1(text, p)
        if v is None:
            return None
        out.append(v)
    return ' / '.join(out)

SUK = lambda a, b: [f'cetosamphassaj{a} / {b}', f'kāyasamphassaj{a} / {b}']
G = {
 # --- headings
 'analysis': ['vibhaṅgo$'], 'dependent': ['^Paṭicca'], 'origination': ['~samuppāda'],
 'classification': ['bhājanīyaṃ$'], 'discourses': ['^Suttanta'], 'abhidhamma': ['^Abhidhamma'],
 'finished': ['niṭṭhito'], 'matrix': ['Mātikā'], 'exposition': ['niddeso$'], 'rooted': ['~mūlaka'],
 'Exposition of Results': ['vipākaniddeso$'], 'Results Rooted': ['~mūlakavipāka'],
 # --- the chain
 'ignorance': ['avijjā', '^avijjā'], 'ignorance as condition': ['avijjāpaccayā'],
 'formation': ['saṅkhāro', 'saṅkhāro$', '^saṅkhāra'], 'formation as condition': ['saṅkhārapaccayā'],
 'formations': ['saṅkhārā', '^saṅkhāra'], 'formations as condition': ['saṅkhārapaccayā'],
 'consciousness': ['viññāṇaṃ', '^viññāṇa'], 'consciousness as condition': ['viññāṇapaccayā'],
 'mentality': ['nāmaṃ', '^nāma', 'mano'], 'mentality as condition': ['nāmapaccayā'],
 'mentality and material': ['nāmarūpaṃ', '^nāmarūpa'],
 'material': ['rūpaṃ', 'rūpaṃ$'], 'material form': ['rūpaṃ', 'rūpaṃ$'], 'form': ['rūpaṃ', 'rūpaṃ$'],
 'form as condition': ['rūpapaccayā$'], 'material form depending': ['rūpaṃ nissāya'], 'depending': ['nissāya'],
 'occurs': ['vattati'], 'great elements': ['mahābhūtā'], 'elements': ['bhūtā$'], 'derived': ['upādāya'],
 'form derived': ['upādāya rūpaṃ'], 'material form derived': ['upādāya rūpaṃ'],
 'sixth': ['chaṭṭhāyatanaṃ', '^chaṭṭhāyatana'], 'sixth sense-field': ['chaṭṭhāyatanaṃ', '^chaṭṭhāyatana'],
 'sense-field': ['āyatanaṃ$', '~āyatana'], 'sense-field as condition': ['āyatanapaccayā$'],
 'sense-fields': ['saḷāyatanaṃ', '^saḷāyatana', 'āyatanānaṃ'], 'sense-fields as condition': ['saḷāyatanapaccayā'],
 'contact': ['phasso', '^phassa'], 'contact as condition': ['phassapaccayā', '^phassapaccayā'],
 'feeling': ['vedanā', '^vedanā'], 'feeling as condition': ['vedanāpaccayā'],
 'craving': ['taṇhā', '^taṇhā'], 'craving as condition': ['taṇhāpaccayā'],
 'clinging': ['upādānaṃ', '^upādāna'], 'clinging as condition': ['upādānapaccayā'],
 'existence': ['bhavo', 'bhavo$', '^bhava'], 'existence as condition': ['bhavapaccayā'],
 'birth': ['jāti', '^jāti'], 'birth as condition': ['jātipaccayā'],
 'aging': ['jarā', '^jarā'], 'aging and death': ['jarāmaraṇaṃ'], 'death': ['maraṇaṃ', 'maraṇaṃ$'],
 'condition': ['paccayā$'], 'origin': ['samudayo'], 'entire': ['kevalassa'],
 'entire mass': ['kevalassa dukkhakkhandhassa'], 'mass': ['khandhassa$'], 'mass of suffering': ['dukkhakkhandhassa'],
 'suffering': ['^dukkha'], 'therefore': ['Tena'], 'therein': ['Tattha'], 'occasion': ['samaye'],
 'appearance': ['pātubhāvo'], 'coming': ['abhinibbatti', 'abhinibbati', 'saṅgati'], 'together': ['saṅgati'],
 'combination': ['samodhānaṃ'], 'forth': ['abhinibbatti', 'abhinibbati'],
 # --- tetrads
 'tetrad': ['catukkaṃ$'], 'Tetrad of Conditions': ['Paccayacatukkaṃ'], 'Tetrad of Association': ['Sampayuttacatukkaṃ'],
 'Tetrad of Mutuality': ['Aññamaññacatukkaṃ'], 'mutuality': ['^Aññamañña'],
 'associated': ['sampayutto$', 'sampayuttaṃ$', 'sampayuttā$'], 'cause': ['hetuko$', 'hetukaṃ$'], 'causes': ['^Hetu'],
 'formation with ignorance': ['saṅkhāro avijjāhetuko'], 'clinging with craving': ['upādānaṃ taṇhāhetukaṃ'],
 'craving with feeling': ['taṇhā vedanāhetukā'], 'feeling with contact': ['vedanā phassahetukā'],
 # --- ignorance / formation / consciousness / mentality definitions
 'lack': ['aññāṇaṃ'], 'lack of knowledge': ['aññāṇaṃ'], 'lack of vision': ['adassanaṃ'], 'vision': ['dassanaṃ$'],
 'knowledge': ['^ñāṇa', 'ābhiññaṃ$', 'ñāṇaṃ$'],
 'barrier': ['laṅgī$'], 'delusion': ['moho'], 'unwholesome root': ['akusalamūlaṃ', 'akusamūlaṃ', '^akusalamūla'],
 'root': ['mūlaṃ$', '~mūla'], 'roots': ['mūlā$'],
 'unwholesome': ['akusalaṃ', 'akusalā', 'akusalassa', 'ākusalā$', 'ākusalaṃ$', '^akusala'],
 'wholesome': ['kusalaṃ', 'kusalā', 'kusalassa', '^kusala', '~kusala'],
 'intention': ['cetanā'], 'intending': ['sañcetanā'], 'state of intending': ['sañcetayitattaṃ'],
 'mind': ['cittaṃ', 'cittassa', 'cetaso', '^mano'],
 'mental activity': ['mānasaṃ'], 'activity': ['mānasaṃ'], 'heart': ['hadayaṃ'], 'bright': ['paṇḍaraṃ'],
 'mind sense-field': ['manāyatanaṃ'], 'mind faculty': ['manindriyaṃ'], 'faculty': ['indriyaṃ$'],
 'aggregate of consciousness': ['viññāṇakkhandho'], 'Aggregate of Consciousness': ['viññāṇakkhandho'],
 'corresponding': ['^tajjā'], 'mind-consciousness element': ['manoviññāṇadhātu', 'manoviññāṇadhātu$'],
 'mind-consciousness': ['manoviññāṇaṃ', '^manoviññāṇa', '~manoviññāṇa'], 'consciousness element': ['viññāṇadhātu$'],
 'element': ['dhātu$'], 'mind element': ['manodhātu', 'manodhātu$'], 'element has arisen': ['~dhātu uppannā'],
 'eye-consciousness element': ['cakkhuviññāṇadhātu$'], 'body-consciousness element': ['kāyaviññāṇadhātu$'],
 'aggregate of feeling': ['vedanākkhandho'], 'aggregate': ['khandho$'], 'aggregates': ['khandhānaṃ'],
 'aggregate of perception': ['saññākkhandho'], 'Aggregate of Perception': ['saññākkhandho'],
 'aggregate of mental': ['saṅkhārakkhandho'], 'Aggregate of Mental': ['saṅkhārakkhandho'],
 'Mental Formations': ['^saṅkhāra'], 'mental formations': ['^saṅkhāra'], 'perception': ['^saññā', '~saññā'],
 'touching': ['phusanā'], 'caused': ['hetukaṃ$'], 'originated': ['samuṭṭhānaṃ$'],
 'eye': ['cakkhāyatanassa'], 'eye sense-field': ['cakkhāyatanassa'], 'ear': ['sotāyatanassa'], 'ear sense-field': ['sotāyatanassa'],
 'nose': ['ghānāyatanassa'], 'nose sense-field': ['ghānāyatanassa'], 'tongue': ['jivhāyatanassa'], 'tongue sense-field': ['jivhāyatanassa'],
 'body': ['kāyāyatanassa'], 'body sense-field': ['kāyāyatanassa'], 'aside': ['Ṭhapetvā'], 'setting': ['Ṭhapetvā'],
 # --- feeling definitions
 'Mental comfort': ['cetasikaṃ sātaṃ'], 'mental comfort': ['cetasikaṃ sātaṃ'], 'mental happiness': ['cetasikaṃ sukhaṃ'],
 'bodily': ['kāyikaṃ', '^kāya'], 'comfort': ['sātaṃ'], 'happiness': ['sukhaṃ', 'sukhassa', '^sukha'],
 'comfortable': ['sātaṃ'], 'comfortable happy': ['sātaṃ sukhaṃ'], 'comfortable happy experience': ['sātaṃ sukhaṃ vedayitaṃ'],
 'comfortable happy feeling': ['sātā sukhā vedanā'], 'happy': ['sukhaṃ'], 'happy experience': ['sukhaṃ vedayitaṃ'],
 'happy feeling': ['sukhā vedanā'], 'happy experience born': SUK('aṃ', 'sukhaṃ vedayitaṃ'),
 'happy feeling born': SUK('ā', 'sukhā vedanā'), 'experience': ['vedayitaṃ'], 'experience born': SUK('aṃ', 'vedayitaṃ'),
 'feeling born': SUK('ā', 'vedanā'), 'Feeling born': SUK('ā', 'vedanā'),
 'born of mind-contact': ['cetosamphassajaṃ'], 'born of body-contact': ['kāyasamphassajaṃ'],
 'born': ['cetosamphassajaṃ', 'kāyasamphassajaṃ', 'cittajaṃ', 'sañjāti'],
 'mind-contact': ['^cetosamphassa', 'manosamphasso'], 'body-contact': ['^kāyasamphassa', 'kāyasamphasso'],
 'neither-painful-nor-pleasant': ['adukkhamasukhaṃ'], 'pleasant feeling': ['adukkhamasukhā vedanā'],
 'mental experience': ['cetasikaṃ'], 'uncomfortable': ['nāsātaṃ', 'asātaṃ'],
 'discomfort': ['asātaṃ'], 'pain': ['dukkhaṃ', '^dukkha'], 'painful': ['dukkhaṃ', '^dukkha'],
 'painful experience': ['dukkhaṃ vedayitaṃ'], 'painful experience born': SUK('aṃ', 'dukkhaṃ vedayitaṃ'),
 'painful feeling': ['dukkhā vedanā'], 'painful feeling born': SUK('ā', 'dukkhā vedanā'),
 'uncomfortable painful': ['asātaṃ dukkhaṃ'], 'uncomfortable painful experience': ['asātaṃ dukkhaṃ vedayitaṃ'],
 'uncomfortable painful feeling': ['asātā dukkhā vedanā'], 'mental discomfort': ['cetasikaṃ asātaṃ'],
 'mental pain': ['cetasikaṃ dukkhaṃ'], 'grief': ['domanassaṃ', '^domanassa'],
 'mental': ['dhammārammaṇaṃ', 'dhammārammaṇā', 'mānasaṃ', 'cetasikaṃ', '^saṅkhāra'],
 'mental object': ['dhammārammaṇaṃ', 'dhammārammaṇā'],
 # --- craving / clinging definitions
 'lust': ['rāgo'], 'passion': ['sārāgo', 'sārāgo$'], 'compliance': ['anunayo'], 'attraction': ['anurodho'],
 'delight': ['nandī'], 'delight-and-lust': ['nandirāgo'],
 'view': ['diṭṭhi', '^diṭṭhigata', '^diṭṭhi', 'diṭṭhi$'], 'resort to views': ['diṭṭhigataṃ'], 'resort': ['diṭṭhigataṃ'],
 'views': ['diṭṭhigataṃ', 'diṭṭhigatānaṃ'], 'thicket': ['gahanaṃ$'], 'wilderness': ['kantāro$'],
 'distortion': ['visūkāyikaṃ$'], 'wavering': ['vipphanditaṃ$', 'saṃsayo'], 'fetter': ['saṃyojanaṃ$'],
 'grip': ['gāho', 'gāho$'], 'insistence': ['abhiniveso'], 'wrong grasping': ['parāmāso'], 'grasping': ['parāmāso'],
 'bad': ['kummaggo'], 'road': ['maggo$'], 'wrong path': ['micchāpatho'], 'wrong': ['^micchā'],
 'path': ['maggaṃ', '^magga', 'patho$'], 'wrongness': ['micchattaṃ'], 'sectarian': ['titthāyatanaṃ'],
 'domain': ['āyatanaṃ$'], 'distorted grip': ['vipariyāsaggāho'], 'distorted': ['^vipariyāsa'],
 # --- birth / aging / death of states
 'various': ['tesaṃ tesaṃ'], 'arising': ['nibbatti'], 'growing': ['jīraṇatā'], 'old': ['jīraṇatā'],
 'span': ['āyuno'], 'life': ['āyuno', '^diṭṭhadhamma'], 'destruction': ['khayo'], 'vanishing': ['vayo'],
 'breakup': ['bhedo'], 'disintegration': ['paribhedo'], 'impermanence': ['aniccatā'], 'disappearance': ['antaradhānaṃ'],
 # --- openings (Katame dhammā ...)
 'things': ['dhammā', 'dhammānaṃ', '^dhamma'], 'things are unwholesome': ['dhammā akusalā'],
 'things are wholesome': ['dhammā kusalā'], 'things are neutral': ['dhammā abyākatā'], 'neutral': ['abyākatā', '^abyākata'],
 'unwholesome mind': ['akusalaṃ cittaṃ'], 'wholesome mind': ['kusalaṃ cittaṃ'], 'arisen': ['uppannaṃ', 'uppannā'],
 'accompanied': ['sahagataṃ$', 'sahagatā$'], 'accompanied by joy': ['somanassasahagataṃ', 'somanassasahagatā'],
 'joy': ['^somanassa'], 'accompanied by equanimity': ['upekkhāsahagataṃ', 'upekkhāsahagatā'], 'equanimity': ['^upekkhā'],
 'accompanied by happiness': ['sukhasahagataṃ'], 'prompting': ['sasaṅkhārena'],
 'dissociated': ['vippayuttaṃ$', 'vippayuttā$'], 'dissociated from knowledge': ['ñāṇavippayuttaṃ', 'ñāṇavippayuttā'],
 'object': ['ārammaṇaṃ$', 'ārammaṇā$'],
 'sight': ['rūpārammaṇaṃ', 'rūpārammaṇā'], 'sound': ['saddārammaṇaṃ', 'saddārammaṇā'],
 'smell': ['gandhārammaṇaṃ', 'gandhārammaṇā'], 'taste': ['rasārammaṇaṃ', 'rasārammaṇā'],
 'tangible': ['phoṭṭhabbārammaṇaṃ', 'phoṭṭhabbārammaṇā'], 'tangible thing': ['phoṭṭhabbārammaṇaṃ', 'phoṭṭhabbārammaṇā'],
 'thing': ['phoṭṭhabbārammaṇaṃ', 'phoṭṭhabbārammaṇā'], 'whatever': ['yaṃ yaṃ', 'yaṃ vā panaññampi'],
 'sense sphere': ['kāmāvacaraṃ', 'kāmāvacarā'], 'sense': ['kāmāvacaraṃ', 'kāmāvacarā', 'kāmehi'],
 'sphere': ['āvacaraṃ$', 'āvacarā$', 'āvacarassa$'], 'sphere has arisen': ['āvacaraṃ$ / uppannaṃ'],
 'sense-sphere': ['kāmāvacarassa'], 'sense-sphere wholesome': ['kāmāvacarassa kusalassa'],
 'wholesome action': ['kusalassa kammassa'], 'done': ['katattā'], 'accumulated': ['upacitattā'], 'developed': ['bhāvitattā'],
 'resultant': ['vipākaṃ', 'vipākā'],
 'eye-consciousness': ['cakkhuviññāṇaṃ', '~cakkhuviññāṇa'], 'ear-consciousness': ['sotaviññāṇaṃ'],
 'nose-consciousness': ['ghānaviññāṇaṃ'], 'tongue-consciousness': ['jivhāviññāṇaṃ'],
 'body-consciousness': ['kāyaviññāṇaṃ', '~kāyaviññāṇa'],
 'functional': ['kiriyā', 'kiriyaṃ'], 'wholesome nor unwholesome': ['kusalā nākusalā', 'kusalaṃ nākusalaṃ'],
 'pleasant': ['~sukha'], 'dwelling': ['vihāraṃ$'],
 # --- wholesome roots, confidence, decision
 'wholesome roots': ['kusalamūlā'], 'wholesome root': ['kusalamūlaṃ', '^kusalamūla', '~kusalamūla'],
 'root as condition': ['mūlapaccayā$'], 'non-greed': ['alobho'], 'absence': ['alubbhanā'], 'greed': ['lobho$'],
 'non-passion': ['asārāgo'], 'non-covetousness': ['anabhijjhā'], 'non-hate': ['adoso'], 'hate': ['doso$'],
 'hating': ['dussanā$'], 'non-ill-will': ['abyāpādo'], 'ill-will': ['byāpādo$'], 'freedom': ['abyāpajjo'],
 'non-delusion': ['amoho'], 'wisdom': ['paññā'], 'understanding': ['pajānanā'],
 'investigation of things': ['dhammavicayo'], 'investigation': ['vicayo$'], 'right': ['^sammā'],
 'awakening': ['sambojjhaṅgo$'], 'awakening factor': ['sambojjhaṅgo$'], 'factor of investigation': ['vicayasambojjhaṅgo$'],
 'factor': ['aṅgaṃ$'], 'path factor': ['maggaṅgaṃ'],
 'confidence': ['pasādo'], 'confidence as condition': ['pasādapaccayā'], 'trusting': ['saddahanā'], 'reliance': ['okappanā'],
 'decision as condition': ['adhimokkhapaccayā'], 'decided': ['tadadhimuttatā'], 'deciding': ['adhimuccanā'],
 # --- unwholesome-specific
 'aversion': ['paṭighaṃ', '^paṭigha'], 'aversion as condition': ['paṭighapaccayā'], 'resentment': ['āghāto'],
 'fierceness': ['caṇḍikkaṃ'], 'rudeness': ['asuropo'], 'dissatisfaction': ['anattamanatā'],
 'doubt': ['vicikicchā'], 'doubt as condition': ['vicikicchāpaccayā'], 'doubting': ['kaṅkhāyanā'], 'perplexity': ['vimati'],
 'uncertainty': ['vicikicchā'], 'minds': ['dveḷhakaṃ'], 'crossroads': ['dvidhāpatho'], 'sides': ['^anekaṃsa'],
 'hesitation': ['āsappanā'], 'vacillation': ['parisappanā'], 'failure': ['apariyogāhaṇā'], 'plunge': ['apariyogāhaṇā'],
 'rigidity': ['chambhitattaṃ'], 'confusion': ['vilekho$'], 'restlessness': ['uddhaccaṃ'],
 'restlessness as condition': ['uddhaccapaccayā'], 'calm': ['vūpasamo$'], 'lack of calm': ['avūpasamo'],
 'distraction': ['vikkhepo'], 'mental distraction': ['cetaso vikkhepo'], 'agitation': ['bhantattaṃ'],
 'non-distraction': ['avikkhepo'],
 # --- jhāna openings
 'develops': ['bhāveti'], 'develops the path': ['maggaṃ bhāveti'], 'develops the meditative': ['jhānaṃ bhāveti'],
 'path for rebirth': ['~ūpapattiyā maggaṃ'], 'rebirth': ['ūpapattiyā$'],
 'fine-material': ['rūpūpapattiyā', 'rūpāvacarā', 'rūpāvacarassa', 'rūpāvacaraṃ'],
 'fine-material sphere': ['rūpūpapattiyā', 'rūpāvacarā'], 'fine-material-sphere': ['rūpāvacarassa', 'rūpāvacaraṃ'],
 'immaterial': ['arūpūpapattiyā', 'arūpāvacarā', 'arūpāvacarassa'], 'immaterial sphere': ['arūpūpapattiyā', 'arūpāvacarā'],
 'immaterial-sphere': ['arūpāvacarassa', 'arūpāvacaraṃ'], 'immaterial-sphere meditative absorption': ['arūpāvacaraṃ jhānaṃ'],
 'secluded': ['vivicceva'], 'secluded from sense': ['vivicceva kāmehi'], 'sense pleasures': ['kāmehi'], 'pleasures': ['kāmehi'],
 'enters': ['upasampajja'], 'dwells': ['viharati'], 'enters and dwells': ['upasampajja viharati'],
 'meditative absorption': ['jhānaṃ'], 'Meditative absorption': ['jhānaṃ'], 'meditative': ['jhānaṃ'], 'absorption': ['jhānaṃ'],
 'earth device': ['pathavīkasiṇaṃ'], 'earth': ['^pathavī'], 'device': ['kasiṇaṃ$'],
 'completely': ['sabbaso'], 'Completely passing': ['sabbaso / samatikkamma'], 'completely passing': ['sabbaso / samatikkamma'],
 'passing': ['samatikkamma'], 'beyond': ['samatikkamma', 'lokuttaraṃ'],
 'field of nothingness': ['ākiñcaññāyatanaṃ'], 'nothingness': ['ākiñcaññāyatanaṃ'], 'field': ['āyatanaṃ$'],
 'neither-perception-nor-non-perception': ['^nevasaññānāsaññāyatana'],
 'abandoning': ['pahānā', 'pahānāya'], 'abandoning of happiness': ['sukhassa ca pahānā'],
 'fourth meditative absorption': ['catutthaṃ jhānaṃ'], 'fourth meditative': ['catutthaṃ jhānaṃ'],
 'leading to dismantling': ['apacayagāmiṃ'], 'dismantling': ['^apacaya'], 'abandoning of views': ['diṭṭhigatānaṃ pahānāya'],
 'reaching': ['pattiyā'], 'stage': ['bhūmiyā'], 'difficult practice': ['dukkhapaṭipadaṃ'], 'difficult': ['^dukkha'],
 'practice': ['paṭipadaṃ$'], 'practice and slow': ['~paṭipadaṃ dandhābhiññaṃ'], 'slow': ['dandhābhiññaṃ'],
 'slow direct': ['dandhābhiññaṃ'], 'slow direct knowledge': ['dandhābhiññaṃ'], 'direct': ['ābhiññaṃ$'],
 'direct knowledge': ['ābhiññaṃ$'], 'wholesome meditative absorption': ['kusalassa jhānassa'],
 'wholesome meditative': ['kusalassa jhānassa'], 'emptiness': ['suññataṃ'],
}

# ---- per-segment overrides (set after reading each segment)
M = {}
M['2-225'] = {'sorrow': '~soka', 'lamentation': '~parideva', 'pain': '~dukkha', 'grief': 'domanassupāyāsā$',
              'despair': 'upāyāsā$', 'origin': 'samudayo', 'suffering': '^dukkha'}
M['2-226'] = {
 'knowing': 'aññāṇaṃ', 'suffering': 'Dukkhe', 'origin of suffering': 'dukkhasamudaye', 'origin': 'samudaye$',
 'cessation of suffering': 'dukkhanirodhe', 'cessation': 'nirodhe$', 'formation': 'saṅkhāro$',
 'meritorious formation': 'Puññābhisaṅkhāro', 'meritorious': 'Puññābhisaṅkhāro',
 'demeritorious formation': 'apuññābhisaṅkhāro', 'demeritorious': 'apuññābhisaṅkhāro',
 'imperturbable formation': 'āneñjābhisaṅkhāro', 'imperturbable': 'āneñjābhisaṅkhāro',
 'bodily formation': 'kāyasaṅkhāro', 'bodily': '^kāya', 'verbal': '^vacī', 'mental': '^citta',
 'wholesome': 'Kusalā', 'unwholesome': 'Akusalā', 'sense sphere': 'kāmāvacarā', 'sense': 'kāmāvacarā',
 'sphere': 'āvacarā$', 'fine-material sphere': 'rūpāvacarā', 'fine-material': 'rūpāvacarā',
 'immaterial sphere': 'arūpāvacarā', 'immaterial': 'arūpāvacarā', 'belonging': NDE, 'giving': '^dāna',
 'virtue': '^sīla', 'meditative development': '^bhāvanā', 'meditative': '^bhāvanā'}
M['2-227'] = {'consciousness': 'viññāṇaṃ'}
M['2-229'] = {'eye': 'Cakkhāyatanaṃ', 'eye sense-field': 'Cakkhāyatanaṃ', 'ear': 'sotāyatanaṃ', 'ear sense-field': 'sotāyatanaṃ',
 'nose': 'ghānāyatanaṃ', 'nose sense-field': 'ghānāyatanaṃ', 'tongue': 'jivhāyatanaṃ', 'tongue sense-field': 'jivhāyatanaṃ',
 'body': 'kāyāyatanaṃ', 'body sense-field': 'kāyāyatanaṃ', 'mind': 'manāyatanaṃ', 'mind sense-field': 'manāyatanaṃ',
 'form': '~rūpa', 'material': '~rūpa', 'material form': '~rūpa', 'mentality and material': '^nāmarūpa',
 'sense-fields': 'saḷāyatanaṃ'}
M['2-230'] = {'eye-contact': 'Cakkhusamphasso', 'ear-contact': 'sotasamphasso', 'nose-contact': 'ghānasamphasso',
 'tongue-contact': 'jivhāsamphasso', 'body-contact': 'kāyasamphasso', 'mind-contact': 'manosamphasso', 'sense-fields': '^saḷāyatana'}
M['2-231'] = {
 'born': 'Cakkhusamphassajā', 'born of eye-contact': 'Cakkhusamphassajā', 'born of ear-contact': 'sotasamphassajā',
 'born of nose-contact': 'ghānasamphassajā', 'born of tongue-contact': 'jivhāsamphassajā',
 'born of body-contact': 'kāyasamphassajā', 'born of mind-contact': 'manosamphassajā',
 'eye-contact': '^Cakkhusamphassa', 'ear-contact': '^sotasamphassa', 'nose-contact': '^ghānasamphassa',
 'tongue-contact': '^jivhāsamphassa', 'body-contact': '^kāyasamphassa', 'mind-contact': '^manosamphassa',
 'Feeling born': 'Cakkhusamphassajā vedanā', 'feeling born': 'Cakkhusamphassajā vedanā'}
M['2-232'] = {'sights': '^Rūpa', 'sounds': '^sadda', 'smells': '^gandha', 'tastes': '^rasa', 'tangible': '^phoṭṭhabba',
 'tangible things': '^phoṭṭhabba', 'things': '^phoṭṭhabba', 'mental': '^dhamma', 'mental objects': '^dhamma', 'objects': '^dhamma'}
M['2-233'] = {'Clinging to sense': 'Kāmupādānaṃ', 'sense': 'Kāmupādānaṃ', 'sense pleasures': 'Kāmupādānaṃ',
 'pleasures': 'Kāmupādānaṃ', 'clinging to views': 'diṭṭhupādānaṃ', 'views': 'diṭṭhupādānaṃ',
 'clinging to rules': 'sīlabbatupādānaṃ', 'rules and observances': 'sīlabbatupādānaṃ', 'rules': '^sīla',
 'observances': 'sīlabbatupādānaṃ', 'doctrine': 'attavādupādānaṃ', 'self': '^atta'}
M['2-234'] = {'twofold': 'duvidhena', 'action-existence': 'kammabhavo', 'rebirth-existence': 'upapattibhavo',
 'meritorious formation': 'Puññābhisaṅkhāro', 'meritorious': 'Puññābhisaṅkhāro',
 'demeritorious formation': 'apuññābhisaṅkhāro', 'demeritorious': 'apuññābhisaṅkhāro',
 'imperturbable formation': 'āneñjābhisaṅkhāro', 'imperturbable': 'āneñjābhisaṅkhāro', 'formation': 'ābhisaṅkhāro$',
 'leads': '~gāmi', 'sense-sphere': '^Kāma', 'fine-material': '^rūpa', 'immaterial': '^arūpa', 'percipient': '^saññā',
 'non-percipient': '^asaññā', 'neither-percipient-nor-non-percipient': '^nevasaññānāsaññā',
 'one-constituent': '^ekavokāra', 'four-constituent': '^catuvokāra', 'five-constituent': '^pañcavokāra'}
M['2-235'] = {'beings': 'sattānaṃ', 'classes': 'nikāye$', 'born': 'sañjāti', 'descent': 'okkanti',
 'obtaining': 'paṭilābho', 'sense-fields': 'āyatanānaṃ'}
M['2-236'] = {'beings': 'sattānaṃ', 'classes': 'nikāye$', 'broken': 'khaṇḍiccaṃ', 'teeth': 'khaṇḍiccaṃ',
 'grey': 'pāliccaṃ', 'hair': 'pāliccaṃ', 'wrinkled': '^vali', 'skin': '~taca', 'faculties': 'indriyānaṃ',
 'ripening': 'paripāko', 'passing': 'cuti', 'away': 'cuti', 'dying': 'maccu', 'completion': 'kālakiriyā',
 'laying': 'nikkhepo', 'body': 'kaḷevarassa', 'life faculty': '^jīvitindriya', 'faculty': '~indriya',
 'cutting': 'upacchedo$'}
LOSS = {'touched': 'phuṭṭhassa', 'touched by loss': '~byasanena vā phuṭṭhassa', 'relatives': '^Ñāti', 'wealth': '^bhoga',
 'illness': '^roga', 'virtue': '^sīla', 'view': '^diṭṭhi', 'meets': 'samannāgatassa', 'misfortune': 'byasanena',
 'painful': '^dukkha', 'thing': 'dhammena$'}
M['2-237'] = dict(LOSS, **{'sorrow': 'soko', 'sorrowing': 'socanā', 'inner': '^anto', 'deep': 'parisoko$',
 'burning': 'parijjhāyanā', 'mind': 'cetaso', 'grief': 'domanassaṃ', 'dart': 'sallaṃ$'})
M['2-238'] = dict(LOSS, **{'crying': 'ādevo', 'lamenting': 'paridevo', 'lamentation': 'paridevo', 'act': 'ādevanā',
 'talk': 'vācā', 'wordy': 'palāpo', 'babbling': 'vippalāpo', 'wailing': 'lālappo'})
M['2-241'] = dict(LOSS, **{'despair': 'upāyāso', 'distress': 'āyāso'})
M['2-242'] = {'finished': NDE, 'coming': 'saṅgati'}
M['2-6-2-10-0'] = {'unwholesome': '^Akusala'}
M['2-6-2-11-0'] = {'wholesome': '^Kusala'}
M['2-6-2-12-0'] = {'neutral': '^Abyākata'}
M['2-6-2-13-0'] = {'wholesome': '~kusala'}
M['2-6-2-14-0'] = {'wholesome': '^Kusala'}
M['2-6-2-15-0'] = {'unwholesome': '^Akusala'}
M['2-289'] = {'doubt': 'vicikicchā', 'grasping': 'gāho$', 'mind': 'cittassa', 'mental': 'cetasikaṃ'}
for s in ('2-300', '2-302', '2-340', '2-341'):  # no avacara word in these segments
    M[s] = {'sphere': NDE}
M['2-304'] = {'views': 'diṭṭhigatānaṃ', 'abandoning': 'pahānāya'}
M['2-305'] = {'things': 'dhammānaṃ', 'path': 'maggapariyāpannaṃ'}

kwlines = (d / f'{ch}.keywords.md').read_text(encoding='utf-8').splitlines()
out, unresolved = [], []
for line in kwlines:
    sid, rest = line.split('] ', 1)
    sid = sid[1:]
    text = segs[sid]
    pairs = []
    for kw in [k.strip() for k in rest.split(', ')]:
        if kw in M.get(sid, {}):
            c = M[sid][kw]
            val = c if c == NDE else find(text, c)
            if val is None:
                unresolved.append((sid, kw, 'OVERRIDE ' + c)); val = '??'
        else:
            val = None
            for c in G.get(kw, []):
                val = find(text, c)
                if val: break
            if val is None:
                unresolved.append((sid, kw, '')); val = '??'
        pairs.append(f'{val}={kw}')
    out.append(f'[{sid}] ' + ', '.join(pairs))

(d / f'{ch}.mapped.md').write_text('\n'.join(out) + '\n', encoding='utf-8')
for u in unresolved: print(u)
print('unresolved', len(unresolved))
