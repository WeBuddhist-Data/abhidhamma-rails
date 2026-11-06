"""Rails translation of chapter 2 (Pairs on Aggregates) and the preamble."""
import re,sys
sys.path.insert(0,'pi-6-rails-scripts')
from common import *
import core as C
C.SUBJ.update({'§rūpa§':'the aggregate of form','§vedanā§':'the aggregate of feeling','§saññā§':'the aggregate of perception','§saṅkhāra§':'the aggregate of formations','§viññāṇa§':'the aggregate of consciousness'})
N={'rūpaṃ':('material form',0),'vedanā':('feeling',0),'saññā':('perception',0),'saṅkhārā':('formations',1),'viññāṇaṃ':('consciousness',0),'khandhā':('the aggregates',1),'khandho':('an aggregate',0)}
N.update({k:(v,0) for k,v in C.SUBJ.items()})
HD={'Khandhayamakaṃ':'The Pairs on Aggregates','Paṇṇattivāro':'The Section on Terms','(Ka) uddeso':'(a) Outline','(Kha) niddeso':'(b) Explanation','Padasodhanavāro':'The Section on Clarifying the Terms','(Ka) anulomaṃ':'(a) Positive','(Kha) paccanīkaṃ':'(b) Negative','Padasodhanamūlacakkavāro':'The Cycle Based on Clarifying the Terms','Suddhakhandhavāro':'The Section on the Aggregates Alone','Suddhakhandhamūlacakkavāro':'The Cycle Based on the Aggregates Alone','Paṇṇattivāraniddesa':'Explanation of the Section on Terms','Pavattivāro 1. uppādavāro':'The Section on Occurrence: 1. Arising','Pavatti 2. nirodhavāro':'Occurrence: 2. Ending','(1) Paccuppannavāro':'(1) Present','(2) Atītavāro':'(2) Past','(3) Anāgatavāro':'(3) Future','(4) Paccuppannātītavāro':'(4) Present and Past','(5) Paccuppannānāgatavāro':'(5) Present and Future','(6) Atītānāgatavāro':'(6) Past and Future','Uppādanirodhavāro':'The Section on Arising and Ending','Pariññāvāro':'The Section on Full Understanding','Paccuppannavāro':'Present','Atītavāro':'Past','Anāgatavāro':'Future','Paccuppannātītavāro':'Present and Past','Paccuppannānāgatavāro':'Present and Future','Atītānāgatavāro':'Past and Future','(Ka) anulomapuggalo':'(a) Positive: Person','(Kha) anulomaokāso':'(b) Positive: Place','(Ga) anulomapuggalokāsā':'(c) Positive: Person and Place','(Gha) paccanīkapuggalo':'(d) Negative: Person','(Ṅa) paccanīkaokāso':'(e) Negative: Place','(Ca) paccanīkapuggalokāsā':'(f) Negative: Person and Place','Abhidhammapiṭake':'In the Abhidhamma Piṭaka','Yamakapāḷi':'The Book of Pairs'}
C.LIT.update({
'Piyarūpaṃ sātarūpaṃ rūpaṃ, na §rūpa§.':'Form in the sense of what is dear and pleasant is material form, but not the aggregate of form.',
'§rūpa§ rūpañceva §rūpa§ ca.':'The aggregate of form is both material form and the aggregate of form.',
'Diṭṭhisaññā saññā, na §saññā§.':'Perception in the sense of a view is perception, but not the aggregate of perception.',
'§saññā§ saññā ceva §saññā§ ca.':'The aggregate of perception is both perception and the aggregate of perception.',
'§saṅkhāra§ ṭhapetvā avasesā saṅkhārā, na §saṅkhāra§.':'Apart from the aggregate of formations, the remaining formations are formations, but not the aggregate of formations.',
'§saṅkhāra§ ṭhapetvā avasesā saṅkhārā ⟦0⟧, na §saṅkhāra§.':'Apart from the aggregate of formations, the remaining formations ⟦0⟧ are formations, but not the aggregate of formations.',
'§saṅkhāra§ saṅkhārā ceva §saṅkhāra§ ca.':'The aggregate of formations is both formations and the aggregate of formations.',
'Piyarūpaṃ sātarūpaṃ na §rūpa§, rūpaṃ.':'Form in the sense of what is dear and pleasant is not the aggregate of form, but it is material form.',
'Rūpañca §rūpa§ ca ṭhapetvā avasesā na ceva rūpaṃ na ca §rūpa§.':'Apart from material form and the aggregate of form, the rest are neither material form nor the aggregate of form.',
'Diṭṭhisaññā na §saññā§, saññā.':'Perception in the sense of a view is not the aggregate of perception, but it is perception.',
'Saññañca §saññā§ ca ṭhapetvā avasesā na ceva saññā na ca §saññā§.':'Apart from perception and the aggregate of perception, the rest are neither perception nor the aggregate of perception.',
'§saṅkhāra§ ṭhapetvā avasesā na §saṅkhāra§, saṅkhārā.':'Apart from the aggregate of formations, the remaining formations are not the aggregate of formations, but they are formations.',
'Saṅkhāre ca §saṅkhāra§ ca ṭhapetvā avasesā na ceva saṅkhārā na ca §saṅkhāra§.':'Apart from formations and the aggregate of formations, the rest are neither formations nor the aggregate of formations.',
'Paṇṇattiuddesavāro.':'The outline of the section on terms.','Paṇṇattiniddesavāro.':'The explanation of the section on terms.','Uppādavāro niṭṭhito.':'The section on arising is complete.','Nirodhavāro niṭṭhito.':'The section on ending is complete.','Uppādanirodhavāro niṭṭhito.':'The section on arising and ending is complete.','Pavattivāro niṭṭhito.':'The section on occurrence is complete.',
'Uppajjati.':'It does arise.','Uppajjittha.':'It has arisen.','Uppajjissati.':'It will arise.','Nirujjhati.':'It does cease.','Nirujjhittha.':'It has ceased.','Nirujjhissati.':'It will cease.','Natthi.':'There is no such case.','No.':'No.','Āmantā.':'Yes.',
'Nirodhavāro.':'The section on ending.','Uppādanirodhavāro.':'The section on arising and ending.','Pariññāvāro.':'The section on full understanding.','Khandhayamakapāḷi niṭṭhitā.':'The Pairs on Aggregates are complete.',
'Namo tassa bhagavato arahato sammāsambuddhassa':'Homage to the Blessed One, the arahant, the Fully Awakened Buddha',
'(Yathā uppādavāre paccuppannātītaṃ vibhattaṃ tathā idha vibhajitabbaṃ).':'(This should be analysed here in the same way as the present-and-past section was analysed in the section on arising.)',
'Pañcakkhandhā – §rūpa§, §vedanā§, §saññā§, §saṅkhāra§, §viññāṇa§.':'There are five aggregates – the aggregate of form, the aggregate of feeling, the aggregate of perception, the aggregate of formations, the aggregate of consciousness.',
})
for nom,acc,ca,en,tk in [('rūpaṃ','Rūpaṃ','Rūpañca','material form','§rūpa§'),('vedanā','Vedanaṃ','Vedanañca','feeling','§vedanā§'),('saññā','Saññaṃ','Saññañca','perception','§saññā§'),('viññāṇaṃ','Viññāṇaṃ','Viññāṇañca','consciousness','§viññāṇa§')]:
    C.LIT[f'{acc} ṭhapetvā avasesā khandhā na {nom}, khandhā.']=f'Apart from {en}, the remaining aggregates are not {en}, but they are aggregates.'
    C.LIT[f'{ca} khandhe ca ṭhapetvā avasesā na ceva {nom} na ca khandhā.']=f'Apart from {en} and the aggregates, the rest are neither {en} nor aggregates.'
def hook(s):
    m=re.fullmatch(rf'{C.T} khandho ceva \1 ca\.',s)
    if m: return f'{C.cap(C.e(m.group(1)))} is both an aggregate and {C.e(m.group(1))}.'
    m=re.fullmatch(rf'Avasesā khandhā( ⟦\d+⟧)? na {C.T}\.',s)
    if m: return f'The remaining aggregates{m.group(1) or ""} are not {C.e(m.group(2))}.'
    m=re.fullmatch(rf'Yattha {C.T} {C.VB} \(yatthakaṃ paripuṇṇaṃ kātabbaṃ\)\.',s)
    if m: return f'Wherever {C.stmt(C.e(m.group(1)),m.group(2),False)}… (the section on place should be filled out in full).'
    return None
C.HOOK.append(hook)
STEMS={'rūpakkhandh':'§rūpa§','vedanākkhandh':'§vedanā§','vadanākkhandh':'§vedanā§','saññākkhandh':'§saññā§','saṅkhārakkhandh':'§saṅkhāra§','viññāṇakkhandh':'§viññāṇa§'}
def sub(b):
    def rp(m):
        w=m.group(0);l=w[0].lower()+w[1:]
        for st,t in STEMS.items():
            if l.startswith(st):
                x=l[len(st):]
                if x in('ā','o','aṃ','oti','anti'): return t
                if x=='añca': return t+' ca'
        return w
    return re.sub(r'\b\w+kkhandh\w*',rp,b)
QN=re.compile(r'\((Ka|Kha)\) (na )?(\S+) (?:na )?(\S+?)([?.])(?: (Āmantā\.))?')
def norm(w):
    if w in N: return w
    w2=re.sub(r'nti$','ṃ',w)
    if w2 in N: return w2
    w3=re.sub(r'ti$','',w)
    if w3 in N: return w3
    return w
def tr(b):
    b=sub(b)
    if b in C.LIT: return C.LIT[b]
    m=C.QP.fullmatch(b)
    if m: return C.q_pav(m)
    m=C.QF.fullmatch(b)
    if m: return C.q_f(m)
    m=QN.fullmatch(b)
    if m:
        lab,neg,a,c,_,yes=m.groups();a,c=norm(a),norm(c)
        (ea,pl),(ec,_p)=N[a],N[c]
        if neg and a=='khandhā': ea='an aggregate'
        t=f'Is what is not {ea} not {ec}?' if neg else f'{"Are" if pl else "Is"} {ea} {ec}?'
        return C.LAB[lab]+t+(' Yes.' if yes else '')
    return C.sentences(b)
if __name__=='__main__':
    for f in ('preamble.md','2-01-khandhayamaka.md','2-02-khandhayamaka.md'):
        o,bad=run(f,tr,HD)
        print(f,'unmatched',len(bad))
        for x in bad[:25]: print(' ',x)
        if not bad: write(f,o);check(f)
