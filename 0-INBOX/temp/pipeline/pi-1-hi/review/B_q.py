import re,sys
sys.path.insert(0,r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-hi\review')
import B_load
from B_load import *
B_load.IDRE=re.compile(r'\^([0-9a-zA-Z\-]+)\s*$')
d=load()
strip=lambda s: re.sub(r'\s*\^[0-9a-zA-Z\-]+\s*$','',s).strip()
T=[('ajjhattikaṃ','आंतरिक'),('bāhiraṃ','बाह्य'),('oḷārikaṃ','स्थूल'),('sukhumaṃ','सूक्ष्म'),('dūre','दूर'),('santike','निकट'),
('anupādiṇṇupādāniyaṃ','कर्म से उत्पन्न न होकर भी आसक्ति'),('upādiṇṇupādāniyaṃ','कर्म से उत्पन्न और आसक्ति'),('anupādiṇṇaṃ','कर्म से उत्पन्न'),('upādiṇṇaṃ','कर्म से उत्पन्न'),
('sanidassanaṃ','दिखाई देने'),('anidassanaṃ','दिखाई न देने'),('sappaṭighaṃ','टकराव वाला'),('appaṭighaṃ','टकराव से रहित'),('mahābhūtaṃ','महाभूत'),('viññatti','अभिव्यक्ति'),
('cittasamuṭṭhānaṃ','मन से उत्पन्न'),('cittasahabhu','मन के साथ-साथ'),('cittānuparivatti','मन का अनुसरण'),('upādā','व्युत्पन्न'),('indriyaṃ','क्षमता'),('lahutā','हल्कापन'),('mudutā','मृदुता'),('kammaññatā','कार्य-योग्यता'),('upacayo','वृद्धि'),('santati','धारा'),('jaratā','बुढ़ापा'),('aniccatā','अनित्यता'),('āhāro','भोजन'),('vatthu','आधार'),('ārammaṇaṃ','विषय')]
neg=0;n=0
for x in d:
    if x['f'] not in('3-02-rupakandam','3-03-rupakandam'): continue
    m=re.match(r'Katamaṃ taṃ rūpaṃ (.*?)\?',strip(x['p']))
    if not m: continue
    q=m.group(1); n+=1
    hq=strip(x['h']).split('?')[0]
    bad=[]
    for a,b in T:
        if re.search(r'(^|\s|…)'+a+r'($|\s|…|\.)',q) and b not in hq: bad.append(a)
    # negation count
    pn=len(re.findall(r'(^|\s)(na|no)\s',q))+len(re.findall(r'anupādiṇṇaṃ',q))
    hn=len(re.findall(r'(नहीं|न होने|न करने| न देने|न होकर)',hq))
    if 'anidassanaṃ' in q: pn+=1
    if 'anupādiṇṇupādāniyaṃ' in q: pass
    if pn!=hn: bad.append(('neg',pn,hn))
    # question vs end
    pe=re.search(r'idaṃ taṃ rūpaṃ (.*?)\.?$',strip(x['p']))
    he=re.search(r'– यह भौतिक रूप (.*?)[।?]$',strip(x['h']))
    if pe and he and pe.group(1).strip('.?')!=q:
        bad.append(('Pend',pe.group(1)))
    if bad: print(x['id'] or x['i'],q,'|',hq[-60:],bad)
print('checked',n)
