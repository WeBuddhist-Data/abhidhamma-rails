"""Rails translation of chapter 8 (Pairs on Consciousness)."""
import re,sys
sys.path.insert(0,'pi-6-rails-scripts')
from common import *
VP={'uppajjati':('arises','does not arise','does arise'),'uppajjittha':('has arisen','has not arisen','has arisen'),'uppajjissati':('will arise','will not arise','will arise'),'nirujjhati':('ceases','does not cease','does cease'),'nirujjhittha':('has ceased','has not ceased','has ceased'),'nirujjhissati':('will cease','will not cease','will cease'),'uppannaṃ':('is arisen','is not arisen','is arisen'),'uppajjamānaṃ':('is arising','is not arising','is arising'),'nirujjhamānaṃ':('is ceasing','is not ceasing','is ceasing'),'niruddhaṃ':('is ceased','is not ceased','is ceased')}
AUX={'uppajjati':('does','arise'),'uppajjittha':('has','arisen'),'uppajjissati':('will','arise'),'nirujjhati':('does','cease'),'nirujjhittha':('has','ceased'),'nirujjhissati':('will','cease'),'uppannaṃ':('is','arisen'),'uppajjamānaṃ':('is','arising'),'nirujjhamānaṃ':('is','ceasing'),'niruddhaṃ':('is','ceased')}
VR='(?:'+'|'.join(VP)+')'
ADJ={'cittaṃ':'consciousness','kusalaṃ cittaṃ':'wholesome consciousness','akusalaṃ cittaṃ':'unwholesome consciousness','abyākataṃ cittaṃ':'indeterminate consciousness','sarāgaṃ cittaṃ':'consciousness with lust','vītarāgaṃ cittaṃ':'consciousness without lust','sadosaṃ cittaṃ':'consciousness with hatred','vītadosaṃ cittaṃ':'consciousness without hatred','samohaṃ cittaṃ':'consciousness with delusion','vītamohaṃ cittaṃ':'consciousness without delusion','saraṇaṃ cittaṃ':'consciousness with conflict','araṇaṃ cittaṃ':'consciousness without conflict'}
ADJR=r'((?:(?:kusalaṃ|akusalaṃ|abyākataṃ|sarāgaṃ|vītarāgaṃ|sadosaṃ|vītadosaṃ|samohaṃ|vītamohaṃ|saraṇaṃ|araṇaṃ) )?cittaṃ)'
def nv(x):
    x=x.lower().strip()
    x=re.sub(r'(uppajjatī|uppajjissatī|nirujjhatī|nirujjhissatī)ti$',lambda m:m.group(1)[:-1]+'i',x)
    x=re.sub(r'(uppajjitthā|nirujjhitthā)ti$',lambda m:m.group(1)[:-1]+'a',x)
    return re.sub(r'(uppanna|uppajjamāna|nirujjhamāna|niruddha)nti$',r'\1ṃ',x)
def vlist(x):
    o=[];neg=False
    for t in [nv(t) for t in nv(x).split()]:
        if t=='na': neg=True;continue
        if t not in VP: raise KeyError('v '+t)
        o.append((neg,t));neg=False
    return o
def stm(vs):
    ps=[VP[v][1 if n else 0] for n,v in vs]
    if len(ps)==2: return f'{ps[0]} but {ps[1]}' if vs[0][0]!=vs[1][0] else f'{ps[0]} and {ps[1]}'
    return ps[0]
def ask(vs,subj,suf):
    n,v=vs[0];a,b=AUX[v];t=f'{a} {subj}{" not" if n else ""} {b}'
    for n2,v2 in vs[1:]:
        t+=(f' and not {AUX[v2][1]}' if n2 else f' and {AUX[v2][1]}')
    return t+suf
LB={'Ka':'(a) ','Kha':'(b) '}
C={'yassa':'For whomever','yassa vā pana':'And for whomever','yaṃ':'Whatever','yaṃ vā pana':'And whatever'}
def qq(b):
    b=b.replace('cittanti?','cittaṃ?')
    m=re.fullmatch(r'(?:\((Ka|Kha)\) )?(na )?(\w+) (?:na )?(\w+)\?',b)
    if m and nv(m.group(3)) in VP and nv(m.group(4)) in VP:
        lab,neg,a,c=m.groups();a,c=nv(a),nv(c);aa=AUX[a][1];ac=AUX[c][1]
        return f'{LB.get(lab,"")}Is what is not {aa} not {ac}?' if neg else f'{LB.get(lab,"")}Is what is {aa} {ac}?'
    m=re.fullmatch(r'(?:\((Ka|Kha)\) )?(yassa vā pana yaṃ|yassa yaṃ|yassa vā pana|yassa|yaṃ vā pana|yaṃ) cittaṃ (na )?(uppajjamānaṃ|nirujjhamānaṃ) khaṇaṃ khaṇaṃ vītikkantaṃ atikkantakālaṃ, (na )?(uppajjamānaṃ|nirujjhamānaṃ) khaṇaṃ khaṇaṃ vītikkantaṃ atikkantakālaṃ (tassa taṃ|tassa|taṃ) cittaṃ\?',b)
    if m:
        lab,c,n1,a,n2,d,t=m.groups()
        ld={'yassa':'For whomever consciousness','yassa vā pana':'And for whomever consciousness','yassa yaṃ':'For whomever a given consciousness','yassa vā pana yaṃ':'And for whomever a given consciousness','yaṃ':'Whatever consciousness','yaṃ vā pana':'And whatever consciousness'}[c]
        w={'uppajjamānaṃ':'in arising','nirujjhamānaṃ':'in ceasing'}
        pp=lambda n,x:f'{w[x]} has {"not " if n else ""}passed its moment, with its time {"not " if n else ""}gone'
        tl={'tassa':'is it so for them','taṃ':'is it so of that consciousness','tassa taṃ':'is it so of that consciousness for them'}[t]
        return f'{LB.get(lab,"")}{ld} {pp(n1,a)}, and {pp(n2,d)} – {tl}?'
    mm=re.fullmatch(rf'(?:\((Ka|Kha)\) )?(yassa vā pana|yassa|yaṃ vā pana|yaṃ) (yaṃ )?{ADJR} (.+?) no ca (?:tassa )?(?:taṃ )?(?:\w+ )?cittaṃ (na )?(\w+), (tassa taṃ|tassa|taṃ) (?:\w+ )?cittaṃ (.+?)\?',b)
    if mm:
        lab,c,y,s_,v1,nn,v0,t,v2=mm.groups();sn=ADJ[s_.lower()];ld=C[c.lower()];giv=bool(y) or c.startswith('yaṃ')
        return f'{LB.get(lab,"")}{ld} {"a given "+sn if y else sn} {stm(vlist(v1))} but {VP[nv(v0)][2 if nn else 1]}, {ask(vlist(v2),("that "+sn) if giv else sn," for them" if t.startswith("tassa") else "")}?'
    m=re.fullmatch(rf'(?:\((Ka|Kha)\) )?([Yy]assa vā pana|[Yy]assa) (yaṃ )?{ADJR} (.+?) (tassa (?:taṃ )?)(?:\w+ )?cittaṃ (.+?)\?',b)
    if m:
        lab,c,y,s_,v1,t,v2=m.groups();sn=ADJ[s_.lower()]
        if y: return f'{LB.get(lab,"")}{C[c.lower()]} a given {sn} {stm(vlist(v1))}, {ask(vlist(v2),"that "+sn," for them")}?'
        return f'{LB.get(lab,"")}{C[c.lower()]} {sn} {stm(vlist(v1))}, {ask(vlist(v2),sn," for them")}?'
    m=re.fullmatch(rf'(?:\((Ka|Kha)\) )?([Yy]aṃ vā pana|[Yy]aṃ) {ADJR} (.+?) taṃ (?:\w+ )?cittaṃ (.+?)\?',b)
    if m:
        lab,c,s_,v1,v2=m.groups();sn=ADJ[s_.lower()]
        return f'{LB.get(lab,"")}{"And whatever" if "pana" in c else "Whatever"} {sn} {stm(vlist(v1))}, {ask(vlist(v2),"that "+sn,"")}?'
    raise KeyError(b)
LEAD={'cittassa bhaṅgakkhaṇe':'At the moment of dissolution of consciousness',
'cittassa uppādakkhaṇe':'At the moment of arising of consciousness',
'pacchimacittassa bhaṅgakkhaṇe':'At the moment of dissolution of the final consciousness',
'pacchimacittassa uppādakkhaṇe':'At the moment of arising of the final consciousness',
'pacchimacittasamaṅgīnaṃ':'For those possessing the final consciousness',
'cittasamaṅgīnaṃ':'For those possessing consciousness',
'nirodhasamāpannānaṃ asaññasattānaṃ':'For those in the attainment of cessation and non-percipient beings',
'cittassa bhaṅgakkhaṇe nirodhasamāpannānaṃ asaññasattānaṃ':'At the moment of dissolution of consciousness, for those in the attainment of cessation and non-percipient beings',
'cittassa uppādakkhaṇe nirodhasamāpannānaṃ asaññasattānaṃ':'At the moment of arising of consciousness, for those in the attainment of cessation and non-percipient beings',
'itaresaṃ':'For the others',
'itaresaṃ cittassa uppādakkhaṇe':'For the others, at the moment of arising of consciousness',
'itaresaṃ cittassa bhaṅgakkhaṇe':'For the others, at the moment of dissolution of consciousness',
'itaresaṃ cittasamaṅgīnaṃ':'For the others possessing consciousness',
'sabbesaṃ cittassa bhaṅgakkhaṇe nirodhasamāpannānaṃ asaññasattānaṃ':'For everyone at the moment of dissolution of consciousness, for those in the attainment of cessation and non-percipient beings',
'sabbesaṃ cittassa uppādakkhaṇe nirodhasamāpannānaṃ asaññasattānaṃ':'For everyone at the moment of arising of consciousness, for those in the attainment of cessation and non-percipient beings',
'sabbesaṃ cittassa bhaṅgakkhaṇe':'For everyone at the moment of dissolution of consciousness',
'sabbesaṃ cittassa uppādakkhaṇe':'For everyone at the moment of arising of consciousness',
'pacchimakusalacittassa uppādakkhaṇe':'At the moment of arising of the final wholesome consciousness',
'sarāgapacchimacittassa uppādakkhaṇe':'At the moment of arising of the final consciousness with lust'}
SUBJ={'bhaṅgakkhaṇe cittaṃ':'Consciousness at the moment of dissolution','uppādakkhaṇe cittaṃ':'Consciousness at the moment of arising','atītaṃ cittaṃ':'Past consciousness','anāgataṃ cittaṃ':'Future consciousness','paccuppannaṃ cittaṃ':'Present consciousness','atītānāgataṃ cittaṃ':'Past and future consciousness','uppādakkhaṇe anāgatañca cittaṃ':'Consciousness at the moment of arising and future consciousness','uppādakkhaṇe anāgataṃ cittaṃ':'Consciousness at the moment of arising and future consciousness','bhaṅgakkhaṇe anāgatañca cittaṃ':'Consciousness at the moment of dissolution and future consciousness','bhaṅgakkhaṇe atītañca cittaṃ':'Consciousness at the moment of dissolution and past consciousness'}
def rest_(s):
    m=re.fullmatch(rf'(na )?({VR}), no ca (?:tesaṃ |tassa )?(?:taṃ )?(?:(?:\w+ )?cittaṃ )?(na )?({VR})\.',s)
    if m:
        n1,v1,n2,v2=m.groups();return f'{VP[v1][1 if n1 else 0]}, but {VP[v2][2 if n2 else 1]}'
    m=re.fullmatch(rf'(na )?({VR}|uppannañ|uppajjamānañ|nirujjhamānañ)(?:ceva| ceva) ({VR}|uppajjamānañca|nirujjhamānañca|uppannañca) ?(?:ca)?\.',s)
    if m:
        n,a,b=m.groups();a=a.replace('ñ','ṃ') if a.endswith('ñ') else a;b=b.replace('ñca','ṃ')
        return f'{VP[a][1]} and {VP[b][0]}' if n else f'both {VP[a][0]} and {VP[b][0]}'
    m=re.fullmatch(rf'na ceva ({VR}) na ca ({VR})\.',s)
    if m:
        x,y=VP[m.group(1)][0],VP[m.group(2)][0]
        return f'is neither {x[3:]} nor {y[3:]}' if x.startswith('is ') and y.startswith('is ') else f'neither {x} nor {y}'
    m=re.fullmatch(r'(.+?), (.+?)\.',s)
    if m:
        def cmp(x):
            x=x.strip();mm=re.fullmatch(rf'({VR})(?: ceva)? ?(na )?({VR})(?: ca)?',x)
            if not mm: raise KeyError(x)
            a,n,b=mm.groups()
            if ' ceva ' in x: return f'both {VP[a][0]} and {VP[b][0]}'
            return f'{VP[a][0]} but {VP[b][1]}' if n else f'{VP[a][0]} and {VP[b][0]}'
        return f'{stm(vlist(m.group(1))) if " ceva " not in m.group(1) else cmp(m.group(1))}, {cmp(m.group(2))}'
    raise KeyError(s)
LEADK=sorted(LEAD,key=len,reverse=True);SUBK=sorted(SUBJ,key=len,reverse=True)
SP={'Āmantā.':'Yes.','Āmantā …pe….':'Yes…','Yassa vā pana…pe…?':'And for whomever…?','No.':'No.','Natthi.':'There is no such case.','Uppajjittha.':'It has arisen.','Nirujjhittha.':'It has ceased.','Nirujjhissati.':'It will cease.','Nirujjhati.':'It does cease.','Uppajjissati.':'It will arise.','Uppajjati.':'It does arise.','Uppannaṃ.':'It is arisen.','(Etena upāyena yāva saraṇaaraṇā uddharitabbā.)':'(In this way the method should be drawn out up to "with conflict" and "without conflict".)','Cittayamakaṃ niṭṭhitaṃ.':'The Pairs on Consciousness are complete.','(14) Atikkantakālavāro':'(14) The Section on Time Having Passed',
'Yassa sarāgaṃ cittaṃ uppajjati…pe… yassa vītarāgaṃ cittaṃ uppajjati… yassa sadosaṃ cittaṃ uppajjati… yassa vītadosaṃ cittaṃ uppajjati… yassa samohaṃ cittaṃ uppajjati… yassa vītamohaṃ cittaṃ uppajjati … yassa saṃkhittaṃ cittaṃ uppajjati… yassa vikkhittaṃ cittaṃ uppajjati… yassa mahaggataṃ cittaṃ uppajjati… yassa amahaggataṃ cittaṃ uppajjati… yassa sauttaraṃ cittaṃ uppajjati… yassa anuttaraṃ cittaṃ uppajjati… yassa samāhitaṃ cittaṃ uppajjati… yassa asamāhitaṃ cittaṃ uppajjati… yassa vimuttaṃ cittaṃ uppajjati… yassa avimuttaṃ cittaṃ uppajjati…?':'For whomever consciousness with lust arises… consciousness without lust… consciousness with hatred… consciousness without hatred… consciousness with delusion… consciousness without delusion… contracted consciousness… scattered consciousness… exalted consciousness… unexalted consciousness… surpassable consciousness… unsurpassable consciousness… concentrated consciousness… unconcentrated consciousness… liberated consciousness… unliberated consciousness arises…?',
'Yassa kusalaṃ cittaṃ uppajjati…pe… yassa akusalaṃ cittaṃ uppajjati… yassa abyākataṃ cittaṃ uppajjati… yassa sukhāya vedanāya sampayuttaṃ cittaṃ uppajjati…?':'For whomever wholesome consciousness arises… unwholesome consciousness… indeterminate consciousness… consciousness associated with pleasant feeling arises…?',
'(Yassa cittake sakabhāvena niddiṭṭhe, yaṃ cittake ca yassa yaṃ cittake ca ekattena niddiṭṭhe.)':'(The part on "for whomever consciousness" is set out in its own form; the part on "whatever consciousness" and the part on "for whomever a given consciousness" are set out as one.)',
'(Mūlayamakaṃ cittayamakaṃ dhammayamakanti tīṇi yamakāni yāva saraṇaaraṇā gacchanti.)':'(The three sets of pairs – the Pairs on Roots, the Pairs on Consciousness and the Pairs on Phenomena – go as far as "with conflict" and "without conflict".)',
'Itaresaṃ sarāgacittassa uppādakkhaṇe tesaṃ…pe….':'For the others, at the moment of arising of consciousness with lust…','Itaresaṃ kusalacittassa uppādakkhaṇe tesaṃ…pe….':'For the others, at the moment of arising of wholesome consciousness…','Yassa akusalaṃ cittaṃ uppajjati na nirujjhati…pe….':'For whomever unwholesome consciousness arises but does not cease…','Yassa abyākataṃ cittaṃ uppajjati na nirujjhati…pe….':'For whomever indeterminate consciousness arises but does not cease…',
'Bhaṅgakkhaṇe cittaṃ uppādakkhaṇaṃ vītakkantaṃ bhaṅgakkhaṇaṃ avītikkantaṃ, atītaṃ cittaṃ uppādakkhaṇañca vītikkantaṃ bhaṅgakkhaṇañca vītikkantaṃ.':'Consciousness at the moment of dissolution has passed the moment of arising but has not passed the moment of dissolution; past consciousness has passed both the moment of arising and the moment of dissolution.',
'Bhaṅgakkhaṇe cittaṃ uppādakkhaṇaṃ vītikkantaṃ bhaṅgakkhaṇaṃ avītikkantaṃ, atītaṃ cittaṃ uppādakkhaṇañca vītikkantaṃ bhaṅgakkhaṇañca vītikkantaṃ.':'Consciousness at the moment of dissolution has passed the moment of arising but has not passed the moment of dissolution; past consciousness has passed both the moment of arising and the moment of dissolution.',
'Bhaṅgakkhaṇe cittaṃ bhaṅgakkhaṇaṃ avītikkantaṃ no ca uppādakkhaṇaṃ avītikkantaṃ, uppādakkhaṇe anāgatañca cittaṃ bhaṅgakkhaṇañca avītikkantaṃ uppādakkhaṇañca avītikkantaṃ.':'Consciousness at the moment of dissolution has not passed the moment of dissolution, but has passed the moment of arising; consciousness at the moment of arising and future consciousness have passed neither the moment of dissolution nor the moment of arising.',
'Namo tassa bhagavato arahato sammāsambuddhassa':'Homage to the Blessed One, the arahant, the Fully Awakened Buddha'}
def sent(s):
    if s in SP: return SP[s]
    l=s[0].lower()+s[1:]
    for k in LEADK:
        if l.startswith(k+' '):
            m=re.match(rf'(?:tesaṃ |tassa )?{ADJR} (.*)',l[len(k)+1:])
            if m: return f'{LEAD[k]}, {ADJ[m.group(1)]} {rest_(m.group(2))}.'
    for k in SUBK:
        if l.startswith(k+' '): return f'{SUBJ[k]} {rest_(l[len(k)+1:])}.'
        if l==k+'.': return SUBJ[k]+'.'
    m=re.fullmatch(r'(bhaṅgakkhaṇe|uppādakkhaṇe) (.+)',l)
    if m:
        wh='At the moment of dissolution' if m.group(1)=='bhaṅgakkhaṇe' else 'At the moment of arising'
        return f'{wh}, it {rest_(m.group(2))}.'
    raise KeyError(s)
HD={'Cittayamakaṃ':'The Pairs on Consciousness',
'(Ka) uddeso':'(a) Outline',
'(Kha) niddeso':'(b) Explanation',
'Suddhacittasāmaññaṃ':'Consciousness in General',
'Suddhacittasāmañña':'Consciousness in General',
'Puggalavāro':'The Section on Persons',
'Dhammavāro':'The Section on Phenomena',
'Puggaladhammavāro':'The Section on Persons and Phenomena',
'Suttantacittamissakaviseso':'Special Case: Mixed with Consciousness in the Suttas',
'Abhidhammacittamissakaviseso':'Special Case: Mixed with Consciousness in the Abhidhamma',
'(1) Uppādanirodhakālasambhedavāro':'(1) Combined Times of Arising and Ending',
'(2) Uppāduppannavāro':'(2) Arising and Arisen',
'(3) Nirodhuppannavāro':'(3) Ending and Arisen',
'(4) Uppādavāro':'(4) Arising',
'(5) Nirodhavāro':'(5) Ending',
'(6) Uppādanirodhavāro':'(6) Arising and Ending',
'(7) Uppajjamāna-nanirodhavāro':'(7) Arising and Not Ending',
'(7) Uppajjamānananirodhavāro':'(7) Arising and Not Ending',
'(8) Uppajjamānuppannavāro':'(8) Arising and Arisen, Present Form',
'(9) Nirujjhamānuppannavāro':'(9) Ceasing and Arisen',
'(10) Uppannuppādavāro':'(10) Arisen and Arising',
'(11) Atītānāgatavāro':'(11) Past and Future',
'(12) Uppannuppajjamānavāro':'(12) Arisen and Arising, Present Form',
'(13) Niruddhanirujjhamānavāro':'(13) Ceased and Ceasing',
'(14) Atikkantakālavāro':'(14) Time Having Passed'}
def tr(b):
    if b in SP: return SP[b]
    return ' '.join(SP[p] if p in SP else (qq(p) if p.endswith('?') else sent(p)) for p in re.split(r'(?<=[.?]) ',b))
if __name__=='__main__':
    f='8-cittayamaka.md';o,bad=run(f,tr,HD);print(f,'unmatched',len(bad))
    for x in bad[:12]: print(x)
    if not bad: write(f,o);check(f)
