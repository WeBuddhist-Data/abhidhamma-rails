import pathlib
tb={}
for l in pathlib.Path(r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi\pi-1-pali-hindi-termbase-plain.md').read_text(encoding='utf-8').splitlines():
    k,b=l.split(': {',1); tb[k]=b[:-1]
ci={k.lower():k for k in tb}
for k in 'ahetukaṃ,ahetuka,hetuvippayuttaṃ,sappaccayaṃ,sappaccaya,anārammaṇaṃ,anārammaṇa,nārammaṇaṃ,acetasikaṃ,ācayagāmi,apacayagāmi,nevasekkhanāsekkhaṃ,nevasekkha,neva,dassana,bhāvanāya,bhāvanā,pariyāpannaṃ,aniyataṃ,aniyyānikaṃ,jarābhibhūtaṃ,chahi,Ekakaṃ,Tikaṃ,Catukkaṃ,Pañcakaṃ,Chakkaṃ,Sattakaṃ,Aṭṭhakaṃ,Navakaṃ,ekavidhena,Duvidhena,Tividhena,Pañcavidhena,Sattavidhena,Aṭṭhavidhena,Navavidhena,Dasavidhena,Ekādasavidhena,upacayo,dūre,santike,vatthu,diṭṭhaṃ,sukhasamphassaṃ,dukkhasamphassaṃ,cakkhundriyaṃ,sotindriyaṃ,ghānindriyaṃ,jivhindriyaṃ,kāyindriyaṃ,savitakkasavicāraṃ,avitakkavicāramattaṃ,savitakka,savicāra,avitakka,avicāra,vicāramatta,hetuvippayutta,Ekakaniddeso,Rūpavibhatti,rūpavibhatti,saṃkiliṭṭha,nevavipākanavipākadhamma,navipāka,neva dassanena na bhāvanāya,hetu,na hetu,Sabbaṃ,sabbaṃ rūpaṃ,cattāro,upādāya rūpaṃ,manoviññeyyaṃ,cakkhuviññeyyaṃ,Rūpakaṇḍaṃ,Rūpakaṇḍa'.split(','):
    kk=ci.get(k.lower()); print(k,'=>',tb[kk] if kk else '##MISSING')
