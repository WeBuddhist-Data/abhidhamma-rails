import pathlib, re
d = pathlib.Path(__file__).parent
root = d.parents[4]
ch = '8-sammappadhanavibhango'
NDE = '(no direct equivalent)'

# sammā+padhāna is a sandhi compound (sammappadhāna): "right" takes the whole compound,
# "effort(s)" the trailing part.

# ---- shared blocks -------------------------------------------------------
# the five verbs "chandaṃ janeti vāyamati vīriyaṃ ārabhati cittaṃ paggaṇhāti padahati"
VERBS = {
 'desire': 'chandaṃ', 'endeavour': 'padahati', 'endeavours': 'padahati', 'exert': 'paggaṇhāti',
 'exert his mind': 'cittaṃ paggaṇhāti', 'exerts': 'paggaṇhāti', 'exerts his mind': 'cittaṃ paggaṇhāti',
 'generate': 'janeti', 'generate desire': 'chandaṃ janeti', 'generates': 'janeti', 'generates desire': 'chandaṃ janeti',
 'initiate': 'ārabhati', 'initiate energy': 'vīriyaṃ ārabhati', 'initiates': 'ārabhati',
 'initiates energy': 'vīriyaṃ ārabhati', 'mind': 'cittaṃ', 'monk': 'bhikkhu', 'monk generate': 'bhikkhu / janeti',
 'monk generate desire': 'bhikkhu / chandaṃ janeti', 'monk generates': 'bhikkhu / janeti',
 'monk generates desire': 'bhikkhu / chandaṃ janeti', 'strive': 'vāyamati', 'strives': 'vāyamati',
 'things': 'dhammānaṃ',
}
# the same verbs quoted as lemmata with iti ("Chandaṃ janetīti…pe… padahatīti"): whole sandhi form
VERBS_ITI = dict(VERBS, **{
 'desire': 'Chandaṃ', 'endeavours': 'padahatīti', 'exerts': 'paggaṇhātīti', 'exerts his mind': 'cittaṃ paggaṇhātīti',
 'generates': 'janetīti', 'generates desire': 'Chandaṃ janetīti', 'initiates': 'ārabhatīti',
 'initiates energy': 'vīriyaṃ ārabhatīti', 'strives': 'vāyamatīti'})
UNW = {'evil': 'pāpakānaṃ', 'unwholesome': 'akusalānaṃ', 'unwholesome things': 'akusalānaṃ dhammānaṃ'}
WH = {'wholesome': 'kusalānaṃ', 'wholesome things': 'kusalānaṃ dhammānaṃ'}
PERSIST = {'expansion': 'vepullāya', 'non-confusion': 'asammosāya', 'perfection': 'pāripūriyā',
           'persistence': 'ṭhitiyā'}
FOUR = dict(VERBS, **UNW, **WH, **PERSIST, **{
 'abandoning': 'pahānāya', 'arisen': 'uppannānaṃ', 'arising': 'uppādāya', 'efforts': 'padhānā',
 'non-arising': 'anuppādāya', 'right': 'sammappadhānā'})
# "Tīṇi akusalamūlāni … taṃsamuṭṭhānaṃ kāyakammaṃ vacīkammaṃ manokammaṃ"
ROOTS = dict(VERBS, **{
 'aggregate': 'khandho', 'aggregate of consciousness': 'viññāṇakkhandho',
 'Aggregate of Consciousness': 'viññāṇakkhandho', 'aggregate of feeling': 'vedanākkhandho',
 'aggregate of mental': 'saṅkhārakkhandho', 'Aggregate of Mental': 'saṅkhārakkhandho',
 'Aggregate of Perception': 'saññākkhandho', 'aggregate of perception': 'saññākkhandho',
 'associated': 'sampayutto', 'bodily': 'kāya', 'bodily action': 'kāyakammaṃ', 'consciousness': 'viññāṇa',
 'feeling': 'vedanā', 'formations': 'saṅkhāra', 'mental': 'saṅkhāra', 'mental action': 'manokammaṃ',
 'mental action originated': 'samuṭṭhānaṃ / manokammaṃ', 'Mental Formations': 'saṅkhāra',
 'mental formations': 'saṅkhāra', 'originated': 'samuṭṭhānaṃ', 'perception': 'saññā', 'roots': 'mūlāni',
 'therein': 'Tattha', 'verbal': 'vacī', 'verbal action': 'vacīkammaṃ'})
ROOTS_UNW = dict(ROOTS, **UNW, **{
 'defilements': 'kilesā', 'delusion': 'moho', 'greed': 'lobho', 'hate': 'doso', 'stand': 'ekaṭṭhā',
 'together': 'ekaṭṭhā', 'unwholesome roots': 'akusalamūlāni'})
ROOTS_WH = dict(ROOTS, **WH, **{
 'non-delusion': 'amoho', 'non-greed': 'alobho', 'non-hate': 'adoso', 'wholesome roots': 'kusalamūlāni'})
CHANDA = {
 'act': 'kattu', 'brings': 'sañjaneti', 'desire': 'chando', 'dhamma': 'dhamma', 'forth': 'sañjaneti',
 'generates': 'janeti', 'generates desire': 'chandaṃ janeti', 'generates this desire': 'Imaṃ chandaṃ janeti',
 'produces': 'nibbatteti', 'rouses': 'samuṭṭhapeti', 'therefore': 'Tena', 'therein': 'Tattha', 'wholesome': 'kusalo',
 'wholesome desire': 'kusalo dhammacchando', 'wish': 'kamyatā', 'wishing': 'chandikatā',
}
ENERGYDEF = {  # "Yo cetasiko vīriyārambho…pe… sammāvāyāmo"
 'effort': 'vāyāmo', 'initiation': 'ārambho', 'initiation of energy': 'vīriyārambho', 'mental': 'cetasiko',
 'mental initiation': 'cetasiko vīriyārambho', 'right': 'sammā', 'therefore': 'Tena', 'therein': 'Tattha',
}
PATHF = {  # "… vīriyasambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ"
 'awakening': 'sambojjhaṅgo', 'awakening factor': 'sambojjhaṅgo', 'factor': 'sambojjhaṅgo',
 'factor of energy': 'vīriyasambojjhaṅgo', 'path': 'magga', 'path factor': 'maggaṅgaṃ',
}
ENDOWED = {'complete': 'sampanno', 'endowed': 'upeto', 'fully': 'samupeto', 'fully endowed': 'samupeto',
           'furnished': 'samannāgato', 'having': NDE, 'possessed': 'upapanno'}
STRIVE = dict(ENERGYDEF, **ENDOWED, **{'strives': 'Vāyamatīti', 'striving': 'vāyāmo'})
ENERGY = dict(ENERGYDEF, **{
 'cultivates': 'bahulīkaroti', 'develops': 'bhāveti', 'initiates': 'ārabhati', 'initiates energy': 'vīriyaṃ ārabhati',
 'initiates this energy': 'Imaṃ vīriyaṃ ārabhati', 'practises': 'āsevati', 'undertakes': 'samārabhati'})
MIND = {
 'activity': 'mānasaṃ', 'consciousness element': 'viññāṇadhātu', 'corresponding': 'tajjā', 'element': 'dhātu',
 'exerts': 'paggaṇhāti', 'exerts his mind': 'cittaṃ paggaṇhāti', 'exerts this mind': 'Imaṃ cittaṃ paggaṇhāti',
 'fully': 'sampaggaṇhāti', 'fully exerts': 'sampaggaṇhāti', 'mental': 'mānasaṃ', 'mental activity': 'mānasaṃ',
 'mentality': 'mano', 'mind': 'cittaṃ', 'mind-consciousness': 'manoviññāṇa',
 'mind-consciousness element': 'manoviññāṇadhātu', 'supports': 'upatthambheti', 'therefore': 'Tena',
 'therein': 'Tattha', 'upholds': 'paccupatthambheti',
}
ENDEAV = dict(ENERGYDEF, **ENDOWED, **{'endeavour': 'padhānaṃ', 'endeavours': 'Padahatīti'})
ENDEAV_ITI = dict(ENDEAV, **VERBS_ITI)
ENDEAV_ITI['therefore'] = 'Tena'; ENDEAV_ITI['therein'] = 'Tattha'; ENDEAV_ITI['endeavour'] = 'padhānaṃ'
ENDEAV_ITI['endeavours'] = 'padahatīti'; ENDEAV_ITI['mind'] = 'cittaṃ'
ATTHI = {'expansion': 'vepullaṃ', 'non-confusion': 'asammoso', 'perfection': 'pāripūrī', 'persistence': 'ṭhiti'}
# Abhidhamma classification (2-409 …)
ABH = dict(VERBS, **{
 'abandoning': 'pahānāya', 'abandoning of views': 'diṭṭhigatānaṃ pahānāya', 'absorption': 'jhānaṃ',
 'beyond': 'uttaraṃ', 'develops': 'bhāveti', 'develops the meditative': 'jhānaṃ bhāveti',
 'difficult': 'dukkhapaṭipadaṃ', 'difficult practice': 'dukkhapaṭipadaṃ', 'direct': 'ābhiññaṃ',
 'direct knowledge': 'ābhiññaṃ', 'dismantling': 'apacaya', 'dwells': 'viharati', 'enters': 'upasampajja',
 'enters and dwells': 'upasampajja viharati', 'knowledge': 'ābhiññaṃ', 'leading to dismantling': 'apacayagāmiṃ',
 'meditative': 'jhānaṃ', 'meditative absorption': 'jhānaṃ', 'Meditative absorption': 'jhānaṃ',
 'non-arising': 'anuppādāya', 'arising': 'uppādāya', 'occasion': 'samaye', 'occasion he generates': 'samaye / janeti',
 'pleasures': 'kāmehi', 'practice': 'paṭipadaṃ', 'practice and slow': 'paṭipadaṃ dandhābhiññaṃ',
 'reaching': 'pattiyā', 'secluded': 'vivicceva', 'secluded from sense': 'vivicceva kāmehi', 'sense': 'kāmehi',
 'sense pleasures': 'kāmehi', 'slow': 'dandhābhiññaṃ', 'slow direct': 'dandhābhiññaṃ',
 'slow direct knowledge': 'dandhābhiññaṃ', 'stage': 'bhūmiyā', 'views': 'diṭṭhigatānaṃ',
})
RIGHTEFF = dict(ENERGYDEF, **PATHF, **{  # "katamaṃ sammappadhānaṃ? … Avasesā dhammā sammappadhānasampayuttā"
 'associated': 'sampayuttā', 'effort': 'padhānaṃ', 'remaining': 'Avasesā', 'remaining things': 'Avasesā dhammā',
 'right': 'sammappadhānaṃ', 'things': 'dhammā'})
QA = {'answers': NDE, 'questions': 'Pañhā', 'Questions and Answers': 'Pañhāpucchakaṃ', 'section': NDE,
      'Section of Questions': 'Pañhāpucchakaṃ'}

M = {}
M['2-8-0'] = {'analysis': 'vibhaṅgo', 'efforts': 'padhāna', 'right': 'Sammappadhānavibhaṅgo'}
M['2-8-1-0'] = {'classification': 'bhājanīyaṃ', 'discourses': 'Suttanta'}
M['2-390'] = dict(FOUR)
M['2-391'] = dict(ROOTS_UNW, **{'arisen': 'anuppannānaṃ', 'non-arising': 'anuppādāya'})
M['2-392'] = dict(CHANDA)
M['2-393'] = dict(STRIVE)
M['2-394'] = dict(ENERGY)
M['2-395'] = dict(MIND)
M['2-396'] = dict(ENDEAV)
M['2-397'] = dict(ROOTS_UNW, **{'abandoning': 'pahānāya', 'arisen': 'uppannānaṃ'})
M['2-398'] = dict(CHANDA)
M['2-399'] = dict(STRIVE)
M['2-400'] = dict(ENERGY)
M['2-401'] = dict(MIND)
M['2-402'] = dict(ENDEAV)
M['2-403'] = dict(ROOTS_WH, **{'arisen': 'anuppannānaṃ', 'arising': 'uppādāya'})
M['2-404'] = dict(ENDEAV_ITI)
M['2-405'] = dict(ROOTS_WH, **PERSIST, **{'arisen': 'uppannānaṃ'})
M['2-406'] = dict(ATTHI)
M['2-407'] = dict(ENDEAV_ITI, **{'classification': 'bhājanīyaṃ', 'discourses': 'Suttanta', 'finished': NDE})
M['2-8-2-0'] = {'abhidhamma': 'Abhidhamma', 'classification': 'bhājanīyaṃ'}
M['2-408'] = dict(FOUR)
M['2-409'] = dict(ABH, **UNW, **{'arisen': 'anuppannānaṃ'})
M['2-410'] = dict(CHANDA)
M['2-411'] = dict(STRIVE, **PATHF)
M['2-412'] = dict(ENERGY, **PATHF)
M['2-413'] = dict(MIND)
M['2-414'] = dict(RIGHTEFF, **{'endeavours': 'Padahatīti'})
M['2-415'] = dict(ABH, **UNW, **{'arisen': 'uppannānaṃ'})
M['2-416'] = dict(VERBS_ITI, **RIGHTEFF)
M['2-417'] = dict(ABH, **WH, **{'arisen': 'anuppannānaṃ'})
M['2-418'] = dict(VERBS_ITI, **RIGHTEFF)
M['2-419'] = dict(ABH, **WH, **PERSIST, **{'arisen': 'uppannānaṃ'})
M['2-420'] = dict(ATTHI)
M['2-421'] = dict(CHANDA)
M['2-422'] = dict(STRIVE, **PATHF)
M['2-423'] = dict(ENERGY, **PATHF)
M['2-424'] = dict(MIND)
M['2-425'] = dict(RIGHTEFF, **{'endeavours': 'Padahatīti'})
M['2-426'] = dict(ABH, **RIGHTEFF, **{'abhidhamma': 'Abhidhamma', 'classification': 'bhājanīyaṃ',
                                       'finished': NDE, 'monk': 'bhikkhu'})
M['2-8-3-0'] = dict(QA)
M['2-427'] = dict(FOUR)
M['2-428'] = {'conflict': 'saraṇā', 'efforts': 'padhānānaṃ', 'free': 'araṇā', 'involve': 'saraṇā',
              'neutral': 'abyākatā', 'right': 'sammappadhānānaṃ', 'unwholesome': 'akusalā', 'wholesome': 'kusalā'}
M['2-8-3-1-0'] = {'triads': 'Tikaṃ'}
M['2-429'] = {
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
M['2-8-3-2-0'] = {'pairs': 'Dukaṃ'}
M['2-430'] = dict(QA, **{
 'abandoned': 'pahātabbā', 'accompanied': 'sahagatā', 'accompanied by equanimity': 'upekkhāsahagatā',
 'accompanied by happiness': 'sukhasahagatā', 'accompanied by joy': 'pītisahagatā', 'along': 'ānuparivattino',
 'analysis': 'vibhaṅgo', 'arise': 'sahabhuno', 'associated': 'sampayuttā', 'belong': NDE, 'beyond': 'uttarā',
 'birth': NDE, 'cannot': 'na', 'causes': 'hetukā', 'clinging': 'upādānā', 'conditioned': 'Saṅkhatā',
 'conflict': 'Araṇā', 'conjoined': 'saṃsaṭṭhā', 'defilements': 'kilesā', 'derived': 'upādā', 'describable': 'vattabbā',
 'dissociated': 'vippayuttā', 'efforts': 'padhāna', 'equanimity': 'upekkhā', 'examination': 'vicārā',
 'external': 'Bāhirā', 'factors': 'Cetasikā', 'fetters': 'saṃyojanā', 'fine-material': 'rūpāvacarā',
 'fine-material sphere': 'rūpāvacarā', 'finished': 'niṭṭhito', 'fixed': 'Niyatā', 'floods': 'oghā',
 'follow': 'ānuparivattino', 'free': 'Araṇā', 'grasping': 'parāmāsā', 'happiness': 'sukha', 'having': 'Sahetukā',
 'hindrances': 'nīvaraṇā', 'immaterial': 'Arūpā', 'immaterial sphere': 'arūpāvacarā', 'invisible': 'Anidassanā',
 'joy': 'pīti', 'known': 'viññeyyā', 'means': 'Kenaci', 'meditative': 'bhāvanāya', 'meditative development': 'bhāvanāya',
 'mental': 'Cetasikā', 'mental factors': 'Cetasikā', 'mental taints': 'āsavā', 'mind': 'Citta', 'minds': 'cittā',
 'objects': 'ārammaṇā', 'originated': 'samuṭṭhānā', 'resistance': 'Appaṭighā', 'right': 'Sammappadhānavibhaṅgo',
 'roots': 'hetū', 'seeing': 'dassanena', 'sense': 'kāmāvacarā', 'sense sphere': 'kāmāvacarā', 'sphere': 'āvacarā',
 'subject to mental': 'sāsavā', 'taints': 'āsavā', 'thought': 'vitakkā', 'ties': 'ganthā', 'together': 'saha',
 'unsurpassed': 'Anuttarā', 'wrong': 'parāmāsā', 'wrong grasping': 'parāmāsā', 'yokes': 'yogā',
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
