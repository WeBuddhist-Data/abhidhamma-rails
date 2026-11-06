"""Rails translation of 1-mulayamaka.md, from the Pāli, using the pi-6 termbase."""
import re,sys
sys.path.insert(0,'pi-6-rails-scripts')
from common import *
X={'kusal':('wholesome','a wholesome'),'akusal':('unwholesome','an unwholesome'),'abyākat':('indeterminate','an indeterminate'),'nām':('mental','a mental')}
XR='(akusal|kusal|abyākat|nām)'
HD={'Mūlayamakaṃ':'The Pairs on Roots','(Ka) uddeso':'(a) Outline','(Kha) niddeso':'(b) Explanation','Mūlavāro':'The Section on Roots','Kusalā dhammā':'Wholesome Phenomena','(1) Mūlanayo':'(1) The Root Method','(2) Mūlamūlanayo':'(2) The Root-of-Roots Method','(3) Mūlakanayo':'(3) The Method Based on a Root','(4) Mūlamūlakanayo':'(4) The Method Based on a Root-of-Roots','Kusalā dhammā (1) mūlanayo':'Wholesome Phenomena: (1) The Root Method','Akusalā dhammā (1) mūlanayo':'Unwholesome Phenomena: (1) The Root Method','Abyākatā dhammā (1) mūlanayo':'Indeterminate Phenomena: (1) The Root Method','Nāmā dhammā (1) mūlanayo':'Mental Phenomena: (1) The Root Method','2-10. Hetuvārādi':'2–10. The Section on Causes and the Others'}
LV='mūlamūlak|mūlamūl|mūlak|mūl'
NL={'mūlamūlak':'mūlamūlaka','mūlamūl':'mūlamūla','mūlak':'mūlaka','mūl':'mūla'}
def plain(x,lv):
    lv=NL.get(lv,lv);a,ar=X[x]
    return {'mūla':f'{a} roots','mūlamūla':f'{a} roots-of-roots','mūlaka':f'based on {ar} root','mūlamūlaka':f'based on {ar} root-of-roots'}[lv]
def eka(x,lv):
    lv=NL.get(lv,lv);r=X[x][1]+' root'
    return {'mūla':f'of one root with {r}','mūlamūla':f'of one root-of-roots with {r}','mūlaka':f'based on one root with {r}','mūlamūlaka':f'based on one root-of-roots with {r}'}[lv]
def mut(x,lv):
    lv=NL.get(lv,lv);r=X[x][1]+' root'
    return {'mūla':f'mutually rooted with {r}','mūlamūla':f'mutually rooted-in-roots with {r}','mūlaka':f'mutually based on a root with {r}','mūlamūlaka':f'mutually based on a root-of-roots with {r}'}[lv]
def eka0(lv): return {'mūl':'of one root','mūlamūl':'of one root-of-roots','mūlak':'based on one root','mūlamūlak':'based on one root-of-roots','mūla':'of one root','mūlamūla':'of one root-of-roots','mūlaka':'based on one root','mūlamūlaka':'based on one root-of-roots'}[lv]
def mut0(lv): return {'mūl':'mutually rooted','mūlamūl':'mutually rooted-in-roots','mūlak':'mutually based on a root','mūlamūlak':'mutually based on a root-of-roots','mūla':'mutually rooted','mūlamūla':'mutually rooted-in-roots','mūlaka':'mutually based on a root','mūlamūlaka':'mutually based on a root-of-roots'}[lv]
def pred(s):
    """Pāli predicate -> English; s like kusalamūlena ekamūlā / kusalamūlā"""
    s=re.sub(r'(ā|a)ti$',lambda m:m.group(1) if m.group(1)=='ā' else 'a',s)
    m=re.fullmatch(rf'{XR}amūlena eka({LV})ā',s)
    if m: return eka(m.group(1),m.group(2))
    m=re.fullmatch(rf'{XR}amūlena aññamañña({LV})ā',s)
    if m: return mut(m.group(1),m.group(2))
    m=re.fullmatch(rf'{XR}a({LV})ā',s)
    if m: return plain(m.group(1),m.group(2))
    raise KeyError('pred '+s)
L={'Ka':'(a) ','Kha':'(b) '}
SYN={'hetū':'causes','hetūti':'causes','nidānā':'sources','sambhavā':'generators','ppabhavā':'beginnings','samuṭṭhānā':'producers','āhārā':'nourishment','ārammaṇā':'objects','paccayā':'conditions','samudayā':'origins'}
SYNR='('+'|'.join(sorted(SYN,key=len,reverse=True))+')'
def syn(tok):
    m=re.fullmatch(rf'{XR}(?:a)?{SYNR}',tok)
    return f'{X[m.group(1)][0]} {SYN[m.group(2)]}'
LIT={'Āmantā.':'Yes.','Mūlavārauddeso.':'The outline of the section on roots.','Mūlavāraniddeso.':'The explanation of the section on roots.','Uddesavāro niṭṭhito.':'The section of outlines is complete.','Niddesavāro niṭṭhito.':'The section of explanations is complete.','Mūlayamakapāḷi niṭṭhitā.':'The Pairs on Roots are complete.','Namo tassa bhagavato arahato sammāsambuddhassa':'Homage to the Blessed One, the arahant, the Fully Awakened Buddha',
'Mūlaṃ hetu nidānañca, sambhavo pabhavena ca;':'Root, cause and source, generator and beginning;','Samuṭṭhānāhārārammaṇā ⟦0⟧, paccayo samudayena cāti.':'Producer, nourishment and object ⟦0⟧, condition and origin.','Samuṭṭhānāhārārammaṇā, paccayo samudayena cāti.':'Producer, nourishment and object, condition and origin.'}
def ans(s):
    if s in LIT: return LIT[s]
    m=re.fullmatch(rf'(Tīṇeva|Naveva) {XR}a(mūlamūl|mūl)āni\. Avasesā \2ā dhammā na \2a\3ā\.',s)
    if m:
        n,x,lv=m.groups();return f'There are only {"three" if n=="Tīṇeva" else "nine"} {plain(x,lv)}. The remaining {X[x][0]} phenomena are not {plain(x,lv)}.'
    m=re.fullmatch(rf'Mūlāni yāni ekato uppajjanti {XR}amūlāni eka({LV})āni ceva aññamañña\2āni ca\. Avasesā \1amūlasahajātā dhammā \1amūlena eka\2ā,? na ca aññamañña\2ā\.',s)
    if m:
        x,lv=m.groups();r=X[x][1]+' root'
        return f'Those {X[x][0]} roots that arise together are both {eka0(lv)} and {mut0(lv)}. The remaining phenomena born together with {r} are {eka(x,lv)}, but are not {mut0(lv)}.'
    m=re.fullmatch(rf'{XR}asamuṭṭhānaṃ rūpaṃ (.+?),? na \1aṃ\. \1aṃ (.+?)ñceva \1añca\.',s,flags=re.I)
    if m:
        x,p1,_=m.groups();x=x.lower();e=X[x][0]
        q=re.sub(r'aṃ$','ā',p1)
        p=pred(q)
        return f'Material form produced by {e} phenomena is {p}, but is not {e}. What is {e} is both {p} and {e}.'
    m=re.fullmatch(rf'Ahetukaṃ {XR}aṃ (?:(\1amūlena) )?na (\S+)aṃ\. Sahetukaṃ \1aṃ (?:\1amūlena )?\S+\.',s)
    if m:
        x,inst,w=m.groups();e=X[x][0]
        p=pred((inst+' ' if inst else '')+w+'ā')
        return f'What is {e} without roots is not {p}. What is {e} with roots is {p}.'
    raise KeyError('ans '+s)
def q(lab,kind,a,b):
    pass
def tr(b):
    if b in LIT: return LIT[b]
    if b=='Ye keci kusalā dhammā, sabbe te kusalahetū…pe… kusalanidānā…pe… kusalasambhavā…pe… kusalappabhavā…pe… kusalasamuṭṭhānā…pe… kusalāhārā…pe… kusalārammaṇā…pe… kusalapaccayā…pe… kusalasamudayā…pe….': pass
    m=re.fullmatch(rf'Ye keci {XR}ā dhammā, sabbe te (.+)',b)
    if m and '…' in b and '?' not in b:
        x=m.group(1);toks=re.split(r'…pe…\.?|…\.?',m.group(2));toks=[t.strip() for t in toks if t.strip()]
        return f'Whatever phenomena are {X[x][0]} – are they all '+'… '.join(syn(t) for t in toks)+'…'
    m=re.fullmatch(rf'Ye keci {XR}ā dhammā, sabbe te {XR}a?hetūti…\?',b)
    if m: return f'Whatever phenomena are {X[m.group(1)][0]} – are they all {X[m.group(2)][0]} causes…?'
    m=re.fullmatch(rf'Tayo eva {XR}ahetū, avasesā \1ā dhammā na \1ahetū…pe… (.+)',b)
    if m:
        x=m.group(1);toks=[t.strip() for t in re.split(r'…\.?',m.group(2)) if t.strip()]
        return f'There are only three {X[x][0]} causes, and the remaining {X[x][0]} phenomena are not {X[x][0]} causes… '+'… '.join(syn(t) for t in toks)+'…'
    m=re.fullmatch(rf'Ye keci {XR}ā dhammā… ye keci {XR}ā dhammā… ye keci {XR}ā dhammā, sabbe te {XR}ahetū ti… (.+)',b)
    if m:
        a,c,d,e,rest=m.groups();toks=[t.strip() for t in re.split(r'…\.?',rest) if t.strip()]
        return f'Whatever phenomena are {X[a][0]}… whatever phenomena are {X[c][0]}… whatever phenomena are {X[d][0]} – are they all {X[e][0]} causes… '+'… '.join(syn(t) for t in toks)+'…'
    # questions
    m=re.fullmatch(r'\((Ka|Kha)\) (.+?)\?(?: (.*))?',b) or re.fullmatch(r'(?:\((Ka|Kha)\) )?(.+?)\?(?: (.*))?',b)
    if m:
        lab,qu,rest=m.groups();la=L.get(lab,'')
        qu=re.sub(r'āti$','ā',qu)
        mm=re.fullmatch(rf'ye keci {XR}ā dhammā, sabbe te (.+)',qu)
        if mm: t=f'Whatever phenomena are {X[mm.group(1)][0]} – are they all {pred(mm.group(2))}?'
        else:
            mm=re.fullmatch(rf'ye keci ({XR}amūlena eka(?:{LV})ā) dhammā, sabbe te (.+)',qu)
            if mm: t=f'Whatever phenomena are {pred(mm.group(1))} – are they all {pred(mm.group(3))}?'
            else:
                mm=re.fullmatch(rf'ye vā pana (.+?), sabbe te dhammā {XR}ā',qu)
                if not mm: raise KeyError('q '+qu)
                t=f'And whatever are {pred(mm.group(1))} – are they all {X[mm.group(2)][0]} phenomena?'
        r=''
        if rest: r=' '+' '.join(ans(x) for x in re.split(r'(?<=\.) (?=Avasesā)|(?<=\.) (?=X)',rest)) if False else ' '+ans(rest)
        return la+t+r
    return ans(b)
if __name__=='__main__':
    f='1-mulayamaka.md'
    o,bad=run(f,tr,HD)
    print('unmatched',len(bad))
    for x in bad[:25]: print(x)
    if not bad:
        write(f,o);check(f)
