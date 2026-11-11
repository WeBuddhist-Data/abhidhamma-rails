import re,sys,collections
sys.path.insert(0,r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-hi\review')
import B_load
from B_load import *
B_load.IDRE=re.compile(r'\^([0-9a-zA-Z\-]+)\s*$')
d=load()
strip=lambda s: re.sub(r'\s*\^[0-9a-zA-Z\-]+\s*$','',s).strip()
# (name, pali regex, hindi regex)
K=[
('kusala',r'(?<![a-zāīūṃṅñṭḍṇḷ])kusal',r'हितकर'),
('akusala',r'(?<![a-zāīūṃṅñṭḍṇḷ])akusal|nākusal|kusalākusal',r'हानिकर'),
('abyakata',r'abyākat',r'अनिर्धारित'),
('sekkha',r'(?<![a-zāīūṃṅñṭḍṇḷ])sekkh',r'सीखने'),
('asekkha',r'(?<![a-zāīūṃṅñṭḍṇḷ])asekkh|nāsekkh',r'सीखना पूरा|सीखने के बाद'),
('sasava',r'(?<![a-zāīūṃṅñṭḍṇḷ])sāsav',r'मन के मैल|मैलों'),
('anasava',r'(?<![a-zāīūṃṅñṭḍṇḷ])anāsav',r'मैलों से|मैल से|मैलों का विषय न'),
('sampayutta',r'(?<![a-zāīūṃṅñṭḍṇḷ])sampayutt|asampayutt|sampayuttā',r'जुड़|संयुक्त|सहयुक्त'),
('vippayutta',r'vippayutt',r'अलग'),
('sahetuka',r'sahetuk',r'मूल(ों)? सहित|मूलों वाल|मूल वाल'),
('ahetuka',r'(?<![a-zāīūṃṅñṭḍṇḷ])ahetuk',r'मूल(ों)? से रहित|मूल रहित'),
('kamavacara',r'kāmāvacar',r'इंद्रिय-सुख'),
('rupavacara',r'rūpāvacar',r'सूक्ष्म भौतिक'),
('arupavacara',r'(?<![a-zāīūṃṅñṭḍṇḷ])arūpāvacar',r'अभौतिक'),
('apariyapanna',r'apariyāpann',r'न समा'),
('lokuttara',r'lokuttar',r'लोकोत्तर|लोक से परे'),
('lokiya',r'lokiy',r'लौकिक'),
('pathama',r'paṭham',r'पहल|प्रथम'),
('dutiya',r'(?<![a-zāīūṃṅñṭḍṇḷ])dutiy',r'दूसर'),
('tatiya',r'(?<![a-zāīūṃṅñṭḍṇḷ])tatiy',r'तीसर'),
('catuttha',r'catutth',r'चौथ'),
('pañcama',r'pañcam',r'पाँचव'),
('dukkhapat',r'dukkhapaṭipad',r'कठिन|कष्ट'),
('sukhapat',r'sukhapaṭipad',r'सरल|सहज|सुगम'),
('dandha',r'dandh',r'धीम'),
('khippa',r'khipp',r'तीव्र|तेज|शीघ्र'),
('paritta',r'parittārammaṇ',r'सीमित'),
('appamana',r'appamāṇārammaṇ',r'असीम|अपरिमित'),
('magga',r'(?<![a-zāīūṃṅñṭḍṇḷ])magg',r'मार्ग'),
('phala',r'(?<![a-zāīūṃṅñṭḍṇḷ])phal',r'फल'),
('vipaka',r'vipāk',r'फल'),
('kiriya',r'kiriy',r'क्रिया'),
('atita',r'atīt',r'अतीत'),
('anagata',r'anāgat',r'भविष्य'),
('paccuppanna',r'paccuppann',r'वर्तमान'),
('ajjhatta',r'ajjhatt',r'आंतरिक'),
('bahiddha',r'bahiddh',r'बाह्य|बाहरी'),
('sanidassana',r'(?<![a-zāīūṃṅñṭḍṇḷ])sanidassan',r'दिखाई देने'),
('anidassana',r'(?<![a-zāīūṃṅñṭḍṇḷ])anidassan',r'दिखाई न देने'),
('sappatigha',r'sappaṭigh',r'टकराव वाल'),
('appatigha',r'(?<![a-zāīūṃṅñṭḍṇḷ])appaṭigh',r'टकराव से रहित'),
('upadinna',r'(?<![a-zāīūṃṅñṭḍṇḷ])upādiṇṇ',r'कर्म से उत्पन्न'),
('anupadinna',r'anupādiṇṇ',r'कर्म से उत्पन्न'),
]
for x in d:
    if x['f'].startswith('3-01'): continue
    p=re.sub(r'\[[^\]]*\]','',strip(x['p']).lower()); h=re.sub(r'\[[^\]]*\]','',strip(x['h']))
    bad=[]
    for n,a,b in K:
        ca=len(re.findall(a,p)); cb=len(re.findall(b,h))
        if ca and not cb or (ca==0 and cb and n not in('kusala','phala','vipaka','vippayutta','lokiya','pathama','dutiya','tatiya','catuttha','magga','kiriya','paritta','appamana','khippa','dandha','sampayutta','sahetuka','ahetuka','sekkha','asekkha','sasava','anasava','pañcama','dukkhapat','sukhapat','atita','anagata','paccuppanna','ajjhatta','bahiddha','akusala','abyakata','rupavacara','arupavacara','kamavacara','apariyapanna','lokuttara','upadinna','anupadinna','sanidassana','anidassana','sappatigha','appatigha')):
            bad.append((n,ca,cb))
    if bad: print(x['id'] or x['f'][:4]+':'+str(x['i']),bad)
