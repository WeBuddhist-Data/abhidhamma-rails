import re,sys
sys.path.insert(0,r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-hi\review')
import B_load
from B_load import *
B_load.IDRE=re.compile(r'\^([0-9a-zA-Z\-]+)\s*$')
d=load()
strip=lambda s: re.sub(r'\s*\^[0-9a-zA-Z\-]+\s*$','',s).strip()
N=[('eka',r'\b(eko|ekā|ekaṃ|ekena)\b','एक'),('dve',r'\b(dve|duve|dvīsu|dvinnaṃ)\b','दो|दोनों'),('tayo',r'\b(tayo|tīṇi|tisso|tīsu)\b','तीन'),('catu',r'\b(cattāro|cattāri|catūsu|catunnaṃ|catūhi)\b','चार|चारों'),('pañca',r'\bpañca\b','पाँच'),('cha',r'\bcha\b','छह'),('satta',r'\bsatta\b','सात'),('aṭṭha',r'\baṭṭha(su)?\b','आठ'),('dasa',r'\bdasa\b','दस'),('ekādasa',r'\bekādasa\b','ग्यारह'),('dvādasa',r'\bdvādasa\b','बारह')]
cnt=0
for x in d:
    if not x['f'].startswith(('3-','4-','5-')): continue
    p=re.sub(r'\[[^\]]*\]','',strip(x['p'])).lower();h=re.sub(r'\[[^\]]*\]','',strip(x['h']))
    for n,a,b in N:
        ca=len(re.findall(a,p)); cb=len(re.findall(b,h))
        if ca!=cb and (ca>0 or n in('pañca','cha','satta','aṭṭha','dasa','ekādasa','dvādasa')):
            cnt+=1
            print(x['id'] or x['f'][:4]+':'+str(x['i']),n,ca,cb)
print('total',cnt)
