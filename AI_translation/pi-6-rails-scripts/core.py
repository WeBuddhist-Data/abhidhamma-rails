"""Shared grammar for the pi-6 rails translation. Terms follow english/pi-6-pali-english-termbase-plain.md."""
import re
LAB={'Ka':'(a) ','Kha':'(b) '}
T=r'(§\w+§)'
VB=r'(na nirujjh\w+|nirujjh\w+|nuppajj\w+|na uppajj\w+|uppajj\w+)'
PRE=r'(tāsaṃ tattha|tesaṃ tattha|tāsaṃ|tesaṃ|tattha)'
PLURAL=[False]
SUBJ={}   # token -> English; filled by each chapter
def e(tok): return SUBJ[tok]
def cap(s): return s[0].upper()+s[1:]
def verb(w):
    neg=False
    if w.startswith('na '): neg=True;w=w[3:]
    if w.startswith('nuppajj'): neg=True;w='uppajj'+w[7:]
    for r,(b,s,p) in {'uppajj':('arise','arises','arisen'),'nirujjh':('cease','ceases','ceased')}.items():
        if w.startswith(r):
            x=w[len(r):]
            if x=='ati': return ('does',b,s,neg)
            if x=='anti': return ('do',b,b,neg)
            if x in('ittha','attha'):
                h='have' if PLURAL[0] else 'has';return (h,p,h+' '+p,neg)
            if x=='issati': return ('will',b,'will '+b,neg)
            if x=='issanti': return ('will',b,'will '+b,neg)
    raise ValueError('verb '+w)
def verbq(w):
    w=re.sub(r'īti$','i',re.sub(r'āti$','a',w));return w
def stmt(subj,v,there):
    aux,b,s,neg=verb(v);t=' there' if there else ''
    return f'{subj} {aux} not {b}{t}' if neg else f'{subj} {s}{t}'
def opposite(subj,v,there):
    aux,b,s,neg=verb(v);t=' there' if there else ''
    return f'{subj} {aux} {b}{t}' if neg else f'{subj} {aux} not {b}{t}'
def ask(subj,v,suf):
    aux,b,s,neg=verb(v);return f'{aux} {subj} {"not " if neg else ""}{b}{suf}'
ATOMS=[('sabbesaṃ cavantānaṃ','all those passing away'),('sabbesaṃ upapajjantānaṃ','all those being reborn'),
('asaññasattaṃ upapajjantānaṃ','those being reborn as non-percipient beings'),('suddhāvāsaṃ upapajjantānaṃ','those being reborn in the Pure Abodes'),('arūpaṃ upapajjantānaṃ','those being reborn in the formless sphere'),
('catuvokāraṃ pañcavokāraṃ upapajjantānaṃ','those being reborn in four- or five-aggregate existence'),('pañcavokāraṃ upapajjantānaṃ','those being reborn in five-aggregate existence'),
('pacchimabhavikānaṃ pañcavokāraṃ upapajjantānaṃ','those in their final existence being reborn in five-aggregate existence'),('pacchimabhavikānaṃ arūpaṃ upapajjantānaṃ','those in their final existence being reborn in the formless sphere'),('pacchimabhavikānaṃ upapajjantānaṃ','those in their final existence being reborn'),
('pañcavokāre pacchimabhavikānaṃ','those in their final existence in five-aggregate existence'),('arūpe pacchimabhavikānaṃ','those in their final existence in the formless sphere'),('pacchimabhavikānaṃ','those in their final existence'),
('catuvokārā pañcavokārā cavantānaṃ','those passing away from four- or five-aggregate existence'),('pañcavokārā cavantānaṃ','those passing away from five-aggregate existence'),('asaññasattā cavantānaṃ','those passing away from among non-percipient beings'),('arūpā cavantānaṃ','those passing away from the formless sphere'),
('suddhāvāse parinibbantānaṃ','those attaining final nibbāna in the Pure Abodes'),('pañcavokāre parinibbantānaṃ','those attaining final nibbāna in five-aggregate existence'),('arūpe parinibbantānaṃ','those attaining final nibbāna in the formless sphere'),('parinibbantānaṃ','those attaining final nibbāna'),
('catuvokārānaṃ pañcavokārānaṃ','those in four- or five-aggregate existence'),('pañcavokārānaṃ','those in five-aggregate existence'),('suddhāvāsānaṃ','those in the Pure Abodes'),('asaññasattānaṃ','non-percipient beings'),('arūpānaṃ','those in the formless sphere'),
('ye ca arūpaṃ upapajjitvā parinibbāyissanti tesaṃ cavantānaṃ','those passing away who will be reborn in the formless sphere and attain final nibbāna'),('ye ca arūpaṃ upapajjitvā parinibbāyissanti','those who will be reborn in the formless sphere and attain final nibbāna'),('ye arūpaṃ upapajjitvā parinibbāyissanti','those who will be reborn in the formless sphere and attain final nibbāna'),('ye rūpāvacaraṃ upapajjitvā parinibbāyissanti','those who will be reborn in the fine-material sphere and attain final nibbāna')]
def atoms_sort(): ATOMS.sort(key=lambda a:-len(a[0]))
ADJ1={'cakkhu':'eyes','sota':'ears','ghāna':'a nose','rūpa':'material form','citta':'mind'}
PMAP={'na itthīnaṃ':'not as women','itthīnaṃ':'as women','na purisānaṃ':'not as men','purisānaṃ':'as men','vinā somanassena':'without joy','somanassena':'with joy','vinā upekkhāya':'without equanimity','upekkhāya':'with equanimity','vinā domanassena':'without displeasure','domanassena':'with displeasure','sahetukānaṃ':'with roots','ahetukānaṃ':'without roots','ñāṇasampayuttānaṃ':'with knowledge','ñāṇavippayuttānaṃ':'without knowledge'}
PA='(?:'+'|'.join(sorted(PMAP,key=len,reverse=True))+r'|(?:sa|a)(?:cakkhu|sota|ghāna|rūpa|citta)kānaṃ)'
PHR=re.compile(rf'((?:{PA}\s+)*{PA}\s+)(?:(kāmāvacaraṃ\s+)?(?:upapajjantānaṃ|upapajjantīnaṃ)|(kāmāvacarā\s+)?(?:cavantānaṃ|cavantīnaṃ))\s*',re.I)
def adj(x):
    o=[]
    for m in re.finditer(PA,x,flags=re.I):
        w=m.group(0).lower()
        if w in PMAP: o.append(PMAP[w]);continue
        mm=re.fullmatch(r'(sa|a)(\w+)kānaṃ',w);o.append(('with ' if mm.group(1)=='sa' else 'without ')+ADJ1[mm.group(2)])
    if len(o)==2 and all(w.startswith(('with ','without ')) and not w.endswith(('roots','joy','equanimity','displeasure','knowledge')) for w in o):
        a,b=o
        if a.startswith('with ') and b.startswith('with '): return f'with {a[5:]} and {b[5:]}'
        if a.startswith('without') and b.startswith('without'): return f'without {a[8:]} or {b[8:]}'
        return f'{a} but {b}'
    return ', '.join(o)
def phr(g):
    m=PHR.match(g)
    if not m: return None
    pre='those being reborn' if 'upapajjant' in m.group(0) else 'those passing away'
    rn=' in the sense sphere' if m.group(2) else (' from the sense sphere' if m.group(3) else '')
    return (pre+rn+' '+adj(m.group(1)),g[m.end():])
_C={'cittassa':'consciousness','taṇhāya':'craving','maggassa':'the path','aggamaggassa':'the highest path','phalassa':'the fruit','maggassa ca phalassa ca':'the path and its fruit','aggamaggassa ca phalassa ca':'the highest path and its fruit','aggaphalassa':'the highest fruit','taṇhāvippayuttacittassa':'consciousness not associated with craving','maggavippayuttacittassa':'consciousness not associated with the path','maggavippayuttataṇhāvippayuttacittassa':'consciousness not associated with the path or with craving','taṇhāvippayuttamaggavippayuttacittassa':'consciousness not associated with craving or with the path','upapatticittassa':'the rebirth consciousness','tassa cittassa':'that consciousness','pacchimacittassa':'the final consciousness'}
def add_time(d):
    for k,v in d.items():
        for w,we in (('uppādakkhaṇe','arising'),('bhaṅgakkhaṇe','dissolution')):
            ATOMS.append((f'{k} {w}',f'@at the moment of {we} of {v}'));ATOMS.append((f'pavatte {k} {w}',f'@during life, at the moment of {we} of {v}'))
add_time(_C)
ATOMS.extend([('taṇhāvippayuttacitte vattamāne','@while consciousness not associated with craving is occurring'),('maggavippayuttacitte vattamāne','@while consciousness not associated with the path is occurring'),('dutiye citte vattamāne','@while the second consciousness is occurring'),('dutiye akusale citte vattamāne','@while the second unwholesome consciousness is occurring'),('arūpe','@in the formless sphere'),('pañcavokāre','@in five-aggregate existence'),('sabbesaṃ','@for everyone')])
_R={'kāmāvacare':'the sense sphere','rūpāvacare':'the fine-material sphere','arūpāvacare':'the formless sphere','rūpāvacare arūpāvacare':'the fine-material and formless spheres'}
for k,x in _R.items():
    ATOMS.append((k+' parinibbantānaṃ','those attaining final nibbāna in '+x));ATOMS.append((k+' pacchimabhavikānaṃ','those in their final existence in '+x))
for k,x in {'rūpāvacaraṃ':'the fine-material sphere','arūpaṃ':'the formless sphere','rūpāvacaraṃ arūpāvacaraṃ':'the fine-material or formless sphere'}.items():
    tl=f'who will be reborn in {x} and attain final nibbāna'
    for pre in ('ye ca ','ye '):
        ATOMS.append((pre+k+' upapajjitvā parinibbāyissanti tesaṃ cavantānaṃ','those passing away '+tl));ATOMS.append((pre+k+' upapajjitvā parinibbāyissanti tesaṃ upapajjantānaṃ','those being reborn now '+tl));ATOMS.append((pre+k+' upapajjitvā parinibbāyissanti','those '+tl))
for k,x in {'kāmāvacaraṃ':'the sense sphere','rūpāvacaraṃ':'the fine-material sphere','rūpāvacaraṃ arūpāvacaraṃ':'the fine-material or formless sphere'}.items():
    ATOMS.append(('pacchimabhavikānaṃ '+k+' upapajjantānaṃ','those in their final existence being reborn in '+x))
ATOMS.extend([('rūpāvacarā cavantānaṃ','those passing away from the fine-material sphere'),('kāmāvacarā cavantānaṃ','those passing away from the sense sphere'),('rūpāvacaraṃ upapajjantānaṃ','those being reborn in the fine-material sphere'),('kāmāvacaraṃ upapajjantānaṃ','those being reborn in the sense sphere'),('rūpāvacaraṃ arūpāvacaraṃ upapajjantānaṃ','those being reborn in the fine-material or formless sphere'),('rūpāvacarā arūpāvacarā cavantānaṃ','those passing away from the fine-material or formless sphere'),('rūpāvacarānaṃ','those in the fine-material sphere'),('arūpāvacarānaṃ','those in the formless sphere'),('kāmāvacarānaṃ','those in the sense sphere'),('tesaṃ upapajjantānaṃ','those being reborn'),('tesaṃ cavantānaṃ','those passing away'),('upapajjantānaṃ','those being reborn'),('cavantānaṃ','those passing away'),('upapajjantīnaṃ','those being reborn'),('cavantīnaṃ','those passing away')])
for k,x in {'pacchimacittasamaṅgīnaṃ':'those possessing the final consciousness','abhisametāvīnaṃ':'those who have realized the truths','anabhisametāvīnaṃ':'those who have not realized the truths','arahantānaṃ':'arahants','aggamaggasamaṅgīnaṃ':'those possessing the highest path','āpāyikānaṃ':'those in the states of misery','nirodhasamāpannānaṃ':'those in the attainment of cessation','yassa cittassa anantarā aggamaggaṃ paṭilabhissanti':'those who will attain the highest path immediately after a given consciousness','ye caññe maggaṃ paṭilabhissanti':'others who will attain the path','ye maggaṃ paṭilabhissanti':'those who will attain the path','ye ca puthujjanā maggaṃ na paṭilabhissanti':'ordinary persons who will not attain the path','ye puthujjanā maggaṃ na paṭilabhissanti':'ordinary persons who will not attain the path'}.items():
    ATOMS.append((k,x))
for k,x in {'abhisametāvīnaṃ':'those who have realized the truths','anabhisametāvīnaṃ':'those who have not realized the truths'}.items():
    ATOMS.append((k+' upapajjantānaṃ',x+' being reborn'));ATOMS.append((k+' cavantānaṃ',x+' passing away'))
atoms_sort()

EXTRA=[phr]  # chapter-level matchers: fn(g)->(text,rest) or None
def group(g):
    g=g.strip().replace(',','');others=False
    var=''.join(re.findall(r' ?⟦\d+⟧',g));g=re.sub(r' ?⟦\d+⟧','',g)
    if g.lower().startswith(('itaresaṃ','itarāsaṃ')): others=True;g=g[8:].strip()
    parts=[]
    while g:
        if g.startswith(('tesaṃ ','tāsaṃ ')) and not g.startswith(('tesaṃ upapajjantānaṃ','tesaṃ cavantānaṃ')): g=g.split(' ',1)[1].strip();continue
        for fn in EXTRA:
            r=fn(g)
            if r: parts.append(r[0]);g=r[1].strip();break
        else:
            for a,x in ATOMS:
                if g.lower().startswith(a.lower()):
                    parts.append(x);g=g[len(a):].strip();break
            else: raise ValueError('group: '+g)
    if any(p.startswith('@') for p in parts):
        o=[]
        if others and parts[0].startswith('@'): o.append('for the others')
        for i,p in enumerate(parts):
            if p.startswith('@'): o.append(p[1:])
            else:
                if others and i==0: p=p.replace('those','the others',1) if 'those' in p else 'the others, '+p
                o.append('for '+p)
        r=', '.join(o);return cap(r)+var
    if others: s='the others' if not parts else ' and '.join(parts).replace('those','the others',1)
    else: s=parts[0] if len(parts)==1 else ', '.join(parts[:-1])+' and '+parts[-1]
    return 'For '+s+var
PLACE={'Apāye':'In the states of misery','Asaññasatte':'Among non-percipient beings','Pañcavokāre':'In five-aggregate existence','Arūpe':'In the formless sphere','Catuvokāre':'In four-aggregate existence','Suddhāvāse':'In the Pure Abodes','Rūpāvacare':'In the fine-material sphere','Kāmāvacare':'In the sense sphere','Arūpāvacare':'In the formless sphere'}
def place(g):
    ps=[PLACE[w[0].upper()+w[1:]] for w in g.split()]
    return ps[0]+''.join(' and '+p[0].lower()+p[1:] for p in ps[1:])
def lead(g,p): return place(g) if p=='tattha' else group(g)
CL={'yassa':'For whomever','yassa vā pana':'And for whomever','yattha':'Wherever','yattha vā pana':'And wherever','yassa yattha':'For whomever and wherever','yassa vā pana yattha':'And for whomever and wherever'}
CLR=r'([Yy]assa vā pana yattha|[Yy]assa yattha|[Yy]assa vā pana|[Yy]attha vā pana|[Yy]assa|[Yy]attha)'
FT={'tassa':' for them','tattha':' there','tassa tattha':' for them there'}
QP=re.compile(rf'(?:\((Ka|Kha)\) )?{CLR} {T} {VB} (tassa tattha|tassa|tattha) {T} {VB}\?(.*)')
PV=r'((?:na |nap)?(?:parijān|pajah|ppajah|bhāv|sacch)\w*)'
def VBASE(w):
    if w.startswith('parijān'): return ('fully understand','fully understood')
    if w.startswith('bhāv'): return ('cultivate','cultivated')
    if w.startswith('sacch'): return ('realize','realized')
    return ('abandon','abandoned')
def fq(w):
    n=False
    if w.startswith('na '): n=True;w=w[3:]
    if w.startswith('napp'): n=True;w=w[3:]
    w=verbq(w)
    b,p=VBASE(w)
    if 'issa' in w or 'essa' in w: return('will',b,'will '+b,n)
    if w.endswith('ittha'): return('has',p,'has '+p,n)
    return('does',b,b.replace('understand','understands') if 'understand' in b else b+'s',n)
QF=re.compile(rf'\((Ka|Kha)\) yo (vā pana )?{T} {PV} so {T} {PV}\?(.*)')
PERS={'Arahā':('An arahant',0),'Aggamaggasamaṅgī':('One who possesses the highest path',0),'Ye maggaṃ paṭilabhissanti te':('Those who will attain the path',1),'Aggamaggasamaṅgiñca arahantañca ṭhapetvā avasesā puggalā':('Apart from one who possesses the highest path and an arahant, the remaining persons',1),'Arahā ye ca puthujjanā maggaṃ na paṭilabhissanti te':('An arahant and ordinary persons who will not attain the path',1),'Aggamaggasamaṅgī ye ca puthujjanā maggaṃ na paṭilabhissanti te':('One who possesses the highest path and ordinary persons who will not attain the path',1)}
def pv(w,pl):
    n=False
    if w.startswith('na '): n=True;w=w[3:]
    if w.startswith('napp'): n=True;w=w[3:]
    b,p=VBASE(w)
    if 'issa' in w or 'essa' in w: return('will',b,n)
    if w.endswith('ittha') or w.endswith('si'): return('have' if pl else 'has',p,n)
    return('do' if pl else 'does',b,n)
def pvs(t,pl,flip=False):
    a,b,n=t
    if flip: return f'{a} {b}' if n else f'{a} not {b}'
    if n: return f'{a} not {b}'
    if a in('do','does'):
        if pl: return b
        return b.replace('understand','understands') if 'understand' in b else b+'s'
    return f'{a} {b}'
def pari(s):
    R='('+'|'.join(sorted(map(re.escape,PERS),key=len,reverse=True))+')'
    m=re.fullmatch(rf'{R} {T} {PV}, no ca (?:te |so )?{T} {PV}\.',s)
    if m:
        su,x,v1,y,v2=m.groups();en,pl=PERS[su]
        return f'{en} {pvs(pv(v1,pl),pl)} {e(x)}, but {pvs(pv(v2,pl),pl,True)} {e(y)}.'
    m=re.fullmatch(rf'{R} {T} ca {PV} {T} ca {PV}\.',s)
    if m:
        su,x,v1,y,v2=m.groups();en,pl=PERS[su];t1,t2=pv(v1,pl),pv(v2,pl)
        return f'{en} {pvs(t1,pl)} {e(x)} and {pvs(t2,pl)} {e(y)}'+(' either.' if t2[2] else ' too.')
    raise KeyError(s)
LIT={'Namo tassa bhagavato arahato sammāsambuddhassa':'Homage to the Blessed One, the arahant, the Fully Awakened Buddha'}
HOOK=[]   # chapter sentence hooks
def sentence(s):
    if s in LIT: return LIT[s]
    for h in HOOK:
        r=h(s)
        if r: return r
    if s.endswith('…pe….'): return sentence(s[:-5]+'.')[:-1]+'…'
    if '…pe…' in s: return pe_parts(s)
    if re.search(r'(tesaṃ|tāsaṃ|tattha)\.$',s): return frag(s)
    m=re.fullmatch(rf'(.+?) {PRE} {T} {VB}, no ca {PRE} {T} {VB}\.',s)
    if m:
        g,p,x,v1,_,y,v2=m.groups();th='tattha' in p
        return f'{lead(g,p)}, {stmt(e(x),v1,th)}, but {opposite(e(y),v2,th)}.'
    m=re.fullmatch(rf'(.+?) {PRE} {T}(?: ca)? {VB},? {T}(?: ca)? {VB}\.',s)
    if m:
        g,p,x,v1,y,v2=m.groups();th='tattha' in p;n1,n2=verb(v1)[3],verb(v2)[3]
        return f'{lead(g,p)}, {stmt(e(x),v1,th)}, and {stmt(e(y),v2,th)}'+('.' if n1!=n2 else (' either.' if n2 else ' too.'))
    m=re.fullmatch(rf'{CLR} {T} {VB}\.',s)
    if m: return f'{CL[m.group(1).lower()]} {stmt(e(m.group(2)),m.group(3),False)}.'
    m=re.fullmatch(rf'(.+?) {PRE} {T} {VB}\.',s)
    if m and not m.group(1).lower().startswith(('yassa','yattha')):
        return f'{lead(m.group(1),m.group(2))}, {stmt(e(m.group(3)),m.group(4),"tattha" in m.group(2))}.'
    if re.search('parijān|pajah|bhāv|sacchik',s): return pari(s)
    raise KeyError(s)
def sentences(s):
    return ' '.join(sentence(x) for x in re.split(r'(?<=\.) |(?<=…pe…) (?=\()',s.strip()) if x)
def frag(p):
    p=p.strip().rstrip('.')
    m=re.fullmatch(rf'(.*?)(?: ?(?:tesaṃ tattha|tāsaṃ tattha|tesaṃ|tāsaṃ|tattha))?(?: {T})?',p)
    return group(m.group(1))+(f', {e(m.group(2))}' if m.group(2) else '')+'.'
def pe_parts(s):
    out=[]
    for part in s.split('…pe…'):
        part=part.strip()
        if not part: continue
        try: t=sentence(part if part.endswith('.') else part+'.')
        except (KeyError,ValueError,AttributeError): t=frag(part)
        out.append(t)
    r=[]
    for i,t in enumerate(out):
        if i and t.startswith(('For ','And ','Wherever ')): t=t[0].lower()+t[1:]
        r.append(t if i==len(out)-1 else t.rstrip('.'))
    j='… '.join(r)
    return j.rstrip('.')+'…' if s.rstrip().endswith('…pe…') else j
def q_pav(m):
    lab,c,x,v1,t,y,v2,rest=m.groups();v2=verbq(v2);pe=''
    if rest.startswith('…Pe….'): rest=rest[5:];pe='…'
    return f'{LAB.get(lab,"")}{CL[c.lower()]} {stmt(e(x),v1,False)}, {ask(e(y),v2,FT[t])}?{pe}'+(' '+sentences(rest) if rest.strip() else '')
def q_f(m):
    lab,ca,x,v1,y,v2,rest=m.groups();a=fq(v1);b=fq(v2);ld='And whoever' if ca else 'Whoever'
    h=f'{a[0]} not {a[1]}' if a[3] else a[2]
    return f'{LAB[lab]}{ld} {h} {e(x)} – {b[0]} that person {"not " if b[3] else ""}{b[1]} {e(y)}?'+(' '+sentences(rest) if rest.strip() else '')
QPE=re.compile(rf'(?:\((Ka|Kha)\) )?{CLR} ([^?]*?§\w+§) ?{VB}? ?(tassa tattha|tassa|tattha) ([^?]*?§\w+§) ?{VB}\?(.*)')
def bl(x): return '… '.join(e(w) for w in re.findall(T,x))
def q_pe(m):
    lab,c,a,v1,t,b,v2,rest=m.groups();v2=verbq(v2)
    head=stmt(bl(a),v1,False) if v1 else bl(a)
    return f'{LAB.get(lab,"")}{CL[c.lower()]} {head}, {ask(bl(b),v2,FT[t])}?'+(' '+sentences(rest) if rest.strip() else '')
QSH=re.compile(rf'(?:\((Ka|Kha)\) )?{CLR}(?: {T})?(?: {VB})?…pe…(?: {VB})?(\?)?(.*)')
def q_sh(m):
    lab,c,x,v0,vv,qm,rest=m.groups();vt=''
    if vv:
        aux,b,_,n=verb(verbq(vv));vt=f' {aux} it {"not " if n else ""}{b}'
    head=(stmt(e(x),v0,False) if x and v0 else (e(x) if x else ''))
    t=f'{LAB.get(lab,"")}{CL[c.lower()]}'+(' '+head if head else '')+'…'+vt+(qm or '')
    r=rest.strip()
    if r=='.': r=''
    return t+(' '+sentences(r) if r else '')
QYO=re.compile(r'(?:\((Ka|Kha)\) )?[Yy]o vā pana…pe…\?(.*)')
N={};SING={};ACC={};CEVA={};OTHER={};SPEC={};NEGCAT=[];FULL={};CAT={}
def nm(w):
    w=w.strip();l=w[0].lower()+w[1:] if not w.startswith('§') else w
    if l in N: return l
    for t in (l[:-3]+'u' if l.endswith('ūti') else None,l[:-3]+'ṃ' if l.endswith('nti') else None,l[:-2] if l.endswith('ti') else None,l[:-3]+'i' if l.endswith('īti') else None):
        if t and t in N: return t
    raise ValueError('name '+w)
QN=re.compile(r'(?:\((Ka|Kha)\) )?(.+?)\?(…Pe…\.?)?(?: (.*))?')
def q_name(m):
    lab,q,pe,rest=m.groups()
    if '…pe…' in q.lower() or '?' in q: raise ValueError('name q '+q)
    ql=q if q.startswith('§') else q[0].lower()+q[1:];neg=False
    v=re.findall(r' ?⟦\d+⟧',ql);ql=re.sub(r' ?⟦\d+⟧','',ql)
    if ql.startswith('na '): neg=True;ql=ql[3:]
    else:
        for nc,pos in NEGCAT:
            if ql.startswith(nc): neg=True;ql=pos+ql[len(nc):];break
    ws=ql.split()
    if neg:
        last=ws[-1]
        for nc,pos in NEGCAT:
            if last.startswith(nc): ws=[ws[0],pos+last[len(nc):]];break
        else:
            if len(ws)==3 and ws[1]=='na': ws=[ws[0],ws[2]]
            else: raise ValueError('neg '+q)
    if len(ws)!=2: raise ValueError('name q '+q)
    a,b=nm(ws[0]),nm(ws[1])
    if neg: t=f'Is what is not {SING.get(a,N[a])} not {SING.get(b,N[b])}?'
    else: t=f'{"Are" if a in SING else "Is"} {N[a]}{"".join(v)} {N[b]}?'
    return LAB.get(lab,'')+t+('…' if pe else '')+(' '+sentences(rest) if rest else '')
def multi_q(b):
    ps=re.split(r'\?\s*…Pe…\.?\s+',b);o=[]
    for i,x in enumerate(ps):
        if i<len(ps)-1: x+='?'
        t=piece(x);o.append(t if i==0 else t[0].lower()+t[1:])
    return '… '.join(o)
def piece(b):
    if b in FULL: return FULL[b]
    m=QP.fullmatch(b)
    if m: return q_pav(m)
    m=QF.fullmatch(b)
    if m: return q_f(m)
    m=QYO.fullmatch(b)
    if m: return LAB.get(m.group(1),'')+'And whoever…?'+(' '+sentences(m.group(2)) if m.group(2).strip() else '')
    m=QPE.fullmatch(b)
    if m: return q_pe(m)
    m=QSH.fullmatch(b)
    if m: return q_sh(m)
    if re.search(r'\?\s*…Pe…\.?\s+\S',b): return multi_q(b)
    if '?' in b: return q_name(QN.fullmatch(b))
    return sentences(b)
def terms_hook(s):
    if not CAT: return None
    ls=s if s.startswith('§') else s[0].lower()+s[1:]
    cw=CAT['pl']
    for k,(en,n) in SPEC.items():
        m=re.fullmatch(re.escape(k)+rf' \S+, na {T}\.',s)
        if m: return f'{en} are {n}, but not {e(m.group(1))}.'
        m=re.fullmatch(re.escape(k)+rf' na {T}, \S+\.',s)
        if m: return f'{en} are not {e(m.group(1))}, but they are {n}.'
    m=re.fullmatch(rf'{T} (\S+?)(?: ceva|ceva) \1(?: ca)?\.',ls)
    if m and m.group(2) in CEVA: return f'{cap(e(m.group(1)))} is both {N[CEVA[m.group(2)]]} and {e(m.group(1))}.'
    m=re.fullmatch(rf'{T} ṭhapetvā (?:avaseso|avasesaṃ|avasesā) ([^\s,]+)( ⟦\d+⟧)?,? na \1\.',ls)
    if m:
        o,n=OTHER[m.group(2)];return f'Apart from {e(m.group(1))}, {o}{m.group(3) or ""} is {n}, but not {e(m.group(1))}.'
    m=re.fullmatch(rf'{T} ṭhapetvā (?:avaseso|avasesaṃ|avasesā) na \1, (\S+)\.',ls)
    if m:
        o,n=OTHER[m.group(2)];return f'Apart from {e(m.group(1))}, {o} is not {e(m.group(1))}, but it is {n}.'
    m=re.fullmatch(rf'(\S+) {T} ca ṭhapetvā (?:avaseso|avasesaṃ|avasesā)( ⟦\d+⟧)? na ceva (\S+) na ca \2\.',s)
    if m: return f'Apart from {N[ACC[m.group(1)]]} and {e(m.group(2))}, the rest{m.group(3) or ""} are neither {N[m.group(4)]} nor {e(m.group(2))}.'
    m=re.fullmatch(rf'Avasesā {cw}( ⟦\d+⟧)? na {T}\.',s)
    if m: return f'The remaining {CAT["en"]}{m.group(1) or ""} are not {e(m.group(2))}.'
    m=re.fullmatch(rf'(\S+) ṭhapetvā avasesā {cw} na (\S+), {cw}\.',s)
    if m:
        a=N[ACC[m.group(1)]];return f'Apart from {a}, the remaining {CAT["en"]} are not {a}, but they are {CAT["en"]}.'
    m=re.fullmatch(rf'(\S+) {CAT["ca"]} ṭhapetvā (?:avasesā|avasesaṃ) na ceva (\S+) na ca {cw}\.',s)
    if m:
        a=N[ACC[m.group(1)]];return f'Apart from {a} and the {CAT["en"]}, the rest are neither {a} nor {CAT["en"]}.'
    m=re.fullmatch(rf'\({T}mūlakaṃ\)\.?',s)
    if m: return f'(Based on {e(m.group(1))}.)'
    return None
HOOK.append(terms_hook)
