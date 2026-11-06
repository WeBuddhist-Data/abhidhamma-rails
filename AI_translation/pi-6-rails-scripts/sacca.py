"""Rails translation of chapter 5 (Pairs on Truths)."""
from general import *
B={'dukkha':'the truth of suffering','samudaya':'the truth of the origin','nirodha':'the truth of the ending','magga':'the truth of the path'}
for k,v in B.items(): C.SUBJ[f'§{k}§']=v
C.N.update({f'§{k}§':v for k,v in B.items()})
C.N.update({'dukkhaṃ':'suffering','samudayo':'origin','nirodho':'ending','maggo':'the path','saccaṃ':'a truth','saccā':'the truths'})
C.SING['saccā']='a truth'
C.ACC.update({'Dukkhaṃ':'dukkhaṃ','Dukkhañca':'dukkhaṃ','Samudayaṃ':'samudayo','Samudayañca':'samudayo','Nirodhaṃ':'nirodho','Nirodhañca':'nirodho','Maggaṃ':'maggo','Maggañca':'maggo'})
C.CEVA.update({'saccañ':'saccaṃ','dukkhañ':'dukkhaṃ','samudayo':'samudayo','nirodho':'nirodho','maggo':'maggo'})
C.OTHER.update({'samudayo':('any other origin','an origin'),'nirodho':('any other ending','an ending'),'maggo':('any other path','a path')})
C.CAT.update({'pl':'saccā','en':'truths','ca':'saccañca'})
C.PLACE['Avasese']='In the remaining'
_pl=C.place
def place(g):
    if g.startswith('Avasese'): return 'In the remaining '+{'catuvokāre pañcavokāre':'four- and five-aggregate existence','pañcavokāre':'five-aggregate existence','catuvokāre':'four-aggregate existence'}[g[8:]]
    return _pl(g)
C.place=place
def sub(b):
    def rp(m):
        w=m.group(0);l=w[0].lower()+w[1:]
        for st in B:
            if l.startswith(st+'sacc'):
                x=l[len(st)+4:]
                if x in('aṃ','anti','a'): return f'§{st}§'
                if x=='añca': return f'§{st}§ ca'
        return w
    return re.sub(r'\b\w+sacc\w*',rp,b)
RAW={'Saccayamakaṃ niṭṭhitaṃ.':'The Pairs on Truths are complete.',
'Cattāri saccāni – dukkhasaccaṃ, samudayasaccaṃ nirodhasaccaṃ, maggasaccaṃ.':'There are four truths – the truth of suffering, the truth of the origin, the truth of the ending, the truth of the path.',
'Kāyikaṃ dukkhaṃ cetasikaṃ dukkhaṃ ṭhapetvā avasesaṃ dukkhasaccaṃ ⟦0⟧, na dukkhaṃ.':'Apart from bodily suffering and mental suffering, the remaining truth of suffering ⟦0⟧ is the truth of suffering, but not suffering.',
'Kāyikaṃ dukkhaṃ cetasikaṃ dukkhaṃ dukkhañceva dukkhasaccañca.':'Bodily suffering and mental suffering are both suffering and the truth of suffering.',
'Kāyikaṃ dukkhaṃ cetasikaṃ dukkhaṃ ṭhapetvā avasesaṃ na dukkhaṃ ⟦0⟧ dukkhasaccaṃ.':'Apart from bodily suffering and mental suffering, the rest is not suffering ⟦0⟧, but it is the truth of suffering.',
'Kāyikaṃ dukkhaṃ cetasikaṃ dukkhaṃ ṭhapetvā avasesaṃ na dukkhaṃ, dukkhasaccaṃ.':'Apart from bodily suffering and mental suffering, the rest is not suffering, but it is the truth of suffering.',
'(Yassakampi yassayatthakampi sadisaṃ vitthāretabbaṃ).':'(The section on persons and the section on person and place should be expanded in the same way.)',
'(Yatthakampi sabbattha sadisaṃ.':'(The section on place is also the same throughout.','Tantinānākaraṇaṃ heṭṭhā yatthakasadisaṃ).':'The differences in wording are like those in the section on place above.)',
'(yatthakā sadisā sabbe).':'(The sections on place are all the same.)','(yatthakampi yassayatthakasadisaṃ kātabbaṃ).':'(The section on place too is to be made like the section on person and place.)',
'(Yatthakaṃ uppādepi nirodhepi uppādanirodhepi sadisaṃ, natthi nānākaraṇaṃ).':'(The section on place is the same in arising, in ending, and in arising and ending; there is no difference.)',
'(Yassayatthakampi sadisaṃ vitthāretabbaṃ).':'(The section on person and place should be expanded in the same way.)',
'(Yassakampi ⟦0⟧ yassayatthakampi sadisaṃ, yassayatthakepi nirodhasamāpannānanti cetaṃ na kātabbaṃ).':'(The section on persons ⟦0⟧ and the section on person and place are the same, but in the section on person and place, "those in the attainment of cessation" is not to be included.)',
'(Yathā uppādavāre atītā pucchā anulomampi paccanīkampi vibhattā evaṃ nirodhepi vibhajitabbā, natthi nānākaraṇaṃ).':'(Just as the question on the past was analysed in the section on arising, both positive and negative, so too it should be analysed in ending; there is no difference.)',
'(Yatthakaṃ uppādavārepi nirodhavārepi uppādanirodhavārepi sadisaṃ natthi nānākaraṇaṃ).':'(The section on place is the same in the sections on arising, on ending, and on arising and ending; there is no difference.)',
'(Yassakampi yassayatthakampi sadisaṃ, yassayatthakepi nirodhasamāpannānanti na kātabbaṃ).':'(The section on persons and the section on person and place are the same, but in the section on person and place, "those in the attainment of cessation" is not to be included.)',
'(Atītā pucchā yathā uppādavāre vibhattā evaṃ uppādanirodhavārepi anulomampi paccanīkampi vibhajitabbaṃ).':'(Just as the question on the past was analysed in the section on arising, so too it should be analysed in the section on arising and ending, both positive and negative.)',
'(Paccuppannaatītā ⟦0⟧ pucchā uppādavārepi uppādanirodhavārepi yassakampi yatthakampi yassayatthakampi anulomampi paccanīkampi sadisaṃ, asammohantena vibhajitabbā).':'(The present-and-past question ⟦0⟧ is the same in the section on arising and in the section on arising and ending – for persons, for places, and for person and place, both positive and negative. It should be analysed without confusion.)',
'(Yathā nirodhavāre atītānāgatā ⟦0⟧ pucchā anulomampi paccanīkampi vibhattā evaṃ uppādanirodhavārepi asammohantena vibhajitabbaṃ).':'(Just as the past-and-future question ⟦0⟧ was analysed in the section on ending, both positive and negative, so too it should be analysed without confusion in the section on arising and ending.)',
'(Yassakampi yassayatthakampi sadisaṃ, samudayasaccaṃ maggasaccaṃ nānākaraṇaṃ, aggamaggassa bhaṅgakkhaṇe, arahantānaṃ asaññasattānaṃ tesaṃ tattha maggasaccañca na nirujjhissati samudayasaccañca nuppajjissati).':'(The section on persons and the section on person and place are the same. The difference concerns the truth of the origin and the truth of the path: at the moment of dissolution of the highest path, for arahants and non-percipient beings, the truth of the path will not cease there, and the truth of the origin will not arise there either.)',
'Samudayaṃ ṭhapetvā…pe… nirodhaṃ ṭhapetvā…pe….':'Apart from the origin… apart from ending…','Nirodhaṃ ṭhapetvā…pe….':'Apart from ending…'}
SLIP=[('parinibbāntānaṃ','parinibbantānaṃ'),('paṭilabhissānti','paṭilabhissanti'),('asaññattā','asaññasattā'),('na nirujjhiti','na nirujjhati')]
HD={'Saccayamakaṃ':'The Pairs on Truths','Suddhasaccavāro':'The Section on the Truths Alone','Suddhasaccamūlacakkavāro':'The Cycle Based on the Truths Alone'}
tr,HDD=build(sub,RAW,None,SLIP,None,HD)
if __name__=='__main__': go(['5-01-saccayamaka.md','5-02-saccayamaka.md','5-03-saccayamaka.md'],tr,HDD)
