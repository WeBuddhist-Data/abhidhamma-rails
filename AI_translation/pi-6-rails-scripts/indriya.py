"""Rails translation of chapter 10 (Pairs on Faculties)."""
from general import *
FAC={'cakkhu':'the eye faculty','sot':'the ear faculty','ghān':'the nose faculty','jivh':'the tongue faculty','kāy':'the body faculty','man':'the mind faculty','itth':'the feminine faculty','puris':'the masculine faculty','jīvit':'the life faculty','sukh':'the pleasure faculty','dukkh':'the pain faculty','somanass':'the joy faculty','domanass':'the faculty of displeasure','upekkh':'the equanimity faculty','saddh':'the faith faculty','vīriy':'the energy faculty','sat':'the mindfulness faculty','samādh':'the concentration faculty','paññ':'the wisdom faculty','anaññāt':'the faculty "I shall know what is yet unknown"','aññ':'the faculty of knowledge','aññātāv':'the faculty of final knowledge'}
for k,v in FAC.items(): C.SUBJ[f'§{k}§']=v
C.N.update({f'§{k}§':v for k,v in FAC.items()})
C.N.update({'cakkhu':'the eye','cakkhuṃ':'the eye','sotaṃ':'the ear','ghānaṃ':'the nose','jivhā':'the tongue','kāyo':'the body','mano':'the mind','itthī':'a woman','puriso':'a man','jīvitaṃ':'life','sukhaṃ':'pleasure','dukkhaṃ':'pain','somanassaṃ':'joy','domanassaṃ':'displeasure','upekkhā':'equanimity','saddhā':'faith','vīriyaṃ':'energy','sati':'mindfulness','samādhi':'concentration','paññā':'wisdom','anaññātaññassāmīti':'"I shall know what is yet unknown"','anaññātaññāssāmīti':'"I shall know what is yet unknown"','aññaṃ':'final knowledge','aññātāvī':'one who has final knowledge','aññātāvi':'one who has final knowledge','indriyā':'the faculties','indriyaṃ':'a faculty','satīti':'mindfulness','samādhīti':'concentration'})
C.SING['indriyā']='a faculty'
FORMS=sorted([('cakkhund','cakkhu'),('sotind','sot'),('ghānind','ghān'),('jivhind','jivh'),('kāyind','kāy'),('manind','man'),('itthind','itth'),('purisind','puris'),('jīvitind','jīvit'),('sukhind','sukh'),('dukkhind','dukkh'),('somanassind','somanass'),('domanassind','domanass'),('upekkhind','upekkh'),('saddhind','saddh'),('vīriyind','vīriy'),('viriyind','vīriy'),('satind','sat'),('samādhind','samādh'),('paññind','paññ'),('anaññātaññassāmītind','anaññāt'),('aññātāvind','aññātāv'),('aññind','aññ'),('ghānand','ghān')],key=lambda x:-len(x[0]))
def sub(b):
    def rp(m):
        w=m.group(0);l=w[0].lower()+w[1:]
        for f,k in FORMS:
            if l.startswith(f+'riya'):
                x=l[len(f)+4:]
                if x in('ṃ','nti',''): return f'§{k}§'
                if x=='ñca': return f'§{k}§ ca'
                if x=='mūlakaṃ': return f'§{k}§mūlakaṃ'
        return w
    return re.sub(r'\b\w+ndriya\w*',rp,b)
BARES={'cakkhu':'Cakkhu','sotaṃ':'Sot','ghānaṃ':'Ghān','jivhā':'Jivh','kāyo':'Kāy','mano':'Man','itthī':'Itth','puriso':'Puris','jīvitaṃ':'Jīvit','sukhaṃ':'Sukh','dukkhaṃ':'Dukkh','somanassaṃ':'Somanass','domanassaṃ':'Domanass','upekkhā':'Upekkh','saddhā':'Saddh','vīriyaṃ':'Vīriy','sati':'Sat','samādhi':'Samādh','paññā':'Paññ','anaññātaññassāmīti':'Anaññātaññassāmīt','aññaṃ':'Aññ','aññātāvī':'Aññātāv'}
for nom,stem in BARES.items():
    for suf in ('aṃ','iṃ','uṃ','añca','iñca','uñca','īṃ','ī'): C.ACC[stem+suf]=nom
C.ACC.update({'Cakkhuṃ':'cakkhu','Cakkhuñca':'cakkhu','Manaṃ':'mano','Manañca':'mano','Kāyañca':'kāyo','Anaññātaññassāmīti':'anaññātaññassāmīti','Anaññātaññassāmītiñca':'anaññātaññassāmīti','Aññañca':'aññaṃ','Aññaṃ':'aññaṃ','Aññātāviñca':'aññātāvī','Aññātāviṃ':'aññātāvī','Satiṃ':'sati','Satiñca':'sati','Samādhiṃ':'samādhi','Samādhiñca':'samādhi','Sotaṃ':'sotaṃ','Sotañca':'sotaṃ'})
C.OTHER.update({'kāyo':('any other body','a body'),'mano':('any other mind','a mind'),'upekkhā':('any other equanimity','equanimity')})
C.CEVA.update({'cakkhu':'cakkhu','sotañ':'sotaṃ','kāyo':'kāyo','upekkhā':'upekkhā','mano':'mano','indriyañ':'indriyaṃ','paññā':'paññā','sukhañ':'sukhaṃ','dukkhañ':'dukkhaṃ','saddhā':'saddhā','sati':'sati','samādhi':'samādhi'})
C.SPEC.update({'Dibbacakkhu paññācakkhu':('The divine eye and the eye of wisdom','eyes'),'Dibbasotaṃ taṇhāsotaṃ':('The divine ear and the stream of craving','"ear" (sota)')})
C.CAT.update({'pl':'indriyā','en':'faculties','ca':'indriye ca'})
QUAL={'somanassa':'joy','upekkhā':'equanimity','saddhā':'faith','ñāṇa':'knowledge','domanassa':'displeasure','dukkha':'pain','sukha':'pleasure','paññā':'wisdom'}
QK='|'.join(QUAL)
CMP=re.compile(rf'(pavatte )?((?:(?:{QK})(?:sampayutta|vippayutta))+)cittassa (uppāda|bhaṅga)kkhaṇe\s*',re.I)
def cmp_(g):
    m=CMP.match(g)
    if not m: return None
    bits=re.findall(rf'({QK})(sampayutta|vippayutta)',m.group(2).lower())
    ps=[('associated with ' if b=='sampayutta' else 'not associated with ')+QUAL[a] for a,b in bits]
    w='arising' if m.group(3).lower()=='uppāda' else 'dissolution'
    return ('@'+('during life, ' if m.group(1) else '')+f'at the moment of {w} of consciousness '+' and '.join(ps),g[m.end():])
GEN=re.compile(r'(ye ca |ye |yā ca |yā )?(itthiyo |purisā |sacakkhukā |saghānakā |sacittakā |sarūpakā )?(eteneva bhāvena katici bhave dassetvā )?(upekkhāya |somanassena |domanassena )(rūpāvacaraṃ |arūpaṃ |kāmāvacaraṃ )?upapajjitvā parinibbāyissanti\s*',re.I)
def gen(g):
    m=GEN.match(g)
    if not m: return None
    w={'itthiyo ':'women','purisā ':'men','sacakkhukā ':'those with eyes','saghānakā ':'those with a nose','sacittakā ':'those with mind','sarūpakā ':'those with material form'}.get((m.group(2) or '').lower(),'those')
    sh=', in this same state, after showing several existences,' if m.group(3) else ''
    q={'upekkhāya ':'with equanimity','somanassena ':'with joy','domanassena ':'with displeasure'}[m.group(4).lower()]
    rl={'rūpāvacaraṃ ':' in the fine-material sphere','arūpaṃ ':' in the formless sphere','kāmāvacaraṃ ':' in the sense sphere'}.get((m.group(5) or '').lower(),'')
    return (f'{w}{sh} who will be reborn {q}{rl} and attain final nibbāna',g[m.end():])
C.EXTRA[:0]=[cmp_,gen]
for k,x in [('yā ca itthiyo eteneva bhāvena katici bhave dassetvā parinibbāyissanti','women who, in this same state, will show several existences and attain final nibbāna'),('yā itthiyo eteneva bhāvena katici bhave dassetvā parinibbāyissanti','women who, in this same state, will show several existences and attain final nibbāna'),('ye ca purisā eteneva bhāvena katici bhave dassetvā parinibbāyissanti','men who, in this same state, will show several existences and attain final nibbāna'),('ye purisā eteneva bhāvena katici bhave dassetvā parinibbāyissanti','men who, in this same state, will show several existences and attain final nibbāna'),('yā ca itthiyo rūpāvacaraṃ arūpāvacaraṃ upapajjitvā parinibbāyissanti','women who will be reborn in the fine-material or formless sphere and attain final nibbāna'),('yā ca itthiyo arūpaṃ upapajjitvā parinibbāyissanti','women who will be reborn in the formless sphere and attain final nibbāna'),('yā ca itthiyo rūpāvacaraṃ upapajjitvā parinibbāyissanti','women who will be reborn in the fine-material sphere and attain final nibbāna'),('ye ca purisā rūpāvacaraṃ arūpāvacaraṃ upapajjitvā parinibbāyissanti','men who will be reborn in the fine-material or formless sphere and attain final nibbāna'),('ye ca purisā arūpaṃ upapajjitvā parinibbāyissanti','men who will be reborn in the formless sphere and attain final nibbāna'),('ye ca purisā rūpāvacaraṃ upapajjitvā parinibbāyissanti','men who will be reborn in the fine-material sphere and attain final nibbāna'),('kāmāvacare','@in the sense sphere'),('rūpāvacare','@in the fine-material sphere'),('arūpāvacare','@in the formless sphere'),('rūpāvacare arūpāvacare','@in the fine-material and formless spheres')]:
    C.ATOMS.append((k,x))
for q,qe in (('upekkhāsampayutta','associated with equanimity'),('somanassasampayutta','associated with joy'),('domanassasampayutta','associated with displeasure'),('saddhāsampayutta','associated with faith'),('ñāṇasampayutta','associated with knowledge'),('saddhāvippayutta','not associated with faith'),('ñāṇavippayutta','not associated with knowledge'),('somanassavippayutta','not associated with joy'),('upekkhāvippayutta','not associated with equanimity')):
    C.ATOMS.append((f'yassa cittassa anantarā {q}pacchimacittaṃ uppajjissati',f'those whose final consciousness {qe} will arise immediately after a given consciousness'))
    C.ATOMS.append((f'{q}pacchimacittasamaṅgīnaṃ',f'those possessing the final consciousness {qe}'))
    for w,we in (('uppādakkhaṇe','arising'),('bhaṅgakkhaṇe','dissolution')): C.ATOMS.append((f'{q}pacchimacittassa {w}',f'@at the moment of {we} of the final consciousness {qe}'))
C.atoms_sort()
C.PERS.update({'Tayo maggasamaṅgino ca arahantañca ṭhapetvā avasesā puggalā':('Apart from those possessing the three paths and an arahant, the remaining persons',1),'Ye puthujjanā maggaṃ na paṭilabhissanti te':('Ordinary persons who will not attain the path',1),'Tayo maggasamaṅgino':('Those possessing the three paths',1),'Cattāro maggasamaṅgino':('Those possessing the four paths',1),'Ye puthujjanā maggaṃ paṭilabhissanti te':('Ordinary persons who will attain the path',1),'Tayo maggasamaṅgino ṭhapetvā avasesā puggalā':('Apart from those possessing the three paths, the remaining persons',1),'Cattāro maggasamaṅgino ṭhapetvā avasesā puggalā':('Apart from those possessing the four paths, the remaining persons',1),'Anāgāmimaggasamaṅgiñca arahantañca ṭhapetvā avasesā puggalā':('Apart from one who possesses the path of non-returning and an arahant, the remaining persons',1),'Aṭṭhamako':('One at the eighth stage',0),'Aṭṭhamakañca arahantañca ṭhapetvā avasesā puggalā':('Apart from one at the eighth stage and an arahant, the remaining persons',1),'Yo aggaphalaṃ sacchākāsi so':('One who has realized the highest fruit',0),'Anāgāmimaggasamaṅgī':('One who possesses the path of non-returning',0),'Yo aggaphalaṃ sacchikaroti so':('One who realizes the highest fruit',0),'Dve puggalā':('Two kinds of person',1),'Cha puggalā':('Six kinds of person',1),'Cattāro puggalā':('Four kinds of person',1),'Tayo puggalā':('Three kinds of person',1),'Pañca puggalā':('Five kinds of person',1),'Satta puggalā':('Seven kinds of person',1),'Aṭṭha puggalā':('Eight kinds of person',1),'Dve maggasamaṅgino ṭhapetvā avasesā puggalā':('Apart from those possessing the two paths, the remaining persons',1),'Puthujjano':('An ordinary person',0),'Anāgāmī':('A non-returner',0),'Sekkhā':('Trainees',1),'Aggamaggasamaṅgī ca arahā ca':('One who possesses the highest path and an arahant',1)})
_pari=C.pari
def pari(s):
    v=re.findall(r' ⟦\d+⟧',s)
    if v: return _pari(re.sub(r' ⟦\d+⟧','',s))[:-1]+''.join(v)+'.'
    return _pari(s)
C.pari=pari
RAW={'Indriyayamakaṃ niṭṭhitaṃ.':'The Pairs on Faculties are complete.','Yamakapakaraṇaṃ niṭṭhitaṃ.':'The Book of Pairs is complete.'}
FULL={'Bāvīsatindriyāni – cakkhundriyaṃ, sotindriyaṃ, ghānindriyaṃ, jivhindriyaṃ, kāyindriyaṃ, manindriyaṃ, itthindriyaṃ, purisindriyaṃ, jīvitindriyaṃ, sukhindriyaṃ, dukkhindriyaṃ, somanassindriyaṃ, domanassindriyaṃ, upekkhindriyaṃ, saddhindriyaṃ, vīriyindriyaṃ ⟦0⟧, satindriyaṃ, samādhindriyaṃ, paññindriyaṃ, anaññātaññassāmītindriyaṃ, aññindriyaṃ, aññātāvindriyaṃ.':'There are twenty-two faculties – the eye faculty, the ear faculty, the nose faculty, the tongue faculty, the body faculty, the mind faculty, the feminine faculty, the masculine faculty, the life faculty, the pleasure faculty, the pain faculty, the joy faculty, the faculty of displeasure, the equanimity faculty, the faith faculty, the energy faculty ⟦0⟧, the mindfulness faculty, the concentration faculty, the wisdom faculty, the faculty "I shall know what is yet unknown", the faculty of knowledge, the faculty of final knowledge.'}
def hook(s):
    ls=s if s.startswith('§') else s[0].lower()+s[1:]
    m=re.fullmatch(r'(\S+) na (\S+), \1\.',ls)
    if m and m.group(1) in C.N and m.group(2) in C.N:
        a=C.N[m.group(1)];return f'{C.cap(a)} is not {C.N[m.group(2)]}, but it is {a}.'
    m=re.fullmatch(r'(?:Yaṃ|Yo|Yā) (\S+) indriyaṃ (?:taṃ|so|sā) (\S+?)(?: ceva|ceva) indriyañca\.',s)
    if m: a=C.N[m.group(1)];return f'That part of {a} which is a faculty is both {a} and a faculty.'
    m=re.fullmatch(r'(?:Avasesaṃ|Avaseso|Avasesā) (\S+) na indriy(?:aṃ|ā)\.',s)
    if m: return f'The rest of {C.N[m.group(1)]} is not a faculty.'
    return None
C.HOOK.insert(0,hook)
SLIP=[('uppajjantīnaṃ','upapajjantīnaṃ'),('uppajjantānaṃ','upapajjantānaṃ'),('na upapajjissati','nuppajjissati'),('Pacchimacittasamaṅgīna ','Pacchimacittasamaṅgīnaṃ '),('Ghānandriya','Ghānindriya'),('asaññasattā cavantāna ','asaññasattā cavantānaṃ '),('uppajjissati, tassa','uppajjissati tassa'),('bhavissanti','bhāvessanti'),('parinibbāntānaṃ','parinibbantānaṃ'),('na uppajjissati pacchimacittassa','na uppajjissati. Pacchimacittassa'),('nuppajjissati pacchimacittassa','nuppajjissati. Pacchimacittassa'),('indriyaṃ ca ','indriyañca '),('uppajjissati. Somanassindriyañca','uppajjissati somanassindriyañca'),('bhāvessati. So ','bhāvessati so '),('nappajjahittha','nappajahittha'),(' anāgāmimaggasamaṅgi aññindriyañca bhāvessanti, domanassindriyañca pajahanti','. Anāgāmimaggasamaṅgī aññindriyañca bhāvessati domanassindriyañca pajahati'),(', pañca puggalā','. Pañca puggalā')]
_tr,HDD=build(sub,RAW,FULL,SLIP,None,{'Indriyayamakaṃ':'The Pairs on Faculties','Suddhindriyavāro':'The Section on the Faculties Alone','Suddhindriyamūlacakkavāro':'The Cycle Based on the Faculties Alone'})
def tr(b):
    b=re.sub(r'([^,]) no ca ',r'\1, no ca ',b)
    b=re.sub(r'^(\(K\w+\) y.*(?:āti|īti))\.( Āmantā\.)?$',lambda m:m.group(1)+'?'+(m.group(2) or ''),b)
    if b not in FULL and not re.match(r'.*[Yy]assa',b):
        ps=re.split(r'(?<=\?) (?=[A-ZĀ])',b)
        if len(ps)>1 and all('?' in x for x in ps[:-1]): return ' '.join(tr(x) for x in ps)
    return _tr(b)
if __name__=='__main__': go([f'10-{i:02d}-indriyayamaka.md' for i in range(1,14)],tr,HDD,show=22)
