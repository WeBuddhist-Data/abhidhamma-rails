"""Rails translation of chapter 6 (Pairs on Formations)."""
from general import *
B={'kāya':'the bodily formation','vacī':'the verbal formation','citta':'the mental formation'}
for k,v in B.items(): C.SUBJ[f'§{k}§']=v
C.N.update({f'§{k}§':v for k,v in B.items()})
C.N.update({'kāyo':'the body','vacī':'speech','cittaṃ':'consciousness','saṅkhārā':'the formations','saṅkhāro':'a formation'})
C.SING['saṅkhārā']='a formation'
C.ACC.update({'Kāyañca':'kāyo','Vaciñca':'vacī','Cittañca':'cittaṃ'})
C.CEVA.update({'saṅkhāro':'saṅkhāro'})
C.CAT.update({'pl':'saṅkhārā','en':'formations','ca':'saṅkhāre ca'})
def sub(b):
    def rp(m):
        w=m.group(0);l=w[0].lower()+w[1:]
        for st in B:
            if l.startswith(st+'saṅkhār'):
                x=l[len(st)+7:]
                if x in('o','aṃ','anti','oti','a'): return f'§{st}§'
                if x=='añca': return f'§{st}§ ca'
        return w
    b=re.sub(r'\b\w+saṅkhār\w*(?: ca\b)?',lambda m:(rp(re.match(r'\S+',m.group(0)))+(' ca' if m.group(0).endswith(' ca') else '')),b)
    return b
_C={'assāsapassāsānaṃ':'in-and-out breathing','vitakkavicārānaṃ':'thought and holding the thought','vinā vitakkavicārehi assāsapassāsānaṃ':'in-and-out breathing without thought and holding the thought','vinā assāsapassāsehi vitakkavicārānaṃ':'thought and holding the thought without in-and-out breathing','vinā assāsapassāsehi cittassa':'consciousness without in-and-out breathing','vinā vitakkavicārehi cittassa':'consciousness without thought and holding the thought','vinā assāsapassāsehi avitakkaavicāracittassa':'consciousness without in-and-out breathing and without thought and holding the thought','avitakkaavicāracittassa':'consciousness without thought and holding the thought','savitakkasavicārapacchimacittassa':'the final consciousness with thought and holding the thought','avitakkaavicārapacchimacittassa':'the final consciousness without thought and holding the thought','kāmāvacarānaṃ pacchimacittassa':'the final consciousness of those in the sense sphere'}
for k,v in _C.items():
    C.ATOMS.append((k+' uppādakkhaṇe','@at the moment of arising of '+v));C.ATOMS.append((k+' bhaṅgakkhaṇe','@at the moment of dissolution of '+v))
C.ATOMS.extend([('kāmāvacare','@in the sense sphere'),('rūpāvacare','@in the fine-material sphere'),('arūpāvacare','@in the formless sphere'),('rūpāvacare arūpāvacare','@in the fine-material and formless spheres'),('savitakkasavicārabhūmiyaṃ','@in a plane with thought and holding the thought'),('avitakkaavicārabhūmiyaṃ','@in a plane without thought and holding the thought')])
for ks,x in [(('paṭhamajjhānaṃ',),'the first jhāna'),(('dutiyajjhānaṃ',),'the second jhāna'),(('tatiyajjhānaṃ',),'the third jhāna'),(('catutthajjhānaṃ',),'the fourth jhāna'),(('dutiyajjhānaṃ','tatiyajjhānaṃ'),'the second or third jhāna'),(('paṭhamajjhānaṃ','dutiyajjhānaṃ','tatiyajjhānaṃ'),'the first, second or third jhāna'),(('dutiyajjhānaṃ','tatiyajjhānaṃ','catutthajjhānaṃ'),'the second, third or fourth jhāna'),(('paṭhamajjhānaṃ','dutiyajjhānaṃ'),'the first or second jhāna'),(('tatiyajjhānaṃ','catutthajjhānaṃ'),'the third or fourth jhāna')]:
    C.ATOMS.append((' '.join(ks)+' samāpannānaṃ','those attaining '+x))
C.ATOMS.extend([('itaresaṃ kāmāvacarānaṃ','the others in the sense sphere'),('itaresaṃ','the others'),('tesaṃyeva','those same beings'),('yassa cittassa anantarā kāmāvacarānaṃ pacchimacittaṃ uppajjissati','those in the sense sphere whose final consciousness will arise immediately after a given consciousness'),('yassa cittassa anantarā avitakkaavicāraṃ pacchimacittaṃ uppajjissati','those whose final consciousness without thought and holding the thought will arise immediately after a given consciousness'),('yassa cittassa anantarā savitakkasavicāraṃ pacchimacittaṃ uppajjissati','those whose final consciousness with thought and holding the thought will arise immediately after a given consciousness'),('avitakkaavicārapacchimacittasamaṅgīnaṃ','those possessing the final consciousness without thought and holding the thought'),('savitakkasavicārapacchimacittasamaṅgīnaṃ','those possessing the final consciousness with thought and holding the thought'),('kāmāvacarānaṃ pacchimacittasamaṅgīnaṃ','those in the sense sphere possessing the final consciousness'),('dutiyajjhāne tatiyajjhāne','@in the second and third jhāna')])
C.atoms_sort()
C.PLACE.update({'Paṭhamajjhāne':'In the first jhāna','Dutiyajjhāne':'In the second jhāna','Tatiyajjhāne':'In the third jhāna','Catutthajjhāne':'In the fourth jhāna','Savitakkasavicārabhūmiyaṃ':'In a plane with thought and holding the thought','Avitakkaavicārabhūmiyaṃ':'In a plane without thought and holding the thought'})
RAW={'Saṅkhārayamakaṃ niṭṭhitaṃ.':'The Pairs on Formations are complete.','(Kha) paccanīkaṃ':'(b) Negative','4 (Ṅa) paccanīkaokāso':'4 (e) Negative: Place',
'(Yassakampi yassayatthakampi sadisaṃ vitthāretabbaṃ, yassayatthake nirodhasamāpannānanti na labbhati.)':'(The section on persons and the section on person and place should be expanded in the same way; in the section on person and place, "those in the attainment of cessation" does not apply.)',
'(Yassakampi yassayatthakampi sadisaṃ, yassayatthake nirodhasamāpannānanti na labbhati).':'(The section on persons and the section on person and place are the same; in the section on person and place, "those in the attainment of cessation" does not apply.)',
'(Yatthakampi sabbattha ekasadisaṃ).':'(The section on place too is alike throughout.)','(itaresaṃ yatthakānaṃ sadisaṃ).':'(It is the same as the other sections on place.)',
'(Atītā pucchā uppādavārepi nirodhavārepi uppādanirodhavārepi sadisaṃ vitthāretabbā).':'(The question on the past should be expanded in the same way in the sections on arising, on ending, and on arising and ending.)',
'(Yathā uppādavāre paccuppannātītā pucchā anulomampi paccanīkampi vibhattā evaṃ uppādavāranirodhavārepi paccuppannātītā pucchā anulomampi paccanīkampi vibhajitabbā.)':'(Just as the present-and-past question was analysed in the section on arising, both positive and negative, so too it should be analysed in the section on arising and ending, both positive and negative.)',
'(Yathā nirodhavāre atītānāgatā pucchā anulomampi paccanīkampi evaṃ uppādanirodhavārepi atītānāgatā pucchā anulomampi paccanīkampi vibhajitabbaṃ asammohantena nirodhavārena sadisaṃ, natthi nānākaraṇaṃ.)':'(Just as the past-and-future question was analysed in the section on ending, both positive and negative, so too it should be analysed without confusion in the section on arising and ending, in the same way as the section on ending; there is no difference.)',
'(Yathā khandhayamake pariññāvāraṃ vibhattaṃ evaṃ saṅkhārayamakepi pariññāvāraṃ vibhajitabbaṃ.)':'(Just as the section on full understanding was analysed in the Pairs on Aggregates, so too it should be analysed in the Pairs on Formations.)',
'(Yassakampi yassayatthakampi sadisaṃ vitthāretabbaṃ, yassayatthake nirodhasamāpannānanti na kātabbaṃ.)':'(The section on persons and the section on person and place should be expanded in the same way; in the section on person and place, "those in the attainment of cessation" is not to be included.)',
'(Yathā uppādavāre atītā pucchā yassakampi yassayatthakampi anulomampi paccanīkampi vibhattaṃ evaṃ nirodhavārepi vibhajitabbaṃ, natthi nānākaraṇaṃ.)':'(Just as the question on the past was analysed in the section on arising – for persons and for person and place, both positive and negative – so too it should be analysed in the section on ending; there is no difference.)'}
FULL={'Tayo saṅkhārā – kāyasaṅkhāro, vacīsaṅkhāro, cittasaṅkhāroti. Assāsapassāsā kāyasaṅkhāro, vitakkavicārā vacīsaṅkhāro, saññā ca vedanā ca cittasaṅkhāro. Ṭhapetvā vitakkavicāre sabbepi cittasampayuttakā dhammā cittasaṅkhāro.':'There are three formations – the bodily formation, the verbal formation, the mental formation. In-and-out breathing is the bodily formation; thought and holding the thought are the verbal formation; perception and feeling are the mental formation. Apart from thought and holding the thought, all phenomena associated with consciousness are the mental formation.'}
def hook(s):
    ls=s if s.startswith('§') else s[0].lower()+s[1:]
    m=re.fullmatch(r'(\S+) na (\S+), \1\.',ls)
    if m and m.group(1) in C.N and m.group(2) in C.N:
        a=C.N[m.group(1)];return f'{C.cap(a)} is not {C.N[m.group(2)]}, but it is {a}.'
    m=re.fullmatch(rf'{C.T} saṅkhāro ceva \1 ca\.',ls)
    if m: a=C.e(m.group(1));return f'{C.cap(a)} is both a formation and {a}.'
    m=re.fullmatch(rf'(\S+) {C.T} ca ṭhapetvā avasesā na ceva (\S+) na ca {C.T}\.',s)
    if m: return f'Apart from {C.N[C.ACC[m.group(1)]]} and {C.e(m.group(2))}, the rest are neither {C.N[m.group(3)]} nor {C.e(m.group(4))}.'
    m=re.fullmatch(rf'{C.T} ca {C.T} ca ṭhapetvā avasesā na ceva {C.T} na ca {C.T}\.',s)
    if m: return f'Apart from {C.e(m.group(1))} and {C.e(m.group(2))}, the rest are neither {C.e(m.group(3))} nor {C.e(m.group(4))}.'
    return None
C.HOOK.insert(0,hook)
HD={'Saṅkhārayamakaṃ':'The Pairs on Formations','Suddhasaṅkhāravāro':'The Section on the Formations Alone','Suddhasaṅkhāramūlacakkavāro':'The Cycle Based on the Formations Alone','1-6. Paccuppannavārādi':'1–6. The Present and the Other Sections'}
tr,HDD=build(sub,RAW,FULL,[('parinibbāntānaṃ','parinibbantānaṃ')],None,HD)
if __name__=='__main__': go(['6-01-sankharayamaka.md','6-02-sankharayamaka.md'],tr,HDD)
