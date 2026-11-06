"""Rails translation of chapter 7 (Pairs on Underlying Tendencies)."""
import re,sys
sys.path.insert(0,'pi-6-rails-scripts')
from common import *
T={'kāmarāg':'sensual desire','kāmārāg':'sensual desire','paṭigh':'aversion','mān':'conceit','diṭṭh':'wrong view','vicikicch':'doubt','bhavarāg':'desire for existence','avijj':'ignorance'}
ST='(?:'+'|'.join(T)+')'
END=r'(?:ñca|ṃ|o|ā|ena|añca|aṃ)'
TOK=rf'{ST}ānusay{END}(?: ca)?(?:…pe…|…)?'
def names(x): return [T[m.lower()] for m in re.findall(rf'({ST})ānusay',x,flags=re.I)]
def tl(x):
    n=names(x)
    if not n: raise ValueError('names '+x)
    if len(n)==1: return f'the underlying tendency to {n[0]}'
    if '…' in x: return 'the underlying tendency to '+'… to '.join(n)
    return 'the underlying tendencies to '+', '.join(n[:-1])+' and '+n[-1]
def plural(x): return len(names(x))>1 and '…' not in x
def vi(v):
    w=v.replace('na parijān','naparijān')
    for forms,r in (((('anuseti','anusenti','anusetīti','anusentīti','anusetī')),('S','lat',0)),(('nānuseti','nānusenti','nānusetīti','nānusentīti'),('S','lat',1)),(('pahīno','pahīnā','pahīnoti','pahīnāti'),('S','aban',0)),(('appahīno','appahīnā','appahīnoti','appahīnāti'),('S','aban',1)),(('uppajjati','uppajjanti','uppajjatīti','uppajjantīti'),('S','ari',0)),(('nuppajjati','nuppajjanti','nuppajjatīti','nuppajjantīti'),('S','ari',1)),(('pajahati','pajahanti','pajahatīti','pajahantīti'),('A','abandon',0)),(('nappajahati','nappajahanti','nappajahatīti','nappajahantīti'),('A','abandon',1)),(('parijānāti','parijānanti','parijānātīti','parijānantīti'),('A','fully understand',0)),(('naparijānāti','naparijānanti','naparijānātīti','naparijānantīti'),('A','fully understand',1)),(('sānusayo','sānusayā','sānusayoti','sānusayāti'),('H','have',0)),(('niranusayo','niranusayā','niranusayoti','niranusayāti'),('H','free',0))):
        if w in forms: return r
    raise ValueError('verb '+v)
VBS=r'(na parijān\w+|nappajah\w+|nānuse\w+|nuppajj\w+|appahīn\w+|anuse\w+|pahīn\w+|uppajj\w+|pajah\w+|parijān\w+|sānusay\w+|niranusay\w+)'
def spred(k,pl,neg):
    return {'lat':(('do not lie latent' if pl else 'does not lie latent') if neg else ('lie latent' if pl else 'lies latent')),'aban':(('are not abandoned' if pl else 'is not abandoned') if neg else ('are abandoned' if pl else 'is abandoned')),'ari':(('do not arise' if pl else 'does not arise') if neg else ('arise' if pl else 'arises'))}[k]
def apred(verb,pl,neg):
    if neg: return f'{"do" if pl else "does"} not {verb}'
    if pl: return verb
    return verb.replace('understand','understands') if 'understand' in verb else verb+'s'
def clause(x,v,ppl,there,flip=False):
    k,w,neg=vi(v);t=tl(x);th=' there' if there else ''
    if k=='S':
        pl=plural(x)
        if flip and neg:
            base={'lat':'do lie latent' if pl else 'does lie latent','aban':'are abandoned' if pl else 'is abandoned','ari':'do arise' if pl else 'does arise'}[w]
            return f'{t} {base}{th}'
        return f'{t} {spred(w,pl,(not neg) if flip else neg)}{th}'
    if k=='A':
        if flip and neg: return f'{"do" if ppl else "does"} {w} {t}{th}'
        return f'{apred(w,ppl,(not neg) if flip else neg)} {t}{th}'
    if w=='have':
        return f'{"do" if ppl else "does"} not have {t}{th}' if flip else f'{"have" if ppl else "has"} {t}{th}'
    return f'{"are" if ppl else "is"} not free of {t}{th}' if flip else f'{"are" if ppl else "is"} free of {t}{th}'
PN={'Anāgāmimaggasamaṅgiṃ ṭhapetvā avasesā puggalā':('Apart from one who possesses the path of non-returning, the remaining persons',1),'Aggamaggasamaṅgiṃ ṭhapetvā avasesā puggalā':('Apart from one who possesses the highest path, the remaining persons',1),'Dvinnaṃ maggasamaṅgīnañca aṭṭhamakañca ṭhapetvā avasesā puggalā':('Apart from those possessing the two paths and one at the eighth stage, the remaining persons',1),'Anāgāmī':('A non-returner',0),'Arahā':('An arahant',0),'Aggamaggasamaṅgī':('One who possesses the highest path',0),'Anāgāmimaggasamaṅgī':('One who possesses the path of non-returning',0),'Puthujjano':('An ordinary person',0),'Aṭṭhamako':('One at the eighth stage',0),'Tayo puggalā':('Three kinds of person',1),'Dve puggalā':('Two kinds of person',1),'Cattāro puggalā':('Four kinds of person',1),'Sveva puggalo':('That same person',0),'Teva puggalā':('Those same persons',1),'Dvinnaṃ maggasamaṅgīnaṃ ṭhapetvā avasesā puggalā':('Apart from those possessing the two paths, the remaining persons',1),'Anāgāmimaggasamaṅgiñca aṭṭhamakañca ṭhapetvā avasesā puggalā':('Apart from one who possesses the path of non-returning and one at the eighth stage, the remaining persons',1),'Aggamaggasamaṅgiñca anāgāmimaggasamaṅgiñca ṭhapetvā avasesā puggalā':('Apart from one who possesses the highest path and one who possesses the path of non-returning, the remaining persons',1),'Aggamaggasamaṅgiñca aṭṭhamakañca ṭhapetvā avasesā puggalā':('Apart from one who possesses the highest path and one at the eighth stage, the remaining persons',1),'Tiṇṇaṃ maggasamaṅgīnaṃ ṭhapetvā avasesā puggalā':('Apart from those possessing the three paths, the remaining persons',1),'Sveva':('That same person',0),'Te':('They',1),'Dvinnaṃ maggasamaṅgīnaṃ':('Those possessing the two paths',1),'Dve maggasamaṅgino':('Those possessing the two paths',1),'Tayo maggasamaṅgino':('Those possessing the three paths',1)}
PG={'Anāgāmissa':'For a non-returner','Arahato':'For an arahant','Puthujjanassa':'For an ordinary person','Tiṇṇaṃ puggalānaṃ':'For three kinds of person','Dvinnaṃ puggalānaṃ':'For two kinds of person','Catunnaṃ puggalānaṃ':'For four kinds of person','Tasseva puggalassa':'For that same person','Tesaññeva puggalānaṃ':'For those same persons','Tesaṃyeva puggalānaṃ':'For those same persons'}
LC={'kāmadhātuyā dvīsu vedanāsu':'in the sense-pleasure element, in two kinds of feeling','kāmadhātuyā tīsu vedanāsu':'in the sense-pleasure element, in three kinds of feeling','dukkhāya vedanāya':'in painful feeling','rūpadhātuyā':'in the material-form element','arūpadhātuyā':'in the immaterial element','kāmadhātuyā':'in the sense-pleasure element','sabbasakkāyapariyāpannesu dhammesu':'in all phenomena included in personal existence','apariyāpanne':'in what is not included','sabbattha':'everywhere'}
LCK=sorted(LC,key=len,reverse=True)
def locs(s):
    o=[];r=s
    while True:
        for k in LCK:
            if r.lower().startswith(k+' ') or r.lower()==k or r.lower().startswith(k+', '):
                o.append(LC[k]);r=r[len(k):].lstrip(', ').strip();break
        else: break
    if not o: return '',s
    return (o[0] if len(o)==1 else ', '.join(o[:-1])+' and '+o[-1]),r
def head(s):
    for k in sorted(PN,key=len,reverse=True):
        if s.startswith(k+' '):
            en,pl=PN[k];lc,r=locs(s[len(k)+1:]);return en+(', '+lc+',' if lc else ''),pl,'N',r
    for k in sorted(PG,key=len,reverse=True):
        if s.startswith(k+' '):
            lc,r=locs(s[len(k)+1:]);return PG[k]+(', '+lc if lc else '')+',',0,'G',r
    lc,r=locs(s)
    if lc: return lc[0].upper()+lc[1:]+',',0,'L',r
    return '',0,'',s
CHK=re.compile(rf'\s*(, no ca |no ca |; |, |)((?:tassa tattha|tesaṃ tattha|so tato|te tato|tassa|tesaṃ|ettha|tato|tattha|so|te) )?((?:{TOK} ?)+)(tadekaṭṭhaṃ )?(?:{VBS}|(na vattabb[oā] "pahīn[oā]"ti vā "appahīn[oā]"ti vā))',re.I)
def thr(c): return bool(c) and any(a in c for a in('tattha','tato','ettha'))
def sent(s):
    s=s.replace(' ariyāpanne so',' apariyāpanne so')
    if '; apariyāpanne' in s: return sentences(s.replace('; apariyāpanne','. Apariyāpanne'))
    if s.endswith(' (vitthāretabbaṃ).'): return sent(s[:-18]+'.')+' (To be expanded.)'
    h,pl,kind,r=head(s)
    pe=r.endswith('…pe….')
    r=re.sub(r' ?…pe…\.$','',r).rstrip('.').strip();pos=0;cl=[]
    while pos<len(r):
        m=CHK.match(r,pos)
        if not m or m.end()==pos: raise KeyError(s)
        cl.append(m.groups());pos=m.end()
    if not cl: raise KeyError(s)
    there=thr(cl[0][1]) if cl[0][1] else False;out=''
    for i,(cn,c,x,td,v,nv) in enumerate(cl):
        if c is not None and thr(c): there=True
        if nv:
            out+=f'; {tl(x)} {"are" if plural(x) else "is"} not to be called either "abandoned" or "not abandoned"';continue
        k=vi(v)[0];flip=cn.strip(', ').startswith('no ca')
        t=clause(x,v,pl,there,flip)
        if k!='S' and kind!='N': t='one '+t
        if td: t+=', which are conjoined with it' if plural(x) else ', which is conjoined with it'
        if i==0: out=t
        elif flip: out+=', but '+t
        elif cn.strip()==';': out+='; '+t
        elif td: out+=', and '+t
        else: out+=', and '+t+(' either' if vi(v)[2] else ' too')
    res=(f'{h} {out}.' if not pe else f'{h} {out}…').strip()
    return res[0].upper()+res[1:]
SP={'(Vitthāretabbaṃ).':'(To be expanded.)','Uppajjanavāro.':'The section on arising.','Dhātupucchāvāro.':'The section of questions on the elements.','(Kāmadhātumūlakaṃ)':'(Based on the sense-pleasure element.)','(Rūpadhātumūlakaṃ)':'(Based on the material-form element.)','(Arūpadhātumūlakaṃ)':'(Based on the immaterial element.)','(Nakāmadhātumūlakaṃ)':'(Based on what is not the sense-pleasure element.)','(Narūpadhātumūlakaṃ)':'(Based on what is not the material-form element.)','(Naarūpadhātumūlakaṃ)':'(Based on what is not the immaterial element.)','(Nakāmanaarūpadhātumūlakaṃ)':'(Based on neither the sense-pleasure element nor the immaterial element.)','(Narūpanaarūpadhātumūlakaṃ)':'(Based on neither the material-form element nor the immaterial element.)','(Nakāmanarūpadhātumūlakaṃ)':'(Based on neither the sense-pleasure element nor the material-form element.)','9':'9',
'Anusayavāre anulomaṃ.':'The positive part of the section on underlying tendencies.','Anusayavāre paṭilomaṃ.':'The negative part of the section on underlying tendencies.','Anusayavāro.':'The section on underlying tendencies.','Sānusayavāre anulomaṃ.':'The positive part of the section on having underlying tendencies.','Sānusayavāre paṭilomaṃ.':'The negative part of the section on having underlying tendencies.','Sānusayavāro.':'The section on having underlying tendencies.','Pajahanavāre anulomaṃ.':'The positive part of the section on abandoning.','Pajahanāvāre paṭilomaṃ.':'The negative part of the section on abandoning.','Pajahanavāro.':'The section on abandoning.','Pariññāvāre anulomaṃ.':'The positive part of the section on full understanding.','Pariññāvāre paṭilomaṃ.':'The negative part of the section on full understanding.','Pariññāvāro.':'The section on full understanding.','Pahīnavāre anulomaṃ.':'The positive part of the section on what is abandoned.','Pahīnavāre paṭilomaṃ.':'The negative part of the section on what is abandoned.','Pahīnavāro.':'The section on what is abandoned.',
'Āmantā.':'Yes.','Natthi.':'There is no such case.','No.':'No.','Āmantā …pe….':'Yes…','Āmantā…pe….':'Yes…','Tadekaṭṭhaṃ pajahati.':'One abandons what is conjoined with it.','Tadekaṭṭhaṃ parijānāti.':'One fully understands what is conjoined with it.','Na vattabbo "pahīno"ti vā "appahīno"ti vā.':'It is not to be called either "abandoned" or "not abandoned".','Na vattabbā "pahīnā"ti vā "appahīnā"ti vā.':'They are not to be called either "abandoned" or "not abandoned".',
'(Ekamūlakaṃ)':'(Based on one.)','(Ekamūlakaṃ )':'(Based on one.)','(Dukamūlakaṃ)':'(Based on two.)','(Tikamūlakaṃ)':'(Based on three.)','(Catukkamūlakaṃ)':'(Based on four.)','(Pañcakamūlakaṃ)':'(Based on five.)','(Chakkamūlakaṃ)':'(Based on six.)','Uppattiṭṭhānavāro.':'The section on the place of arising.','Arahato sabbattha…pe….':'For an arahant, everywhere…','Dvinnaṃ puggalānaṃ sabbattha…pe….':'For two kinds of person, everywhere…',
'Sattānusayā – kāmarāgānusayo, paṭighānusayo, mānānusayo, diṭṭhānusayo, vicikicchānusayo, bhavarāgānusayo, avijjānusayo.':'There are seven underlying tendencies – the underlying tendency to sensual desire, to aversion, to conceit, to wrong view, to doubt, to desire for existence, to ignorance.',
'Dhātuvisajjavāro.':'The section of answers on the elements.','Anusayayamakaṃ niṭṭhitaṃ.':'The Pairs on Underlying Tendencies are complete.','Namo tassa bhagavato arahato sammāsambuddhassa':'Homage to the Blessed One, the arahant, the Fully Awakened Buddha'}
HD={'Anusayayamakaṃ':'The Pairs on Underlying Tendencies','Uppattiṭṭhānavāro':'The Section on the Place of Arising','Mahāvāro 1. anusayavāro':'The Great Section: 1. Underlying Tendencies','Anusayavāra':'Underlying Tendencies','Sānusayavāro':'The Section on Having Underlying Tendencies','Sānusayavāra':'Having Underlying Tendencies','Pajahanavāro':'The Section on Abandoning','Pajahanavāra':'Abandoning','Pariññāvāro':'The Section on Full Understanding','Pariññāvāra':'Full Understanding','Pahīnavāro':'The Section on What Is Abandoned','Pahīnavāra':'What Is Abandoned','Uppajjanavāro':'The Section on Arising','(Ka) dhātupucchāvāro':'(a) Questions on the Elements','(Kha) dhātuvisajjanāvāro':'(b) Answers on the Elements','(Ka) anulomapuggalo':'(a) Positive: Person','(Kha) anulomaokāso':'(b) Positive: Place','(Ga) anulomapuggalokāsā':'(c) Positive: Person and Place','(Gha) paṭilomapuggalo':'(d) Negative: Person','(Ṅa) paṭilomaokāso':'(e) Negative: Place','(Ca) paṭilomapuggalokāsā':'(f) Negative: Person and Place'}
LAB={'Ka':'(a) ','Kha':'(b) '}
QRE=re.compile(rf'(?:\((Ka|Kha)\) )?([Yy]o vā pana yato|[Yy]o yato|[Yy]o vā pana|[Yy]o|[Yy]ato vā pana|[Yy]ato|[Yy]assa vā pana yattha|[Yy]assa yattha|[Yy]assa vā pana|[Yy]assa|[Yy]attha vā pana|[Yy]attha) (.+?) ?{VBS} (so tato|tassa tattha|so|tato|tassa|tattha) (.+?) ?{VBS}\?(.*)')
def q(m):
    lab,c,x,v1,t,y,v2,rest=m.groups();c=c.lower();k,w,n=vi(v1);k2,w2,n2=vi(v2);pn='vā pana' in c;tx=tl(x);ty=tl(y)
    if k=='S':
        ld={'yassa':'For whomever','yattha':'Wherever','yassa yattha':'For whomever and wherever'}[c.replace(' vā pana','')]
        if pn: ld='And '+ld[0].lower()+ld[1:]
        a=spred(w,plural(x),n);ft={'tassa':' for them','tattha':' there','tassa tattha':' for them there'}[t]
        aux={'lat':'do' if plural(y) else 'does','aban':'are' if plural(y) else 'is','ari':'do' if plural(y) else 'does'}[w2];tail={'lat':'lie latent','aban':'abandoned','ari':'arise'}[w2]
        out=f'{ld} {tx} {a}, {aux} {ty}{" not" if n2 else ""} {tail}{ft}?'
    else:
        kk=c.replace(' vā pana','')
        act=lambda kd,ww,nn,xx:(apred(ww,False,nn)+' '+xx if kd=='A' else ('has ' if ww=='have' else 'is free of ')+xx)
        ask=lambda kd,ww,nn,xx,p:(f'does {p}{" not" if nn else ""} {ww} {xx}' if kd=='A' else (f'does {p} have {xx}' if ww=='have' else f'is {p} free of {xx}'))
        if kk=='yo': out=f'{"And whoever" if pn else "Whoever"} {act(k,w,n,tx)} – {ask(k2,w2,n2,ty,"that person")}?'
        elif kk=='yato': out=f'{"And wherever" if pn else "Wherever"} one {act(k,w,n,tx)}, {ask(k2,w2,n2,ty,"one")} there?'
        else: out=f'{"And whoever" if pn else "Whoever"} {act(k,w,n,tx)} wherever – {ask(k2,w2,n2,ty,"that person")} there?'
    r=rest.strip();return LAB.get(lab,'')+out+(' '+sentences(r) if r else '')
S1={'kāmadhātu':'the sense-pleasure element','rūpadhātu':'the material-form element','arūpadhātu':'the immaterial element'}
def lfrom(g):
    ws=re.findall(r'(na )?(kāmadhātuyā|rūpadhātuyā|arūpadhātuyā)',g.lower());n=[S1[w[1][:-3]+'u'] for w in ws]
    if ws[0][0]: return 'neither '+' nor '.join(n) if len(n)>1 else 'what is not '+n[0]
    return n[0]
def lto(g):
    ws=re.findall(r'(na )?(kāmadhātuṃ|rūpadhātuṃ|arūpadhātuṃ)',g.lower());n=[S1[w[1][:-1]] for w in ws]
    if ws[0][0]: return 'in neither '+' nor '.join(n) if len(n)>1 else 'in what is not '+n[0]
    return 'in '+n[0]
NUM={'satt':'seven','satta':'seven','pañca':'five','tayo':'three','cha':'six','cattāro':'four','dve':'two','eko':'one'}
def dhatu(s):
    s=s.strip()
    m=re.fullmatch(r'(.+?) cutassa (.+?) upapajjantassa kati anusayā anusenti, kati anusayā nānusenti, kati anusayā bhaṅgā\?',s)
    if m: return f'For one who has passed away from {lfrom(m.group(1))} and is being reborn {lto(m.group(2))}, how many underlying tendencies lie latent, how many do not lie latent, and how many are dissolved?'
    m=re.fullmatch(r'(.+?) cutassa (.+?) upapajjantassa (.+?); anusayā bhaṅgā natthi\.?',s)
    if m:
        ps=[]
        for c in m.group(3).split(', '):
            mm=re.fullmatch(r'kassaci (\w+) anusayā anusenti',c)
            if mm: ps.append(f'in some cases {NUM[mm.group(1)]} underlying tendencies lie latent');continue
            mm=re.fullmatch(r'(\w+)eva anusayā anusenti',c)
            if mm: ps.append(f'exactly {NUM[mm.group(1)]} underlying tendencies lie latent');continue
            raise KeyError(c)
        return f'For one who has passed away from {lfrom(m.group(1))} and is being reborn {lto(m.group(2))}, '+', '.join(ps)+'; none are dissolved.'
    m=re.fullmatch(r'(.+?) cutassa (.+?) (?:upapatti ?nāma|upapatti) natthi, heṭṭhā upapajjamāno (kāmadhātuṃ|rūpadhātuṃ)yeva upapajjati, (\w+)eva anusayā anusenti; anusayā bhaṅgā natthi\.?',s)
    if m: return f'For one who has passed away from {lfrom(m.group(1))}, there is no such thing as rebirth {lto(m.group(2).replace("dhātuyā","dhātuṃ"))}. Being reborn lower, one is reborn only in {S1[m.group(3)[:-1]]}; exactly {NUM[m.group(4)]} underlying tendencies lie latent; none are dissolved.'
    raise KeyError(s)
def sentences(s): return ' '.join(one(x) for x in re.split(r'(?<=\.) ',s.strip()) if x)
def one(x): return SP[x] if x in SP else sent(x)
def tr(body):
    body=body.replace(' anusanti',' anusenti').replace('kati anusayā bhaṅgā. ','kati anusayā bhaṅgā? ')
    if body.endswith('kati anusayā bhaṅgā.'): body=body[:-1]+'?'
    if 'cutassa' in body: return ' '.join(dhatu(x) if 'cutassa' in x else one(x) for x in re.split(r'(?<=[.?]) ',body))
    if body in SP: return SP[body]
    if re.search(r'(?<=\.) (?=(?:Yassa|Yato|Yattha|Yo) )',body):
        return ' '.join(tr(x) for x in re.split(r'(?<=\.) (?=(?:Yassa|Yato|Yattha|Yo) )',body))
    vm=re.search(r' (⟦\d+⟧) ',body)
    if vm and '?' in body: return tr(body.replace(vm.group(0),' ',1))+' '+vm.group(1)
    m=QRE.fullmatch(body)
    msh=re.fullmatch(r'(?:\((Ka|Kha)\) )?([Yy]o vā pana yato|[Yy]o yato|[Yy]o vā pana|[Yy]ato vā pana|[Yy]assa vā pana yattha|[Yy]assa yattha|[Yy]assa vā pana|[Yy]attha vā pana)…pe…\?(.*)',body)
    mk=re.fullmatch(rf'Kattha ({ST}ānusayo) anuseti\? (.*)',body)
    if m: return q(m)
    if msh: return LAB.get(msh.group(1),'')+{'yo vā pana yato':'And whoever, wherever','yo yato':'Whoever, wherever','yo vā pana':'And whoever','yato vā pana':'And wherever','yassa vā pana yattha':'And for whomever and wherever','yassa yattha':'For whomever and wherever','yassa vā pana':'And for whomever','yattha vā pana':'And wherever'}[msh.group(2).lower()]+'…?'+(' '+sentences(msh.group(3)) if msh.group(3).strip() else '')
    if mk: return f'Where does {tl(mk.group(1))} lie latent? '+sentences(mk.group(2))
    return sentences(body)
if __name__=='__main__':
    S={}
    for i in range(1,12):
        f=f'7-{i:02d}-anusayayamaka.md';o,bad=run(f,tr,HD);print(f,'unmatched',len(bad))
        for ln,e,b in bad: S.setdefault(e[:36],[0,f[:4],ln,e[:90],b[:170]])[0]+=1
        if not bad: write(f,o);check(f)
    for v in list(S.values())[:25]: print(v)
