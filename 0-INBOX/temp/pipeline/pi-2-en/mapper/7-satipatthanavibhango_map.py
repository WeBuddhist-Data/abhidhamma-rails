import pathlib, re
d = pathlib.Path(__file__).parent
root = d.parents[4]
ch = '7-satipatthanavibhango'
NDE = '(no direct equivalent)'

# ---- shared blocks -------------------------------------------------------
# "ātāpī sampajāno satimā vineyya loke abhijjhādomanassaṃ"
REFRAIN = {
 'ardent': 'ātāpī', 'clearly': 'sampajāno', 'comprehending': 'sampajāno', 'covetousness': 'abhijjhā',
 'covetousness and grief': 'abhijjhādomanassaṃ', 'grief': 'domanassaṃ',
 'grief with regard': 'loke abhijjhādomanassaṃ', 'having': NDE, 'mindful': 'satimā', 'regard': 'loke',
 'removed': 'vineyya', 'removed covetousness': 'vineyya / abhijjhā',
}
# the four-fold "kāye kāyānupassī viharati ..." list (2-355, 2-374, 2-380, 2-386)
FOURFOLD = dict(REFRAIN, **{
 'body': 'kāye', 'contemplating': 'ānupassī', 'contemplating feelings': 'vedanānupassī',
 'contemplating mental': 'dhammānupassī', 'contemplating mental objects': 'dhammānupassī',
 'contemplating the body': 'kāyānupassī', 'contemplating the mind': 'cittānupassī', 'dwells': 'viharati',
 'dwells contemplating': 'kāyānupassī viharati', 'dwells contemplating feelings': 'vedanānupassī viharati',
 'dwells contemplating mental': 'dhammānupassī viharati', 'feelings': 'vedanāsu',
 'feelings in feelings': 'vedanāsu vedanānupassī', 'foundations': 'paṭṭhānā',
 'foundations of mindfulness': 'satipaṭṭhānā', 'mental': 'dhammesu', 'mental objects': 'dhammesu', 'mind': 'citte',
 'mindfulness': 'satipaṭṭhānā', 'monk': 'bhikkhu', 'monk dwells': 'bhikkhu / viharati',
 'monk dwells contemplating': 'bhikkhu / kāyānupassī viharati', 'objects': 'dhammesu', 'objects in mental': 'dhammesu',
})
# the meditation-practice frame (2-356, 2-363, 2-365, 2-367)
def PRACTICE(obj, anupassi):
    return dict(REFRAIN, **{
     'contemplating': 'ānupassī', 'cultivated': 'bahulīkaritvā', 'cultivates': 'bahulīkaroti',
     'developed': 'bhāvetvā', 'develops': 'bhāveti', 'directs': 'upasaṃharati',
     'directs his mind': 'cittaṃ upasaṃharati', 'dwell': 'viharati', 'dwell contemplating': f'{anupassi} viharati',
     'dwells': 'viharati', 'dwells contemplating': f'{anupassi} viharati', 'established': 'vavatthapetvā',
     'establishes': 'vavatthapeti', 'externally': 'bahiddhā', 'internally': 'ajjhattaṃ',
     'internally and externally': 'ajjhattabahiddhā', 'knows': 'pajānāti', 'mind': 'cittaṃ', 'monk': 'bhikkhu',
     'monk dwell': 'bhikkhu / viharati', 'monk dwell contemplating': f'bhikkhu / {anupassi} viharati',
     'monk dwells': 'bhikkhu / viharati', 'monk dwells contemplating': f'bhikkhu / {anupassi} viharati',
     'practised': 'āsevitvā', 'practised that sign': 'taṃ nimittaṃ āsevitvā', 'practises': 'āsevati',
     'practises that sign': 'taṃ nimittaṃ āsevati', 'sign': 'nimittaṃ',
    })
# "anupassī / ātāpī / sampajāno / satimā" glosses: "upeto hoti samupeto upāgato ..."
ENDOWED = {
 'complete': 'sampanno', 'endowed': 'upeto', 'fully': 'samupeto', 'fully endowed': 'samupeto',
 'furnished': 'samannāgato', 'having': NDE, 'possessed': 'upapanno', 'right': 'sammā', 'therefore': 'Tena',
 'therein': 'Tattha',
}
WISDOM = dict(ENDOWED, **{
 'investigation': 'vicayo', 'investigation of things': 'dhammavicayo', 'non-delusion': 'amoho', 'things': 'dhamma',
 'understanding': 'pajānanā', 'view': 'diṭṭhi', 'wisdom': 'paññā',
})
DWELLS = {
 'carries': 'yāpeti', 'conducts': 'carati', 'dwells': 'viharati', 'goes': 'vattati', 'going': 'pāleti',
 'himself': NDE, 'keeps': 'pāleti', 'maintains': 'yapeti', 'moves': 'Iriyati', 'therefore': 'Tena',
}
# "vineyya loke abhijjhādomanassa"nti" explanation (2-362, 2-364, 2-366, 2-373)
WORLD = {
 'aggregates': 'khandhā', 'born': 'cetosamphassajaṃ', 'born of mind-contact': 'cetosamphassajaṃ',
 'brought': 'byantīkatā', 'calmed': 'samitā', 'clung': 'upādāna', 'completely': 'abbhatthaṅgatā',
 'completely dried': 'visositā', 'contemplating': 'ānupassanā', 'covetousness': 'abhijjhā',
 'covetousness and grief': 'abhijjhādomanassa', 'discomfort': 'asātaṃ', 'dried': 'sositā',
 'experience': 'vedayitaṃ', 'experience born': 'cetosamphassajaṃ / vedayitaṃ', 'exposition': 'niddeso',
 'Exposition of Contemplating': 'ānupassanāniddeso', 'extinguished': 'appitā', 'feeling': 'vedanā',
 'Feeling born': 'cetosamphassajā / vedanā', 'feeling born': 'cetosamphassajā / vedanā', 'fully': 'byappitā',
 'fully extinguished': 'byappitā', 'gone': 'atthaṅgatā', 'grief': 'domanassaṃ',
 'grief with regard': 'loke abhijjhādomanassa', 'having': NDE, 'lust': 'rāgo', 'mental': 'cetasikaṃ',
 'mental discomfort': 'cetasikaṃ asātaṃ', 'mental pain': 'cetasikaṃ dukkhaṃ', 'mind': 'cittassa',
 'mind-contact': 'cetosamphassa', 'pain': 'dukkhaṃ', 'painful': 'dukkhaṃ', 'painful experience': 'dukkhaṃ vedayitaṃ',
 'painful experience born': 'cetosamphassajaṃ asātaṃ dukkhaṃ vedayitaṃ', 'painful feeling': 'dukkhā vedanā',
 'painful feeling born': 'cetosamphassajā asātā dukkhā vedanā', 'passion': 'sārāgo', 'quieted': 'vūpasantā',
 'regard': 'loke', 'removed': 'Vineyya', 'removed covetousness': 'Vineyya / abhijjhā', 'rest': 'atthaṅgatā',
 'stilled': 'santā', 'therefore': 'Tena', 'therein': 'Tattha', 'thoroughly': 'paṭivinītā',
 'uncomfortable': 'asātaṃ', 'uncomfortable painful': 'asātaṃ dukkhaṃ',
 'uncomfortable painful experience': 'asātaṃ dukkhaṃ vedayitaṃ', 'uncomfortable painful feeling': 'asātā dukkhā vedanā',
}
# second-round world explanation also repeats the glossed words "Anupassīti … viharatīti … ātāpīti …"
WORLD2 = dict(WORLD, **{'ardent': 'ātāpī', 'clearly': 'sampajāno', 'comprehending': 'sampajāno',
                        'contemplating': 'Anupassī', 'dwells': 'viharatīti', 'mindful': 'satimā'})
HEAD = lambda word, part: {  # sub-chapter headings "Xānupassanāniddeso"
 'contemplating': 'ānupassanā', 'exposition': 'niddeso', 'Exposition of Contemplating': 'ānupassanāniddeso'}
# Abhidhamma classification (2-375 .. 2-385)
ABH = {
 'abandoning': 'pahānāya', 'abandoning of views': 'diṭṭhigatānaṃ pahānāya', 'absorption': 'jhānaṃ',
 'associated': 'sampayuttā', 'awakening': 'sambojjhaṅgo', 'awakening factor': 'sambojjhaṅgo', 'beyond': 'uttaraṃ',
 'body': 'kāye', 'contemplating': 'ānupassī', 'contemplating feelings': 'vedanānupassī',
 'contemplating mental': 'dhammānupassī', 'contemplating mental objects': 'dhammānupassī',
 'contemplating the body': 'kāyānupassī', 'contemplating the mind': 'cittānupassī', 'develops': 'bhāveti',
 'develops the meditative': 'jhānaṃ bhāveti', 'difficult': 'dukkhapaṭipadaṃ', 'difficult practice': 'dukkhapaṭipadaṃ',
 'direct': 'ābhiññaṃ', 'direct knowledge': 'ābhiññaṃ', 'dismantling': 'apacaya', 'dwell': 'viharati',
 'dwells': 'viharati', 'enters': 'upasampajja', 'enters and dwells': 'upasampajja viharati',
 'factor': 'sambojjhaṅgo', 'factor of mindfulness': 'satisambojjhaṅgo', 'feelings': 'vedanāsu',
 'feelings in feelings': 'vedanāsu vedanānupassī', 'foundation': 'paṭṭhānaṃ',
 'foundation of mindfulness': 'satipaṭṭhānaṃ', 'knowledge': 'ābhiññaṃ', 'leading to dismantling': 'apacayagāmiṃ',
 'meditative': 'jhānaṃ', 'meditative absorption': 'jhānaṃ', 'Meditative absorption': 'jhānaṃ',
 'mental': 'dhammesu', 'mental objects': 'dhammesu', 'mind': 'citte', 'mindfulness': 'sati', 'monk': 'bhikkhu',
 'monk dwell': 'bhikkhu / viharati', 'objects': 'dhammesu', 'objects in mental': 'dhammesu', 'occasion': 'samaye',
 'path': 'magga', 'path factor': 'maggaṅgaṃ', 'pleasures': 'kāmehi', 'practice': 'paṭipadaṃ',
 'practice and slow': 'paṭipadaṃ dandhābhiññaṃ', 'reaching': 'pattiyā', 'recollection': 'anussati',
 'remaining': 'Avasesā', 'remaining things': 'Avasesā dhammā', 'right': 'sammā', 'secluded': 'vivicceva',
 'secluded from sense': 'vivicceva kāmehi', 'sense': 'kāmehi', 'sense pleasures': 'kāmehi', 'slow': 'dandhābhiññaṃ',
 'slow direct': 'dandhābhiññaṃ', 'slow direct knowledge': 'dandhābhiññaṃ', 'stage': 'bhūmiyā', 'therein': 'Tattha',
 'things': 'dhammā', 'views': 'diṭṭhigatānaṃ',
 # result-round additions (2-381 .. 2-385)
 'contact': 'phasso', 'developed': 'bhāvitattā', 'done': 'katattā', 'emptiness': 'suññataṃ',
 'non-distraction': 'avikkhepo', 'things are wholesome': 'dhammā kusalā', 'wholesome': 'kusalā',
 'wholesome meditative': 'kusalassa jhānassa', 'wholesome meditative absorption': 'kusalassa jhānassa',
}
def ABHX(anupassi):
    m = dict(ABH)
    m['dwell contemplating'] = f'{anupassi} viharati'
    m['dwell contemplating feelings'] = f'{anupassi} viharati'
    m['dwell contemplating mental'] = f'{anupassi} viharati'
    m['monk dwell contemplating'] = f'bhikkhu / {anupassi} viharati'
    return m
QA = {'answers': NDE, 'questions': 'Pañhā', 'Questions and Answers': 'Pañhāpucchakaṃ', 'section': NDE,
      'Section of Questions': 'Pañhāpucchakaṃ'}

M = {}
M['2-7-0'] = {'analysis': 'vibhaṅgo', 'foundations': 'paṭṭhāna', 'foundations of mindfulness': 'Satipaṭṭhāna',
              'mindfulness': 'Satipaṭṭhānavibhaṅgo'}  # sati+upaṭṭhāna sandhi: whole compound
M['2-7-1-0'] = {'classification': 'bhājanīyaṃ', 'discourses': 'Suttanta'}
M['2-355'] = dict(FOURFOLD, **{
 'body both internally': 'ajjhattabahiddhā kāye', 'body externally': 'bahiddhā kāye',
 'body internally': 'ajjhattaṃ kāye', 'externally': 'bahiddhā',
 'feelings both internally': 'ajjhattabahiddhā vedanāsu', 'feelings externally': 'bahiddhā vedanāsu',
 'feelings internally': 'ajjhattaṃ vedanāsu', 'internally': 'ajjhattaṃ', 'internally and externally': 'ajjhattabahiddhā',
 'mental objects externally': 'bahiddhā dhammesu', 'mind both internally': 'ajjhattabahiddhā citte',
 'mind externally': 'bahiddhā citte', 'mind internally': 'ajjhattaṃ citte'})
M['2-7-1-1-0'] = dict(HEAD(0, 0), **{'body': 'Kāyānupassanāniddeso', 'contemplating the body': 'Kāyānupassanā'})
M['2-356'] = dict(PRACTICE('kāye', 'kāyānupassī'), **{
 'bile': 'pittaṃ', 'blood': 'lohitaṃ', 'body': 'kāye', 'body both internally': 'ajjhattabahiddhā kāye',
 'body externally': 'bahiddhā kāye', 'body hairs': 'lomā', 'body head': 'kāye kesā',
 'body internally': 'ajjhattaṃ kāye', 'bone': 'aṭṭhi', 'bones': 'aṭṭhi', 'contemplating the body': 'kāyānupassī',
 'contents': 'udariyaṃ', 'enclosed': 'pariyantaṃ', 'excrement': 'karīsaṃ', 'fat': 'medo', 'feet': 'pāda',
 'flesh': 'maṃsaṃ', 'fluid': 'lasikā', 'grease': 'vasā', 'hairs': 'kesā', 'head': 'kesamatthakā',
 'heart': 'hadayaṃ', 'impurity': 'asucino', 'intestines': 'antaṃ', 'joints': 'lasikā', 'kidneys': 'vakkaṃ',
 'kinds': 'pakārassa', 'liver': 'yakanaṃ', 'lungs': 'papphāsaṃ', 'marrow': 'miñjaṃ', 'membranes': 'kilomakaṃ',
 'mesentery': 'antaguṇaṃ', 'nails': 'nakhā', 'person': 'atthissa', 'phlegm': 'semhaṃ', 'pus': 'pubbo',
 'reviews': 'paccavekkhati', 'saliva': 'kheḷo', 'sinews': 'nhāru', 'skin': 'taco', 'snot': 'siṅghāṇikā',
 'soles': 'talā', 'spleen': 'pihakaṃ', 'stomach': 'udariyaṃ', 'sweat': 'sedo', 'tears': 'assu', 'teeth': 'dantā',
 'top': 'matthakā', 'urine': 'mutta'})
M['2-357'] = dict(WISDOM, **{'contemplating': 'anupassī', 'contemplation': 'anupassanā'})
M['2-358'] = dict(DWELLS)
M['2-359'] = dict(ENDOWED, **{
 'ardent': 'ātāpī', 'ardour': 'ātāpo', 'effort': 'vāyāmo', 'initiation': 'ārambho',
 'initiation of energy': 'vīriyārambho', 'mental': 'cetasiko', 'mental initiation': 'cetasiko vīriyārambho'})
M['2-360'] = dict(WISDOM, **{
 'clear': 'sampajaññaṃ', 'clear comprehension': 'sampajaññaṃ', 'clearly': 'sampajāno',
 'comprehending': 'sampajāno', 'comprehension': 'sampajaññaṃ'})
M['2-361'] = dict(ENDOWED, **{'mindful': 'satimā', 'mindfulness': 'sati', 'recollection': 'anussati'})
M['2-362'] = dict(WORLD, **{'body': 'kāyo', 'contemplating the body': 'Kāyānupassanā'})
M['2-7-1-2-0'] = dict(HEAD(0, 0), **{'contemplating feelings': 'Vedanānupassanā', 'feelings': 'Vedanānupassanāniddeso'})
M['2-363'] = dict(PRACTICE('vedanāsu', 'vedanānupassī'), **{
 'contemplating feelings': 'vedanānupassī', 'dwell contemplating feelings': 'vedanānupassī viharati',
 'dwells contemplating feelings': 'vedanānupassī viharati', 'feel': 'vedayāmī', 'feeling': 'vedayamāno',
 'feeling a worldly': 'sāmisaṃ / vedayamāno', 'feeling an unworldly': 'nirāmisaṃ / vedayamāno',
 'feelings': 'vedanāsu', 'feelings both internally': 'ajjhattabahiddhā vedanāsu',
 'feelings externally': 'bahiddhā vedanāsu', 'feelings in feelings': 'vedanāsu vedanānupassī',
 'feelings internally': 'ajjhattaṃ vedanāsu', 'feels': 'vedayatī', 'mind to feelings': 'vedanāsu cittaṃ',
 'neither-painful-nor-pleasant': 'adukkhamasukhaṃ', 'painful': 'dukkhaṃ', 'painful feeling': 'dukkhaṃ vedanaṃ',
 'pleasant': 'sukhaṃ', 'pleasant feeling': 'sukhaṃ vedanaṃ', 'unworldly': 'nirāmisaṃ',
 'unworldly painful': 'nirāmisaṃ dukkhaṃ', 'unworldly painful feeling': 'nirāmisaṃ dukkhaṃ vedanaṃ',
 'unworldly pleasant': 'nirāmisaṃ sukhaṃ', 'unworldly pleasant feeling': 'nirāmisaṃ sukhaṃ vedanaṃ',
 'worldly': 'sāmisaṃ', 'worldly painful': 'sāmisaṃ dukkhaṃ', 'worldly painful feeling': 'sāmisaṃ dukkhaṃ vedanaṃ',
 'worldly pleasant': 'sāmisaṃ sukhaṃ', 'worldly pleasant feeling': 'sāmisaṃ sukhaṃ vedanaṃ'})
M['2-364'] = dict(WORLD2, **{'contemplating feelings': 'Vedanānupassanā', 'feelings': 'Vedanānupassanāniddeso'})
M['2-7-1-3-0'] = dict(HEAD(0, 0), **{'contemplating the mind': 'Cittānupassanā', 'mind': 'Cittānupassanāniddeso'})
M['2-365'] = dict(PRACTICE('citte', 'cittānupassī'), **{
 'concentrated': 'samāhitaṃ', 'concentrated mind': 'samāhitaṃ vā cittaṃ', 'contemplating the mind': 'cittānupassī',
 'contracted': 'saṃkhittaṃ', 'contracted mind': 'saṃkhittaṃ vā cittaṃ', 'delusion': 'mohaṃ',
 'distracted': 'vikkhittaṃ', 'distracted mind': 'vikkhittaṃ vā cittaṃ', 'expanded': 'mahaggataṃ',
 'expanded mind': 'mahaggataṃ vā cittaṃ', 'freed': 'vimuttaṃ', 'freed mind': 'vimuttaṃ vā cittaṃ', 'hate': 'dosaṃ',
 'lust': 'rāgaṃ', 'mind': 'citte', 'mind both internally': 'ajjhattabahiddhā citte', 'mind externally': 'bahiddhā citte',
 'mind internally': 'ajjhattaṃ citte', 'mind with delusion': 'samohaṃ vā cittaṃ',
 'mind with hate': 'sadosaṃ vā cittaṃ', 'mind with lust': 'sarāgaṃ vā cittaṃ',
 'mind without delusion': 'vītamohaṃ vā cittaṃ', 'mind without hate': 'vītadosaṃ vā cittaṃ',
 'mind without lust': 'vītarāgaṃ vā cittaṃ', 'surpassable': 'sauttaraṃ', 'surpassable mind': 'sauttaraṃ vā cittaṃ',
 'unconcentrated': 'asamāhitaṃ', 'unconcentrated mind': 'asamāhitaṃ vā cittaṃ', 'unexpanded': 'amahaggataṃ',
 'unexpanded mind': 'amahaggataṃ vā cittaṃ', 'unfreed': 'avimuttaṃ', 'unfreed mind': 'avimuttaṃ vā cittaṃ',
 'unsurpassable': 'anuttaraṃ', 'unsurpassable mind': 'anuttaraṃ vā cittaṃ'})
M['2-366'] = dict(WORLD2, **{'contemplating the mind': 'Cittānupassanā', 'mind': 'cittaṃ'})
M['2-7-1-4-0'] = dict(HEAD(0, 0), **{
 'contemplating mental': 'Dhammānupassanā', 'contemplating mental objects': 'Dhammānupassanā',
 'mental': 'Dhammānupassanāniddeso', 'mental objects': 'Dhammānupassanāniddeso', 'objects': 'Dhammānupassanāniddeso'})
M['2-367'] = dict(PRACTICE('dhammesu', 'dhammānupassī'), **{
 'abandoned': 'pahīnassa', 'abandoned doubt': 'pahīnāya vicikicchāya', 'abandoned sense': 'pahīnassa kāmacchandassa',
 'abandoned sense desire': 'pahīnassa kāmacchandassa', 'again': NDE, 'arise': 'anuppādo', 'arisen': 'uppannassa',
 'arisen awakening': 'uppannassa satisambojjhaṅgassa', 'arisen awakening factor': 'uppannassa satisambojjhaṅgassa',
 'arisen doubt': 'uppannāya vicikicchāya', 'arisen sense': 'uppannassa kāmacchandassa',
 'arisen sense desire': 'uppannassa kāmacchandassa', 'arises': 'uppādo', 'awakening': 'sambojjhaṅgaṃ',
 'awakening factor': 'sambojjhaṅgaṃ', 'concentration': 'samādhi',
 'concentration is present': 'santaṃ / samādhisambojjhaṅgaṃ', 'contemplating mental': 'dhammānupassī',
 'contemplating mental objects': 'dhammānupassī', 'desire': 'chandaṃ', 'desire arises': 'kāmacchandassa uppādo',
 'desire is present': 'santaṃ / kāmacchandaṃ', 'doubt': 'vicikicchaṃ', 'doubt arises': 'vicikicchāya uppādo',
 'doubt is present': 'santaṃ / vicikicchaṃ', 'drowsiness': 'middhaṃ',
 'drowsiness are present': 'santaṃ / thinamiddhaṃ', 'dullness': 'thina', 'dullness and drowsiness': 'thinamiddhaṃ',
 'dwell contemplating mental': 'dhammānupassī viharati', 'dwells contemplating mental': 'dhammānupassī viharati',
 'energy is present': 'santaṃ / vīriyasambojjhaṅgaṃ', 'equanimity': 'upekkhā',
 'equanimity arises': 'upekkhāsambojjhaṅgassa uppādo', 'equanimity is present': 'santaṃ / upekkhāsambojjhaṅgaṃ',
 'factor': 'sambojjhaṅgaṃ', 'factor of concentration': 'samādhisambojjhaṅgaṃ',
 'factor of energy': 'vīriyasambojjhaṅgaṃ', 'factor of equanimity': 'upekkhāsambojjhaṅgaṃ',
 'factor of investigation': 'dhammavicayasambojjhaṅgaṃ', 'factor of joy': 'pītisambojjhaṅgaṃ',
 'factor of mindfulness': 'satisambojjhaṅgaṃ', 'factor of tranquillity': 'passaddhisambojjhaṅgaṃ',
 'ill': 'byāpādaṃ', 'investigation': 'vicaya', 'investigation of things': 'dhammavicaya', 'joy': 'pīti',
 'joy is present': 'santaṃ / pītisambojjhaṅgaṃ', 'mental': 'dhammesu', 'mental objects': 'dhammesu',
 'mental objects externally': 'bahiddhā dhammesu', 'mindfulness': 'sati',
 'mindfulness arises': 'satisambojjhaṅgassa uppādo',
 'mindfulness is perfected': 'satisambojjhaṅgassa bhāvanāya pāripūrī',
 'mindfulness is present': 'santaṃ / satisambojjhaṅgaṃ', 'objects': 'dhammesu', 'objects in mental': 'dhammesu',
 'perfected': 'pāripūrī', 'remorse': 'kukkuccaṃ', 'remorse are present': 'santaṃ / uddhaccakukkuccaṃ',
 'restlessness': 'uddhacca', 'restlessness and remorse': 'uddhaccakukkuccaṃ', 'sense': 'kāma',
 'sense desire': 'kāmacchandaṃ', 'sense desire arises': 'kāmacchandassa uppādo', 'things': 'dhamma',
 'things is present': 'santaṃ / dhammavicayasambojjhaṅgaṃ', 'tranquillity': 'passaddhi',
 'tranquillity is present': 'santaṃ / passaddhisambojjhaṅgaṃ', 'unarisen': 'anuppannassa',
 'unarisen awakening': 'anuppannassa satisambojjhaṅgassa',
 'unarisen awakening factor': 'anuppannassa satisambojjhaṅgassa', 'unarisen doubt': 'anuppannāya vicikicchāya',
 'unarisen doubt arises': 'anuppannāya vicikicchāya uppādo', 'unarisen sense': 'anuppannassa kāmacchandassa',
 'unarisen sense desire': 'anuppannassa kāmacchandassa'})
M['2-368'] = dict(M['2-357'])
M['2-369'] = dict(DWELLS)
M['2-370'] = dict(M['2-359'])
M['2-371'] = dict(M['2-360'])
M['2-372'] = dict(M['2-361'])
M['2-373'] = dict(WORLD, **{
 'classification': 'bhājanīyaṃ', 'contemplating mental': 'Dhammānupassanā',
 'contemplating mental objects': 'Dhammānupassanā', 'discourses': 'Suttanta', 'finished': NDE,
 'mental': 'dhammā', 'mental objects': 'dhammā', 'objects': 'dhammā'})
M['2-7-2-0'] = {'abhidhamma': 'Abhidhamma', 'classification': 'bhājanīyaṃ'}
M['2-374'] = dict(FOURFOLD)
for s, a in [('2-375', 'kāyānupassī'), ('2-376', 'vedanānupassī'), ('2-377', 'cittānupassī'),
             ('2-378', 'dhammānupassī'), ('2-379', 'dhammānupassī'), ('2-381', 'kāyānupassī'),
             ('2-382', 'vedanānupassī'), ('2-383', 'cittānupassī'), ('2-384', 'dhammānupassī'),
             ('2-385', 'dhammānupassī')]:
    M[s] = ABHX(a)
M['2-385'].update({'abhidhamma': 'Abhidhamma', 'classification': 'bhājanīyaṃ', 'finished': NDE})
M['2-380'] = dict(FOURFOLD)
M['2-7-3-0'] = dict(QA)
M['2-386'] = dict(FOURFOLD)
M['2-387'] = {
 'conflict': 'saraṇā', 'foundations': 'paṭṭhānānaṃ', 'foundations of mindfulness': 'satipaṭṭhānānaṃ',
 'free': 'araṇā', 'involve': 'saraṇā', 'mindfulness': 'satipaṭṭhānānaṃ', 'neutral': 'abyākatā', 'unwholesome': 'akusalā',
 'wholesome': 'kusalā',
}
M['2-7-3-1-0'] = {'triads': 'Tikaṃ'}
M['2-388'] = {
 'abandoned': 'pahātabbā', 'able': 'upādāniyā', 'accompanied': 'sahagatā',
 'accompanied by equanimity': 'upekkhāsahagatā', 'accompanied by happiness': 'sukhasahagatā',
 'accompanied by joy': 'pītisahagatā', 'accumulation': 'ācaya', 'arise': 'uppādino', 'arisen': 'uppannā',
 'associated': 'sampayuttā', 'belong': NDE, 'beyond': 'asekkhā', 'birth': NDE, 'cause': 'hetukā',
 'causes': 'hetukā', 'clung': 'upādāniyā', 'connected': 'saṃkilesikā', 'connected with defilement': 'saṃkilesikā',
 'defilement': 'saṃkilesikā', 'describable': 'vattabbā', 'dismantling': 'apacaya', 'dominant': 'ādhipatino',
 'dominant factor': 'ādhipatino', 'due to arise': 'uppādino', 'equanimity': 'upekkhā', 'examination': 'vicāra',
 'external': 'bahiddhā', 'external objects': 'Bahiddhārammaṇā', 'factor': 'ādhipatino', 'feeling': 'vedanāya',
 'fixed': 'niyatā', 'future object': 'anāgatārammaṇā', 'happiness': 'sukha', 'having': NDE, 'internal': 'ajjhattā',
 'internal and external': 'ajjhattabahiddhā', 'invisible': 'Anidassana', 'invisible and offer': 'Anidassanaappaṭighā',
 'joy': 'pīti', 'leading to dismantling': 'apacayagāmino', 'measureless': 'Appamāṇā',
 'measureless objects': 'Appamāṇārammaṇā', 'meditative': 'bhāvanāya', 'meditative development': 'bhāvanāya',
 'neither-painful-nor-pleasant': 'adukkhamasukhāya', 'neutral': 'abyākatā', 'object': 'ārammaṇā',
 'objects': 'ārammaṇā', 'past object': 'atītārammaṇā', 'path': 'magga', 'pleasant': 'sukhāya',
 'pleasant feeling': 'sukhāya vedanāya', 'present object': 'paccuppannārammaṇā', 'refined': 'Paṇītā',
 'resistance': 'appaṭighā', 'rightness': 'sammatta', 'seeing': 'dassanena', 'subject to result': 'vipākadhammadhammā',
 'things': 'dhammā', 'things subject': 'vipākadhammadhammā', 'thought': 'vitakka', 'training': 'sekkhā',
 'undefiled': 'Asaṃkiliṭṭha', 'unfixed': 'aniyatā', 'wholesome': 'kusalā',
}
M['2-7-3-2-0'] = {'pairs': 'Dukaṃ'}
M['2-389'] = dict(QA, **{
 'abandoned': 'pahātabbā', 'accompanied': 'sahagatā', 'accompanied by equanimity': 'upekkhāsahagatā',
 'accompanied by happiness': 'sukhasahagatā', 'accompanied by joy': 'pītisahagatā', 'along': 'ānuparivattino',
 'analysis': 'vibhaṅgo', 'arise': 'sahabhuno', 'associated': 'sampayuttā', 'belong': NDE, 'beyond': 'uttarā',
 'birth': NDE, 'cannot': 'na', 'causes': 'hetukā', 'clinging': 'upādānā', 'conditioned': 'Saṅkhatā',
 'conflict': 'Araṇā', 'conjoined': 'saṃsaṭṭhā', 'defilements': 'kilesā', 'derived': 'upādā', 'describable': 'vattabbā',
 'dissociated': 'vippayuttā', 'equanimity': 'upekkhā', 'examination': 'vicārā', 'external': 'Bāhirā',
 'factors': 'Cetasikā', 'fetters': 'saṃyojanā', 'fine-material': 'rūpāvacarā', 'fine-material sphere': 'rūpāvacarā',
 'finished': 'niṭṭhito', 'fixed': 'niyatā', 'floods': 'oghā', 'follow': 'ānuparivattino', 'foundations': 'paṭṭhāna',
 'foundations of mindfulness': 'Satipaṭṭhāna', 'free': 'Araṇā', 'grasping': 'parāmāsā', 'happiness': 'sukha',
 'having': 'Sahetukā', 'hindrances': 'nīvaraṇā', 'immaterial': 'Arūpā', 'immaterial sphere': 'arūpāvacarā',
 'invisible': 'Anidassanā', 'joy': 'pīti', 'known': 'viññeyyā', 'means': 'Kenaci', 'meditative': 'bhāvanāya',
 'meditative development': 'bhāvanāya', 'mental': 'Cetasikā', 'mental factors': 'Cetasikā', 'mental taints': 'āsavā',
 'mind': 'Citta', 'mindfulness': 'Satipaṭṭhānavibhaṅgo', 'minds': 'cittā', 'objects': 'ārammaṇā', 'originated': 'samuṭṭhānā',
 'resistance': 'Appaṭighā', 'roots': 'hetū', 'seeing': 'dassanena', 'sense': 'kāmāvacarā',
 'sense sphere': 'kāmāvacarā', 'sphere': 'āvacarā', 'subject to mental': 'sāsavā', 'taints': 'āsavā',
 'thought': 'vitakkā', 'ties': 'ganthā', 'together': 'saha', 'unfixed': 'aniyatā', 'unsurpassed': 'Anuttarā',
 'wrong': 'parāmāsā', 'wrong grasping': 'parāmāsā', 'yokes': 'yogā',
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
