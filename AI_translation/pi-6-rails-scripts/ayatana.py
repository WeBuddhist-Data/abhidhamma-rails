"""Rails translation of chapter 3 (Pairs on Bases)."""
import re,sys
sys.path.insert(0,'pi-6-rails-scripts')
from common import *
import core as C
B={'cakkh':'the eye base','sot':'the ear base','ghān':'the nose base','jivh':'the tongue base','kāy':'the body base','rūp':'the visible-form base','sadd':'the sound base','gandh':'the scent base','ras':'the taste base','phoṭṭhabb':'the tangible base','man':'the mind base','dhamm':'the mind-object base'}
STEM={'cakkhāyatan':'cakkh','sotāyatan':'sot','ghānāyatan':'ghān','jivhāyatan':'jivh','kāyāyatan':'kāy','rūpāyatan':'rūp','saddāyatan':'sadd','gandhāyatan':'gandh','rasāyatan':'ras','phoṭṭhabbāyatan':'phoṭṭhabb','manāyatan':'man','dhammāyatan':'dhamm'}
for k,v in B.items(): C.SUBJ[f'§{k}§']=v
C.N.update({f'§{k}§':v for k,v in B.items()})
C.N.update({'cakkhu':'the eye','sotaṃ':'the ear','ghānaṃ':'the nose','jivhā':'the tongue','kāyo':'the body','rūpaṃ':'material form','saddo':'sound','gandho':'scent','raso':'taste','phoṭṭhabbo':'the tangible','mano':'the mind','dhammo':'a phenomenon','āyatanaṃ':'a base','āyatanā':'the bases'})
C.SING['āyatanā']='a base';C.SING['āyatanaṃ']='a base'
C.NEGCAT[:]=[('nāyatanā','āyatanā'),('nāyatana','āyatana')]
C.ACC.update({'Cakkhuṃ':'cakkhu','Cakkhuñca':'cakkhu','Sotaṃ':'sotaṃ','Sotañca':'sotaṃ','Manaṃ':'mano','Manañca':'mano','Kāyañca':'kāyo','Rūpañca':'rūpaṃ','Gandhañca':'gandho','Rasañca':'raso','Dhammañca':'dhammo'})
C.CEVA.update({'cakkhu':'cakkhu','sotañ':'sotaṃ','kāyo':'kāyo','rūpañ':'rūpaṃ','gandho':'gandho','raso':'raso','dhammo':'dhammo','āyatanañ':'āyatanaṃ'})
C.OTHER.update({'kāyo':('any other body','a body'),'rūpaṃ':('any other material form','material form'),'dhammo':('any other phenomenon','a phenomenon')})
C.SPEC.update({'Dibbacakkhu paññācakkhu':('The divine eye and the eye of wisdom','eyes'),'Dibbasotaṃ taṇhāsotaṃ':('The divine ear and the stream of craving','"ear" (sota)'),'Sīlagandho samādhigandho paññāgandho':('The scent of virtue, the scent of concentration and the scent of wisdom','scents'),'Attharaso dhammaraso vimuttiraso':('The taste of meaning, the taste of the Dhamma and the taste of liberation','tastes')})
C.CAT.update({'pl':'āyatanā','en':'bases','ca':'āyatanañca'})
HD={'Āyatanayamakaṃ':'The Pairs on Bases','Paṇṇattivāro':'The Section on Terms','(Ka) uddeso':'(a) Outline','(Kha) niddeso':'(b) Explanation','Padasodhanavāro':'The Section on Clarifying the Terms','(Ka) anulomaṃ':'(a) Positive','(Kha) paccanīkaṃ':'(b) Negative','Padasodhanamūlacakkavāro':'The Cycle Based on Clarifying the Terms','Suddhāyatanavāro':'The Section on the Bases Alone','Suddhāyatanamūlacakkavāro':'The Cycle Based on the Bases Alone','Paṇṇattivāraniddesa':'Explanation of the Section on Terms','Pavattivāro 1. uppādavāro':'The Section on Occurrence: 1. Arising','Pavatti 2. nirodhavāro':'Occurrence: 2. Ending','Pavatti 3. uppādanirodhavāro':'Occurrence: 3. Arising and Ending','(1) Paccuppannavāro':'(1) Present','(2) Atītavāro':'(2) Past','(3) Anāgatavāro':'(3) Future','(4) Paccuppannātītavāro':'(4) Present and Past','(5) Paccuppannānāgatavāro':'(5) Present and Future','(6) Atītānāgatavāro':'(6) Past and Future','Pariññāvāro':'The Section on Full Understanding','Paccuppannavāro':'Present','Atītavāro':'Past','Anāgatavāro':'Future','Paccuppannātītavāro':'Present and Past','Paccuppannānāgatavāro':'Present and Future','Atītānāgatavāro':'Past and Future','(Ka) anulomapuggalo':'(a) Positive: Person','(Kha) anulomaokāso':'(b) Positive: Place','(Ga) anulomapuggalokāsā':'(c) Positive: Person and Place','(Gha) paccanīkapuggalo':'(d) Negative: Person','(Ṅa) paccanīkaokāso':'(e) Negative: Place','(Ca) paccanīkapuggalokāsā':'(f) Negative: Person and Place'}
def sub(b):
    def rp(m):
        w=m.group(0);l=w[0].lower()+w[1:]
        for st,k in STEM.items():
            if l.startswith(st):
                x=l[len(st):]
                if x in('aṃ','anti','a',''): return f'§{k}§'
                if x=='añca': return f'§{k}§ ca'
                if x=='amūlakaṃ': return f'§{k}§mūlakaṃ'
        return w
    return re.sub(r'\b\w*āyatan\w*',rp,b)
RAW={
'Uppādavāro.':'The section on arising.','Āyatanayamakaṃ niṭṭhitaṃ.':'The Pairs on Bases are complete.','Paṇṇattiuddesavāro.':'The outline of the section on terms.','Paṇṇattiniddesavāro.':'The explanation of the section on terms.','Uppādavāro niṭṭhito.':'The section on arising is complete.','Nirodhavāro niṭṭhito.':'The section on ending is complete.','Nirodhavāro.':'The section on ending.','Uppādanirodhavāro.':'The section on arising and ending.','Uppādanirodhavāro niṭṭhito.':'The section on arising and ending is complete.','Pavattivāro niṭṭhito.':'The section on occurrence is complete.','Pariññāvāro.':'The section on full understanding.',
'Uppajjati.':'It does arise.','Uppajjittha.':'It has arisen.','Uppajjissati.':'It will arise.','Nirujjhati.':'It does cease.','Nirujjhittha.':'It has ceased.','Nirujjhissati.':'It will cease.','Natthi.':'There is no such case.','No.':'No.','Āmantā.':'Yes.','Āmantā.…Pe….':'Yes.…','Natthi.…Pe….':'There is no such case.…','(Saṃkhittaṃ).':'(Abbreviated.)',
'(Cakkaṃ bandhitabbaṃ)':'(The cycle should be linked up.)','(Ekekapadamūlakaṃ cakkaṃ bandhitabbaṃ asammohantena).':'(The cycle based on each single term should be linked up without confusion.)','(Cakkaṃ bandhantena sabbattha āmantāti kātabbaṃ).':'(When linking up the cycle, the answer "Yes" is to be given throughout.)',
'Dvādasāyatanāni – cakkhāyatanaṃ, sotāyatanaṃ ghānāyatanaṃ, jivhāyatanaṃ, kāyāyatanaṃ, rūpāyatanaṃ, saddāyatanaṃ, gandhāyatanaṃ, rasāyatanaṃ, phoṭṭhabbāyatanaṃ, manāyatanaṃ, dhammāyatanaṃ.':'There are twelve bases – the eye base, the ear base, the nose base, the tongue base, the body base, the visible-form base, the sound base, the scent base, the taste base, the tangible base, the mind base, the mind-object base.',
'(uppādepi nirodhepi uppādanirodhepi yatthakaṃ sabbattha sadisaṃ).':'(The section on place is the same throughout – in arising, in ending, and in arising and ending.)',
'(Uppādavārepi nirodhavārepi uppādanirodhavārepi atītā pucchā anulomampi paccanīkampi ⟦0⟧ sadisaṃ.)':'(In the sections on arising, on ending, and on arising and ending, the question on the past is the same, both positive and negative ⟦0⟧.)',
'(Yathā uppādavāre yassa yatthake anāgatā pucchā vitthāritā, evaṃ nirodhepi vitthāretabbā).':'(Just as the question on the future was expanded for person and place in the section on arising, so too it should be expanded in ending.)',
'(yathā paccuppannātītepi tividhaṃ vitthāritaṃ evaṃ idampi vitthāretabbaṃ).':'(Just as the present-and-past section was expanded in three ways, this too should be expanded.)',
'(yatthakaṃ noti na kātabbaṃ, yatthakaṃ itaresaṃ yatthakānaṃ sadisaṃ kātabbaṃ, yatthakaṃ tīsupi vāresu sadisaṃ).':'(In the section on place, "No" is not to be used. The section on place is to be made the same as the other sections on place, and it is the same in all three sections.)',
'(Yassakampi yassayatthakampi sadisaṃ).':'(The section on persons and the section on person and place are also the same.)',
'(Atītā pucchā uppādepi nirodhepi uppādanirodhepi anulomampi paccanīkampi sadisaṃ).':'(The question on the past is the same in arising, in ending, and in arising and ending, both positive and negative.)',
'(Yathā uppādavāre paccuppannātītā pucchā vibhattā evaṃ uppādanirodhepi paccuppannātītā pucchā anulomampi paccanīkampi vibhajitabbā ⟦0⟧ ).':'(Just as the present-and-past question was analysed in the section on arising, so too the present-and-past question should be analysed in arising and ending, both positive and negative ⟦0⟧.)',
'(Yathā nirodhavāre atītānāgatā ⟦0⟧ pucchā yassakampi yatthakampi yassayatthakampi anulomampi paccanīkampi vibhattaṃ, evaṃ uppādanirodhepi atītānāgatā pucchā vibhajitabbā.)':'(Just as the past-and-future ⟦0⟧ question was analysed in the section on ending – for persons, for places, and for person and place, both positive and negative – so too the past-and-future question should be analysed in arising and ending.)',
}
for k,v in RAW.items(): C.LIT[sub(k)]=v
FULLRAW={
'Āyatanā ghānāyatananti…pe… āyatanā dhammāyatananti?':'Are the bases the nose base?… are the bases the mind-object base?',
'Sotaṃ sotāyatananti?…Pe… avasesā āyatanā na dhammāyatanaṃ…pe….':'Is the ear the ear base?… the remaining bases are not the mind-object base…',
'Āyatanā sotāyatananti…pe… āyatanā manāyatananti?':'Are the bases the ear base?… are the bases the mind base?',
'Nāyatanā na cakkhāyatanaṃ…pe… nāyatanā na dhammāyatananti? Āmantā.':'Is what is not a base not the eye base?… is what is not a base not the mind-object base? Yes.',
'Na ghānaṃ na ghānāyatanaṃ…pe… nāyatanā na dhammāyatananti?':'Is what is not the nose not the nose base?… is what is not a base not the mind-object base?',
'Nāyatanā na sotāyatanaṃ…pe… nāyatanā na manāyatananti? Āmantā.':'Is what is not a base not the ear base?… is what is not a base not the mind base? Yes.',
'Āmantā.…Pe… ghānaṃ… jivhā… kāyo… rūpaṃ… saddo… gandho… raso… phoṭṭhabbo… mano… dhammo āyatananti?':'Yes.… the nose… the tongue… the body… material form… sound… scent… taste… the tangible… the mind… is a phenomenon a base?',
'Sotaṃ ṭhapetvā…pe… ghānaṃ ṭhapetvā…pe… jivhaṃ ṭhapetvā…pe… na ca āyatanā.':'Apart from the ear… apart from the nose… apart from the tongue… nor bases.',
'Rūpaṃ ṭhapetvā…pe… saddaṃ ṭhapetvā…pe… gandhaṃ ṭhapetvā…pe… rasaṃ ṭhapetvā…pe… phoṭṭhabbaṃ ṭhapetvā…pe… na ca āyatanā. Nāyatanā na phoṭṭhabbāyatananti? Āmantā.':'Apart from material form… apart from sound… apart from scent… apart from taste… apart from the tangible… nor bases. Is what is not a base not the tangible base? Yes.',
'Āyatanā ghānāyatanaṃ…pe… āyatanā dhammāyatananti?':'Are the bases the nose base?… are the bases the mind-object base?',
'Āyatanā cakkhāyatananti?…Pe… na cakkhāyatanaṃ…pe…. Āyatanā dhammāyatananti?…Pe… na dhammāyatanaṃ.':'Are the bases the eye base?… are not the eye base… Are the bases the mind-object base?… are not the mind-object base.',
'Āyatanā cakkhāyatananti?…Pe… āyatanā dhammāyatananti? …Pe… na dhammāyatanaṃ…pe….':'Are the bases the eye base?… are the bases the mind-object base? … are not the mind-object base…',
'Āyatanā cakkhāyatanaṃ…pe… āyatanā manāyatananti?':'Are the bases the eye base?… are the bases the mind base?',
'Cakkhuṃ ṭhapetvā avasesā āyatanā na cakkhu, āyatanā. Cakkhuñca āyatanañca ṭhapetvā avasesā na ceva cakkhu na ca āyatanā….':'Apart from the eye, the remaining bases are not the eye, but they are bases. Apart from the eye and the bases, the rest are neither the eye nor bases…',
'Nāyatanā na ghānāyatanaṃ…pe… nāyatanā na dhammāyatananti?':'Is what is not a base not the nose base?… is what is not a base not the mind-object base?',
'Sotaṃ ṭhapetvā…pe… ghānaṃ ṭhapetvā…pe… jivhaṃ ṭhapetvā…pe… na ca āyatanā. Nāyatanā na dhammāyatananti? Āmantā.':'Apart from the ear… apart from the nose… apart from the tongue… nor bases. Is what is not a base not the mind-object base? Yes.',
'Nāyatanā na cakkhāyatananti? Āmantā.…Pe…. Nāyatanā na dhammāyatananti? Āmantā.…Pe….':'Is what is not a base not the eye base? Yes.… Is what is not a base not the mind-object base? Yes.…',
'Yassa cakkhāyatanaṃ uppajjittha tassa ghānāyatanaṃ…pe… rūpāyatanaṃ… manāyatanaṃ… dhammāyatanaṃ uppajjitthāti? Āmantā.':'For whomever the eye base has arisen, has the nose base… the visible-form base… the mind base… the mind-object base arisen for them? Yes.',
'Yassa ghānāyatanaṃ…pe… rūpāyatanaṃ… manāyatanaṃ uppajjittha tassa dhammāyatanaṃ uppajjitthāti? Āmantā.':'For whomever the nose base… the visible-form base… the mind base has arisen, has the mind-object base arisen for them? Yes.',
'(Ka) yattha cakkhāyatanaṃ uppajjittha…pe… (yatthakaṃ paccuppannepi atītepi anāgatepi paccuppannātītepi paccuppannānāgatepi atītānāgatepi sabbattha sadisaṃ, uppajjati uppajjitthāti nāmaṃ atirekaṃ kātabbaṃ).':'(a) Wherever the eye base has arisen… (The section on place is the same throughout – in the present, the past, the future, the present and past, the present and future, and the past and future. Only the extra wording, such as "arises" or "has arisen", is to be added.)',
'(Yattha ghānāyatanaṃ uppajjati tattha manāyatanaṃ dhammāyatanañca ekasadisaṃ, nānaṃ natthi, upari pana vārasaṅkhepo ⟦0⟧ tīti jānitabbaṃ.)':'(Wherever the nose base arises, the mind base and the mind-object base are treated alike; there is no difference. It should be understood, however, that the sections further on are abbreviated ⟦0⟧.)',
'Yassa cakkhāyatanaṃ uppajjissati (tassa manāyatanañca dhammāyatanañca sadisaṃ, ime dve sadisāyeva honti).':'For whomever the eye base will arise (the mind base and the mind-object base are treated alike for them; these two are just the same).',
'Yassa yattha cakkhāyatanaṃ nirujjhati tassa tattha sotāyatanaṃ nirujjhatīti…pe… ghānāyatanaṃ… rūpāyatanaṃ… manāyatanaṃ… dhammāyatanaṃ nirujjhatīti? (Yassa yatthakampi sadisaṃ vitthāretabbaṃ).':'For whomever and wherever the eye base ceases, does the ear base… the nose base… the visible-form base… the mind base… the mind-object base cease for them there? (The section on person and place should be expanded in the same way.)',
'Yassa yattha cakkhāyatanaṃ na nirujjhati tassa tattha sotāyatanaṃ na nirujjhatī ti…pe… (yassa yatthakampi yassakasadisaṃ).':'For whomever and wherever the eye base does not cease, does the ear base not cease for them there?… (The section on person and place is the same as the section on persons.)',
'Asaññasattaṃ upapajjantānaṃ tesaṃ tattha rūpāyatanaṃ uppajjati, no ca tesaṃ tattha…pe… pañcavokāraṃ upapajjantānaṃ tesaṃ tattha…pe….':'For those being reborn as non-percipient beings, the visible-form base arises there, but not… for those being reborn in five-aggregate existence…',
}
C.FULL.update({sub(k):v for k,v in FULLRAW.items()});C.FULL.update(FULLRAW)
SLIP=[('uppajjittharūpāyatanañca','uppajjittha rūpāyatanañca'),('rūpāyatanañca ca uppajjittha','rūpāyatanañca uppajjittha'),('parinibbāntānaṃ','parinibbantānaṃ'),('ghānāyatanaṃ upapajjissati','ghānāyatanaṃ uppajjissati'),(', parinibbantānaṃ asaññasattānaṃ','. Parinibbantānaṃ asaññasattānaṃ'),(' tasaṃ tattha',' tesaṃ tattha'),('yassa =93 yattha','yassa yattha'),('manāyatana…pe…','manāyatanaṃ…pe…'),('sotāyananti','sotāyatananti'),('dhammāyatanaṃ nuppajjissati.','dhammāyatanaṃ nuppajjissati.')]
C.N['cakkhūti']='the eye'
TAIL=re.compile(r'(.*) \(saṃkhittaṃ yassakasadisaṃ ⟦0⟧ \)\.')
def tr(b):
    if b in FULLRAW: return FULLRAW[b]
    for x,y in SLIP: b=b.replace(x,y)
    b=re.sub(r'(No|Āmantā) …pe…',r'\1…pe…',b)
    m=TAIL.fullmatch(b);tail=''
    if m: b=m.group(1)+'.';tail=' (Abbreviated: the same as the section on persons ⟦0⟧.)'
    b2=sub(b)
    if b2 in C.FULL: return C.FULL[b2]
    if b2 in C.LIT: return C.LIT[b2]
    ps=re.split(r'(?<=\.) (?=(?:Yassa|Yattha) )',b2)
    if len(ps)>1 and any('?' in x for x in ps): return ' '.join(C.piece(x) for x in ps)
    return C.piece(b2)+tail
if __name__=='__main__':
    fs=[f'3-0{i}-ayatanayamaka.md' for i in range(1,7)];C_={}
    for f in fs:
        o,bad=run(f,tr,HD)
        print(f,'unmatched',len(bad))
        for ln,e,body in bad:
            k=re.sub(r'§\w+§','F',e)[:40]
            C_.setdefault(k,[0,f[:4],ln,e[:70],body[:170]])[0]+=1
        if not bad: write(f,o);check(f)
    for k,v in sorted(C_.items(),key=lambda x:-x[1][0])[:30]: print(v)
