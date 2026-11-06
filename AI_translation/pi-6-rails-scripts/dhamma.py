"""Rails translation of chapter 9 (Pairs on Phenomena)."""
from general import *
C.PLURAL[0]=True
B={'kusala':'wholesome phenomena','akusala':'unwholesome phenomena','abyākata':'indeterminate phenomena'}
for k,v in B.items(): C.SUBJ[f'§{k}§']=v
C.N.update({f'§{k}§':v for k,v in B.items()})
C.N.update({'kusalā':'what is wholesome','akusalā':'what is unwholesome','abyākatā':'what is indeterminate','dhammā':'phenomena','dhammo':'a phenomenon'})
C.SING['dhammā']='a phenomenon'
C.NEGCAT[:]=[]
AC={'Kusalaṃ':'kusalā','Kusalañca':'kusalā','Akusalaṃ':'akusalā','Akusalañca':'akusalā','Abyākataṃ':'abyākatā','Abyākatañca':'abyākatā'}
_C={'kusalānaṃ':'wholesome phenomena','akusalānaṃ':'unwholesome phenomena','kusalākusalānaṃ':'wholesome and unwholesome phenomena','abyākatānaṃ':'indeterminate phenomena','kusalavippayuttacittassa':'consciousness not associated with what is wholesome','akusalavippayuttacittassa':'consciousness not associated with what is unwholesome','kusalavippayuttaakusalavippayuttacittassa':'consciousness not associated with what is wholesome or unwholesome','akusalavippayuttakusalavippayuttacittassa':'consciousness not associated with what is unwholesome or wholesome','kusalākusalavippayuttacittassa':'consciousness not associated with what is wholesome or unwholesome'}
C.add_time(_C);C.atoms_sort()
def sub(b):
    for st in ('akusalā','kusalā','abyākatā'):
        for pre in (st,st[0].upper()+st[1:]):
            k=st[:-1]+'a'
            b=b.replace(pre+' ca dhammā',f'§{k}§ ca').replace(pre+' dhammā',f'§{k}§')
    return b
RAW={'Dhammayamakaṃ niṭṭhitaṃ.':'The Pairs on Phenomena are complete.','(Kha) niddeso':'(b) Explanation','(Ca) paccanīkapuggalokāsā':'(f) Negative: Person and Place','(Ga) anulomapuggalokāsā':'(c) Positive: Person and Place','Uppajjanti.':'They do arise.','Nirujjhanti.':'They do cease.','Uppajjittha.':'They have arisen.','Nirujjhittha.':'They have ceased.','Uppajjissanti.':'They will arise.','Nirujjhissanti.':'They will cease.','Bhāvanāvāro.':'The section on cultivation.','Abhidhammapiṭake':'In the Abhidhamma Piṭaka'}
FULL={'(Ka) yo kusalaṃ dhammaṃ bhāveti so akusalaṃ dhammaṃ pajahatīti? Āmantā.':'(a) Whoever cultivates wholesome phenomena – does that person abandon unwholesome phenomena? Yes.','(Kha) yo vā pana akusalaṃ dhammaṃ pajahati so kusalaṃ dhammaṃ bhāvetīti? Āmantā.':'(b) And whoever abandons unwholesome phenomena – does that person cultivate wholesome phenomena? Yes.','(Ka) yo kusalaṃ dhammaṃ na bhāveti so akusalaṃ dhammaṃ nappajahatīti? Āmantā.':'(a) Whoever does not cultivate wholesome phenomena – does that person not abandon unwholesome phenomena? Yes.','(Kha) yo vā pana akusalaṃ dhammaṃ nappajahati so kusalaṃ dhammaṃ na bhāvetīti? Āmantā…pe….':'(b) And whoever does not abandon unwholesome phenomena – does that person not cultivate wholesome phenomena? Yes…','Abhidhammapiṭake':'In the Abhidhamma Piṭaka'}
def hook(s):
    ls=s if s.startswith('§') else s[0].lower()+s[1:]
    m=re.fullmatch(rf'{C.T} dhammā ceva \1(?: ca)?\.',ls)
    if m: a=C.e(m.group(1));return f'{C.cap(a)} are both phenomena and {a}.'
    m=re.fullmatch(rf'Avasesā dhammā( ⟦\d+⟧)? na {C.T}\.',s)
    if m: return f'The remaining phenomena{m.group(1) or ""} are not {C.e(m.group(2))}.'
    m=re.fullmatch(r'(\S+) ṭhapetvā avasesā dhammā na (\S+), dhammā\.',s)
    if m:
        a=C.N[AC[m.group(1)]];return f'Apart from {a}, the remaining phenomena are not {a}, but they are phenomena.'
    m=re.fullmatch(r'(\S+) dhamme ca ṭhapetvā avasesā na ceva (\S+) na ca dhammā\.',s)
    if m:
        a=C.N[AC[m.group(1)]];return f'Apart from {a} and phenomena, the rest are neither {a} nor phenomena.'
    return None
C.HOOK.insert(0,hook)
def pre(b):
    m=re.fullmatch(r'(?:\((Ka|Kha)\) )?(na )?(kusalā|akusalā|abyākatā) (?:na )?dhammā(?:ti)?\?((?: .*)?)',b)
    if m:
        lab,neg,w,rest=m.groups();en=C.N[w]
        t=f'Is what is not {en[8:]} not a phenomenon?' if neg else f'Is {en} a phenomenon?'
        return C.LAB.get(lab,'')+t+(' '+C.sentences(rest.strip()) if rest.strip() else '')
    return None
HD={'Dhammayamakaṃ':'The Pairs on Phenomena','3 Suddhadhammavāro':'3 The Section on Phenomena Alone','Suddhadhammavāro':'The Section on Phenomena Alone','Suddhadhammamūlacakkavāro':'The Cycle Based on Phenomena Alone','4 Suddhadhammamūlacakkavāro':'4 The Cycle Based on Phenomena Alone','Bhāvanāvāro':'The Section on Cultivation'}
tr,HDD=build(sub,RAW,FULL,[('parinibbāntānaṃ','parinibbantānaṃ')],pre,HD)
if __name__=='__main__': go(['9-01-dhammayamaka.md','9-02-dhammayamaka.md','9-03-dhammayamaka.md'],tr,HDD)
