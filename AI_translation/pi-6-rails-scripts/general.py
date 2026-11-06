"""Skeleton shared by chapters built on core.py."""
import re,sys
sys.path.insert(0,'pi-6-rails-scripts')
from common import *
import core as C
BASEHD={'Paṇṇattivāro':'The Section on Terms','Paṇṇattivāra':'The Section on Terms','(Ka) uddeso':'(a) Outline','(Kha) niddeso':'(b) Explanation','Padasodhanavāro':'The Section on Clarifying the Terms','(Ka) anulomaṃ':'(a) Positive','(Kha) paccanīkaṃ':'(b) Negative','Padasodhanamūlacakkavāro':'The Cycle Based on Clarifying the Terms','Paṇṇattivāraniddesa':'Explanation of the Section on Terms','Pavattivāro 1. uppādavāro':'The Section on Occurrence: 1. Arising','Pavatti 2. nirodhavāro':'Occurrence: 2. Ending','Pavatti 3. uppādanirodhavāro':'Occurrence: 3. Arising and Ending','Pavattivāro':'The Section on Occurrence','Uppādavāro':'The Section on Arising','Nirodhavāro':'The Section on Ending','Uppādanirodhavāro':'The Section on Arising and Ending','(1) Paccuppannavāro':'(1) Present','(2) Atītavāro':'(2) Past','(3) Anāgatavāro':'(3) Future','(4) Paccuppannātītavāro':'(4) Present and Past','(5) Paccuppannānāgatavāro':'(5) Present and Future','(6) Atītānāgatavāro':'(6) Past and Future','Pariññāvāro':'The Section on Full Understanding','Paccuppannavāro':'Present','Atītavāro':'Past','Anāgatavāro':'Future','Paccuppannātītavāro':'Present and Past','Paccuppannānāgatavāro':'Present and Future','Atītānāgatavāro':'Past and Future','(Ka) anulomapuggalo':'(a) Positive: Person','(Kha) anulomaokāso':'(b) Positive: Place','(Ga) anulomapuggalokāsā':'(c) Positive: Person and Place','(Gha) paccanīkapuggalo':'(d) Negative: Person','(Ṅa) paccanīkaokāso':'(e) Negative: Place','(Ṅa) paccanīkaokāsā':'(e) Negative: Place','(Ca) paccanīkapuggalokāsā':'(f) Negative: Person and Place'}
RAWBASE={'Uppādavāro.':'The section on arising.','Uppādavāro niṭṭhito.':'The section on arising is complete.','Nirodhavāro niṭṭhito.':'The section on ending is complete.','Nirodhavāro.':'The section on ending.','Uppādanirodhavāro.':'The section on arising and ending.','Uppādanirodhavāro niṭṭhito.':'The section on arising and ending is complete.','Pavattivāro niṭṭhito.':'The section on occurrence is complete.','Pariññāvāro.':'The section on full understanding.','Paṇṇattivāro.':'The section on terms.','Paṇṇattiuddesavāro.':'The outline of the section on terms.','Paṇṇattiniddesavāro.':'The explanation of the section on terms.','Natthi.':'There is no such case.','No.':'No.','Āmantā.':'Yes.','Āmantā.…Pe….':'Yes.…','Natthi.…Pe….':'There is no such case.…','(Saṃkhittaṃ).':'(Abbreviated.)','(Cakkaṃ bandhitabbaṃ)':'(The cycle should be linked up.)','(Cakkaṃ bandhitabbaṃ).':'(The cycle should be linked up.)','…Pe….':'…','(Sadisaṃ )':'(The same.)',
'Uppajjati.':'It does arise.','Uppajjittha.':'It has arisen.','Uppajjissati.':'It will arise.','Nirujjhati.':'It does cease.','Nirujjhittha.':'It has ceased.','Nirujjhissati.':'It will cease.',
'(Yassakampi yassayatthakampi sadisaṃ).':'(The section on persons and the section on person and place are also the same.)','(yassakampi yassayatthakampi sadisaṃ).':'(The section on persons and the section on person and place are also the same.)','(Yassakampi yassayatthakampi sadisaṃ.)':'(The section on persons and the section on person and place are also the same.)'}
def build(sub,RAW=None,FULLRAW=None,SLIP=(),pre=None,HD=None):
    for k,v in {**RAWBASE,**(RAW or {})}.items(): C.LIT[sub(k)]=v
    FR=FULLRAW or {}
    C.FULL.update({sub(k):v for k,v in FR.items()})
    def tr(b):
        if b in FR: return FR[b]
        if pre:
            r=pre(b)
            if r is not None: return r
        for x,y in SLIP: b=b.replace(x,y)
        b=re.sub(r'(No|Āmantā) …pe…',r'\1…pe…',b)
        b=re.sub(r'(?<=\S) …pe…','…pe…',b)
        b=b.replace('…pe…. Āmantā','…pe…? Āmantā').replace('na uppajj','nuppajj').replace('nuppajjissanti','nuppajjissati') if not C.PLURAL[0] else b.replace('…pe…. Āmantā','…pe…? Āmantā').replace('na uppajj','nuppajj')
        if re.match(r'\(K\w+\) y.*(āti|īti)\.$',b): b=b[:-1]+'?'
        b2=sub(b)
        if b2 in C.FULL: return C.FULL[b2]
        if b2 in C.LIT: return C.LIT[b2]
        ps=re.split(r'(?<=\.) (?=(?:Yassa|Yattha|Yo|Saccā|Na saccā) )',b2)
        if len(ps)>1 and any('?' in x for x in ps): return ' '.join(C.piece(x) for x in ps)
        return C.piece(b2)
    return tr,{**BASEHD,**(HD or {})}
def go(fs,tr,HD,show=30):
    S={}
    for f in fs:
        o,bad=run(f,tr,HD);print(f,'unmatched',len(bad))
        src=open(PALI+f,encoding='utf-8').read().split('\n')
        for ln,e,_ in bad:
            k=re.sub(r'§\w+§','F',e)[:40]
            S.setdefault(k,[0,f[:5],ln,e[:80],src[ln-1][:190]])[0]+=1
        if not bad: write(f,o);check(f)
    for k,v in sorted(S.items(),key=lambda x:-x[1][0])[:show]: print(v)
