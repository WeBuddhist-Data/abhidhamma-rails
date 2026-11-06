"""Rails translation of chapter 4 (Pairs on Elements)."""
import re,sys
sys.path.insert(0,'pi-6-rails-scripts')
from common import *
import core as C
S={'cakkhu':'the eye element','sota':'the ear element','ghāna':'the nose element','jivhā':'the tongue element','kāya':'the body element','rūpa':'the visible-form element','sadda':'the sound element','gandha':'the scent element','rasa':'the taste element','phoṭṭhabba':'the tangible element','cakkhuviññāṇa':'the eye-consciousness element','sotaviññāṇa':'the ear-consciousness element','ghānaviññāṇa':'the nose-consciousness element','jivhāviññāṇa':'the tongue-consciousness element','kāyaviññāṇa':'the body-consciousness element','mano':'the mind-element','manoviññāṇa':'the mind-consciousness element','dhamma':'the mind-object element'}
D={k+'dhātu':v for k,v in S.items()}
BARE={'cakkhu':'the eye','sotaṃ':'the ear','ghānaṃ':'the nose','jivhā':'the tongue','kāyo':'the body','rūpaṃ':'material form','saddo':'sound','gandho':'scent','raso':'taste','phoṭṭhabbo':'the tangible','mano':'the mind','dhammo':'a phenomenon','cakkhuviññāṇaṃ':'eye-consciousness','sotaviññāṇaṃ':'ear-consciousness','ghānaviññāṇaṃ':'nose-consciousness','jivhāviññāṇaṃ':'tongue-consciousness','kāyaviññāṇaṃ':'body-consciousness','manoviññāṇaṃ':'mind-consciousness'}
N={**D,**BARE}
ACC={'cakkhuñca':'cakkhu','cakkhu ca':'cakkhu','sotañca':'sotaṃ','kāyañca':'kāyo','rūpañca':'rūpaṃ','gandhañca':'gandho','rasañca':'raso','manañca':'mano','dhammañca':'dhammo','cakkhuṃ':'cakkhu'}
CEVA={'cakkhu':'cakkhu','sotañ':'sotaṃ','kāyo':'kāyo','rūpañ':'rūpaṃ','gandho':'gandho','raso':'raso','mano':'mano','dhammo':'dhammo'}
OTHER={'kāyo':('any other body','a body'),'rūpaṃ':('any other material form','material form'),'mano':('any other mind','a mind'),'dhammo':('any other phenomenon','a phenomenon')}
SPEC={'Dibbacakkhu paññācakkhu':('The divine eye and the eye of wisdom','eyes'),'Dibbasotaṃ taṇhāsotaṃ':('The divine ear and the stream of craving','"ear" (sota)'),'Sīlagandho samādhigandho paññāgandho':('The scent of virtue, the scent of concentration and the scent of wisdom','scents'),'Attharaso dhammaraso vimuttiraso':('The taste of meaning, the taste of the Dhamma and the taste of liberation','tastes')}
DH=r'(\w+dhātu)';VB=C.VB
SP={
'Aṭṭhārasa dhātuyo – cakkhudhātu, sotadhātu, ghānadhātu, jivhādhātu, kāyadhātu, rūpadhātu, saddadhātu, gandhadhātu, rasadhātu, phoṭṭhabbadhātu, cakkhuviññāṇadhātu, sotaviññāṇadhātu, ghānaviññāṇadhātu, jivhāviññāṇadhātu, kāyaviññāṇadhātu, manodhātu, manoviññāṇadhātu, dhammadhātu.':'There are eighteen elements – the eye element, the ear element, the nose element, the tongue element, the body element, the visible-form element, the sound element, the scent element, the taste element, the tangible element, the eye-consciousness element, the ear-consciousness element, the nose-consciousness element, the tongue-consciousness element, the body-consciousness element, the mind-element, the mind-consciousness element, the mind-object element.',
'(Yathā āyatanayamake cakkaṃ bandhitaṃ evamidha cakkaṃ bandhitabbaṃ.)':'(Just as the cycle was linked up in the Pairs on Bases, so the cycle should be linked up here.)',
'(Cakkaṃ bandhitabbaṃ).':'(The cycle should be linked up.)','Paṇṇattiuddesavāro.':'The outline of the section on terms.','Paṇṇattiniddesavāro.':'The explanation of the section on terms.','Āmantā.':'Yes.',
'Ghānaṃ dhātu?…Pe… jivhā dhātu?… Kāyo dhātu?… Rūpaṃ dhātu?… Saddo dhātu?… Gandho dhātu?… Raso dhātu?… Phoṭṭhabbo dhātu?…':'Is the nose an element?… is the tongue an element?… Is the body an element?… Is material form an element?… Is sound an element?… Is scent an element?… Is taste an element?… Is the tangible an element?…',
'… Ghānaviññāṇaṃ?…Pe… jivhāviññāṇaṃ?… Kāyaviññāṇaṃ?':'… Nose-consciousness?… tongue-consciousness?… Body-consciousness?',
'… Na ghānaṃ?… Na jivhā?… Na kāyo?… Na rūpaṃ? … Na saddo?… Na gandho?… Na raso?… Na phoṭṭhabbo?':'… Not the nose?… Not the tongue?… Not the body?… Not material form? … Not sound?… Not scent?… Not taste?… Not the tangible?',
'… Na sotaviññāṇaṃ?…Pe… na ghānaviññāṇaṃ?… Na jivhāviññāṇaṃ?':'… Not ear-consciousness?… not nose-consciousness?… Not tongue-consciousness?',
'(Jivhāpi ghānadhātusadisā).':'(The tongue too is like the nose element.)','(Saddo ghānasadiso).':'(Sound is like the nose.)','(Phoṭṭhabbo ghānasadiso).':'(The tangible is like the nose.)',
'Sotaviññāṇaṃ…pe… ghānaviññāṇaṃ… jivhāviññāṇaṃ… kāyaviññāṇaṃ….':'Ear-consciousness… nose-consciousness… tongue-consciousness… body-consciousness…',
'Na jivhā… (saṃkhittaṃ ⟦0⟧, ubhato āmantā).':'Not the tongue… (Abbreviated ⟦0⟧; the answer is "Yes" in both directions.)',
'Na saddo…pe… na gandho na gandhadhātūti?':'Not sound… is what is not scent not the scent element?',
'Na phoṭṭhabbo…pe… na cakkhuviññāṇaṃ na cakkhuviññāṇadhātūti?':'Not the tangible… is what is not eye-consciousness not the eye-consciousness element?',
'Na sotaviññāṇaṃ…pe… na ghānaviññāṇaṃ… na jivhāviññāṇaṃ… na kāyaviññāṇaṃ….':'Not ear-consciousness… not nose-consciousness… not tongue-consciousness… not body-consciousness…',
'Dhātū ghānadhātu…pe… dhātū dhammadhātūti?':'Are the elements the nose element?… are the elements the mind-object element?',
'(Yathā āyatanayamake paṇṇatti evaṃ dhātuyamakepi paṇṇatti.':'(As the section on terms was in the Pairs on Bases, so it is in the Pairs on Elements too.',
'Cakkaṃ bandhitabbaṃ).':'The cycle should be linked up.)',
'Na dhātū na ghānadhātu…pe… na dhātū na dhammadhātūti?':'Is what is not an element not the nose element?… is what is not an element not the mind-object element?',
'Na dhātū na sotadhātu…pe… na dhātū na manoviññāṇadhātūti?':'Is what is not an element not the ear element?… is what is not an element not the mind-consciousness element?',
'(Cakkaṃ bandhitabbaṃ, sabbe āmantā ubhatopi sesepi).':'(The cycle should be linked up. All the answers are "Yes", in both directions and in the rest as well.)',
'Ghānaṃ…pe… jivhā… kāyo… rūpaṃ… saddo… gandho… raso… phoṭṭhabbo….':'The nose… the tongue… the body… material form… sound… scent… taste… the tangible…',
'Sotaṃ ṭhapetvā…pe… ghānaṃ ṭhapetvā…pe… jivha ṭhapetvā…pe….':'Apart from the ear… apart from the nose… apart from the tongue…',
'Rūpaṃ ṭhapetvā…pe… saddaṃ… gandhaṃ… rasaṃ… phoṭṭhabbaṃ… cakkhuviññāṇaṃ…pe… manoviññāṇaṃ ṭhapetvā…pe….':'Apart from material form… sound… scent… taste… the tangible… eye-consciousness… apart from mind-consciousness…',
'(Yathā āyatanayamakassa paṇṇatti evaṃ dhātuyamakassa paṇṇatti vitthāretabbā)':'(The section on terms of the Pairs on Elements should be expanded in the same way as that of the Pairs on Bases.)',
'(Yathā āyatanayamakaṃ vibhattaṃ evaṃ dhātuyamakampi vibhajitabbaṃ, sadisaṃ kātabbaṃ).':'(The Pairs on Elements should be analysed in the same way as the Pairs on Bases were analysed, and made the same.)',
'Yo cakkhudhātuṃ parijānāti so sotadhātuṃ parijānātīti?':'Whoever fully understands the eye element – does that person fully understand the ear element?',
'Āmantā.…Pe… (dhātuyamakaṃ paripuṇṇaṃ peyyālena).':'Yes.… (The Pairs on Elements are complete, with abbreviation.)',
'Dhātuyamakaṃ niṭṭhitaṃ.':'The Pairs on Elements are complete.','Namo tassa bhagavato arahato sammāsambuddhassa':'Homage to the Blessed One, the arahant, the Fully Awakened Buddha'}
HD={'Dhātuyamakaṃ':'The Pairs on Elements','Paṇṇattivāro':'The Section on Terms','(Ka) uddeso':'(a) Outline','(Kha) niddeso':'(b) Explanation','Padasodhanavāro':'The Section on Clarifying the Terms','(Ka) anulomaṃ':'(a) Positive','(Kha) paccanīkaṃ':'(b) Negative','Padasodhanamūlacakkavāro':'The Cycle Based on Clarifying the Terms','Suddhadhātuvāro':'The Section on the Elements Alone','Suddhadhātumūlacakkavāro':'The Cycle Based on the Elements Alone','Pavattivāro 1. uppādavāro':'The Section on Occurrence: 1. Arising','(1) Paccuppannavāro':'(1) Present','(Ka) anulomapuggalo':'(a) Positive: Person','Pariññāvāro':'The Section on Full Understanding'}
def sentence(s):
    if s in SP: return SP[s]
    m=re.fullmatch(rf'(.+?) {C.PRE} {DH} {VB}, no ca {C.PRE} {DH} {VB}\.',s)
    if m:
        g,p,x,v1,_,y,v2=m.groups();return f'{C.lead(g,p)}, {C.stmt(D[x],v1,False)}, but {C.opposite(D[y],v2,False)}.'
    m=re.fullmatch(rf'(.+?) {C.PRE} {DH} ca {VB} {DH} ca {VB}\.',s)
    if m:
        g,p,x,v1,y,v2=m.groups();return f'{C.lead(g,p)}, {C.stmt(D[x],v1,False)}, and {C.stmt(D[y],v2,False)} too.'
    for k,(e,n) in SPEC.items():
        m=re.fullmatch(re.escape(k)+rf' \S+, na {DH}\.',s)
        if m: return f'{e} are {n}, but not {D[m.group(1)]}.'
        m=re.fullmatch(re.escape(k)+rf' na {DH}, \S+\.',s)
        if m: return f'{e} are not {D[m.group(1)]}, but they are {n}.'
    l=s[0].lower()+s[1:]
    m=re.fullmatch(rf'{DH} dhātu ceva \1 ca\.',l)
    if m: return f'{C.cap(D[m.group(1)])} is both an element and {D[m.group(1)]}.'
    m=re.fullmatch(rf'{DH} (\S+?)(?: ceva|ceva) \1 ca\.',l)
    if m: return f'{C.cap(D[m.group(1)])} is both {N[CEVA[m.group(2)]]} and {D[m.group(1)]}.'
    m=re.fullmatch(rf'Avasesā dhātū( ⟦\d+⟧)? na {DH}\.',s)
    if m: return f'The remaining elements{m.group(1) or ""} are not {D[m.group(2)]}.'
    m=re.fullmatch(rf'{DH}ṃ ṭhapetvā (?:avaseso|avasesaṃ) (\S+)( ⟦\d+⟧)?, na \1\.',l)
    if m:
        o,n=OTHER[m.group(2)];return f'Apart from {D[m.group(1)]}, {o}{m.group(3) or ""} is {n}, but not {D[m.group(1)]}.'
    m=re.fullmatch(rf'{DH}ṃ ṭhapetvā (?:avaseso|avasesaṃ) na \1, (\S+)\.',l)
    if m:
        o,n=OTHER[m.group(2)];return f'Apart from {D[m.group(1)]}, {o} is not {D[m.group(1)]}, but it is {n}.'
    m=re.fullmatch(rf'(\S+) {DH}ñca ṭhapetvā (?:avaseso|avasesaṃ)( ⟦\d+⟧)? na ceva (\S+) na ca \2\.',l)
    if m:
        a=N[ACC[m.group(1)]];b=D[m.group(2)];return f'Apart from {a} and {b}, the rest{m.group(3) or ""} are neither {N[m.group(4)]} nor {b}.'
    m=re.fullmatch(r'(\S+) ṭhapetvā avasesā dhātū na (\S+), dhātu\.',l)
    if m:
        a=N[ACC[m.group(1)]];return f'Apart from {a}, the remaining elements are not {a}, but they are elements.'
    m=re.fullmatch(rf'(\S+) ṭhapetvā avasesā dhātū na {DH}\.',l)
    if m: return f'Apart from {N[ACC[m.group(1)]]}, the remaining elements are not {D[m.group(2)]}.'
    m=re.fullmatch(r'(cakkhu ca|\S+) dhātuñca ṭhapetvā avasesā na ceva (\S+) na ca dhāt[uū]\.',l)
    if m:
        a=N[ACC[m.group(1)]];return f'Apart from {a} and the elements, the rest are neither {a} nor elements.'
    raise KeyError(s)
QP=re.compile(rf'\((Ka|Kha)\) (yassa vā pana|yassa) {DH} {VB} tassa {DH} {VB}\?')
def nm(w,second):
    w=w.lower()
    if w in('dhātūti','dhātu') and second: return 'an element'
    if w=='dhātū': return 'the elements'
    for t in (w,w[:-3]+'u' if w.endswith('ūti') else None,w[:-3]+'ṃ' if w.endswith('nti') else None,w[:-2] if w.endswith('ti') else None):
        if t in N: return N[t]
    raise ValueError('name '+w)
def q(p):
    m=re.fullmatch(r'(?:\((Ka|Kha)\) )?(.+?)\?(…Pe…\.?)?',p)
    lab,qq,pe=m.groups();vm=re.search(r' ⟦\d+⟧',qq);vv=vm.group(0) if vm else '';qq=re.sub(r' ⟦\d+⟧','',qq).lower();neg=qq.startswith('na ')
    ws=qq[3:].split(' na ') if neg else qq.split()
    if len(ws)!=2: raise ValueError('q '+p)
    a=nm(ws[0],False);b=nm(ws[1],True)
    t=f'Is what is not {"an element" if a=="the elements" else a} not {b}?' if neg else f'{"Are" if a=="the elements" else "Is"} {a}{vv} {b}?'
    return C.LAB.get(lab,'')+t+('…' if pe else '')
def piece(p):
    if p in SP: return SP[p]
    m=QP.fullmatch(p)
    if m:
        lab,c,x,v1,y,v2=m.groups();v2=C.verbq(v2);ld='And for whomever' if 'pana' in c else 'For whomever'
        return f'{C.LAB[lab]}{ld} {C.stmt(D[x],v1,False)}, {C.ask(D[y],v2," for them")}?'
    if '?' in p: return q(p)
    return sentence(p)
def tr(b):
    b=re.sub(r'…Pe…\.$','…Pe…',b) if b.startswith('(Kha)') else b
    if b in SP: return SP[b]
    return ' '.join(piece(x) for x in re.split(r'(?<=[.?)]) (?=[A-Z(Āā…])',b))
if __name__=='__main__':
    f='4-dhatuyamaka.md';o,bad=run(f,tr,HD);print(f,'unmatched',len(bad))
    for x in bad[:20]: print(x)
    if not bad: write(f,o);check(f)
