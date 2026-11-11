import re,sys,collections
sys.path.insert(0,r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-hi\review')
import B_load
from B_load import *
B_load.IDRE=re.compile(r'\^([0-9a-zA-Z\-]+)\s*$')
d=load()
strip=lambda s: re.sub(r'\s*\^[0-9a-zA-Z\-]+\s*$','',s).strip()
out=open(sys.argv[2],'w',encoding='utf-8')
seen={}
tot=0;n=0
for x in d:
    if not x['f'].startswith(sys.argv[1]): continue
    p=strip(x['p']);h=strip(x['h'])
    m=re.match(r'Katame dhammā (.*?)\? (.*?)(?: – ime dhammā .*)?$',p)
    q=h.split('?',1)
    if m and len(q)==2:
        ans=m.group(2)
        ha=re.sub(r' – ये .*$','',q[1]).strip()
        k=ans.lower()
        if k in seen:
            if seen[k]!=ha: s='VAR %s P=%s\n H=%s\n H0=%s\n'%(x['id'],ans,ha,seen[k]); out.write(s);tot+=len(s)
            continue
        seen[k]=ha
        s='[%s] %s\nP %s\nH %s\n'%(x['id'] or x['i'],m.group(1),ans,ha)
    else:
        s='[%s]\nP %s\nH %s\n'%(x['id'] or x['i'],p,h)
    out.write(s);tot+=len(s);n+=1
print(tot,n)
